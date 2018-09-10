import csv
import io
import time
import json

from SqlModeling.DS18B20DatabaseClient import ds18b20_DbClient
from SqlModeling.microDpm680DatabaseClient import microDpm680_powers_DbClient, microDpm680_voltage_and_currents_DbClient
from SqlModeling.QBE2002_P25_PressureSensorDatabaseClient import qbe2002p25_DbClient
from SqlModeling.flowMeterDatabaseClient import flow_meter_DbClient

from sqlalchemy.exc import OperationalError

from flask import jsonify, send_file

r404a_datasheet = dict(json.load(open('utils/refrigerantsTables/R404A.json')))
r134a_datasheet = dict(json.load(open('utils/refrigerantsTables/R134A.json')))

def convert_json_to_list(datasheet):
    result = []
    pressures = list(datasheet.keys())
    temperatures = list(datasheet.values())
    for i in range(len(pressures)):
        result.append([float(pressures[i]), temperatures[i]])
    return result

def get_temperature_from_pressure(refrigerant, pressure):
    if refrigerant == "R404A":
        datasheet = convert_json_to_list(r404a_datasheet)
    elif refrigerant == "R134A":
        datasheet = convert_json_to_list(r134a_datasheet)
    else:
        raise AttributeError("The given refrigerant is not supported")

    for i in range(len(datasheet)):
        if i == len(datasheet) -1:
            raise IndexError("Out of range")
        pressure_1 = datasheet[i][0]
        pressure_2 = datasheet[i + 1][0]

        if pressure >= pressure_1 and pressure <= pressure_2:
            x1 = pressure_1
            x2 = pressure_2

            y1 = datasheet[i][1]
            y2 = datasheet[i + 1][1]

            a = (y2 - y1) / (x2 - x1)

            b = (y1 - a * x1)

            return a * pressure + b

def count_q(flow, output_temperature, input_temperature): 
    result = flow * 4.2 * 0.0995 * (output_temperature - input_temperature)
    return result

def count_cop(q_1, q_2, power):  
    if power == 0:
        return None
    result = (q_1 + q_2) / power
    return result

def convert_json_to_csv(json_variable):
    try:
        rows_list = [list(json_variable[0].keys())]
    except IndexError:
        rows_list = []
    for json in json_variable:
        rows_list.append(list(json.values()))

    proxy = io.StringIO()

    writer = csv.writer(proxy)
    for row in rows_list:
        writer.writerow(row)

    mem = io.BytesIO()
    mem.write(proxy.getvalue().encode('utf-8'))
    mem.seek(0)
    proxy.close()

    json_variable = send_file(
        mem,
        as_attachment=True,
        attachment_filename='ticker.csv',
        mimetype='text/csv'
    )

    return json_variable

def get_historical_ticker(timerange_begin=None, csv=None):  
    if timerange_begin is None:
        timerange_begin = time.time() - 24 * 60 * 60

    sensors_addresses = json.load(open('config.json'))['parameterTickerEndpointConfiguration']
    results_len = []
    
    # Set temperatures
    temperatures = {} 

    for sensor in sensors_addresses['Temperatures']:
        sql_query = "SELECT reading FROM ds18b20_readings WHERE timestamp > " + str(timerange_begin) + " AND sensor_id=" + '"' + sensors_addresses['Temperatures'][sensor] + '"'
        try:
            temperatures[sensor] = list(ds18b20_DbClient.session.execute(sql_query).fetchall())
        except OperationalError:
            time.sleep(0.01)
            return get_historical_ticker(timerange_begin, csv)
        results_len.append(len(temperatures[sensor]))

    # Set pressures
    pressures = {}
    for sensor in sensors_addresses['Pressures']:
        sql_query = "SELECT reading FROM qbe2002p25_readings WHERE timestamp > " + str(timerange_begin) + " AND sensor_id=" + '"' + str(sensors_addresses['Pressures'][sensor]) + '"'
        try:
            pressures[sensor] = list(qbe2002p25_DbClient.session.execute(sql_query).fetchall())
        except OperationalError:
            time.sleep(0.01)
            return get_historical_ticker(timerange_begin, csv)
        results_len.append(len(pressures[sensor]))

    # Set flows
    flows = {}
    for sensor in sensors_addresses['Flows']:
        sql_query = "SELECT reading FROM flow_meters_readings WHERE timestamp > " + str(timerange_begin) + " AND sensor_id=" + '"' + str(sensors_addresses['Flows'][sensor]) + '"'
        print(sensor)
        try:
            flows[sensor] = list(flow_meter_DbClient.session.execute(sql_query).fetchall())
        except OperationalError:
            time.sleep(0.01)
            return get_historical_ticker(timerange_begin, csv)
        results_len.append(len(flows[sensor]))
    
    # Set timestamp and datetime
    sql_query = "SELECT reading FROM flow_meters_readings WHERE timestamp > " + str(timerange_begin) + " AND sensor_id=" + '"' + str(sensors_addresses['Flows'][40]) + '"'
    try:
        times = list(flow_meter_DbClient.session.execute(sql_query).fetchall())
        print(times[len(times) - 1])
        print(times)
    except OperationalError:
        time.sleep(0.01)
        return get_historical_ticker(timerange_begin, csv)

    # Set powers
    sql_query = "SELECT P4 FROM micro_dpm680_power_readings WHERE timestamp > " + str(timerange_begin)
    try:
        powers = list(microDpm680_powers_DbClient.session.execute(sql_query).fetchall())
    except OperationalError:
        time.sleep(0.01)
        return get_historical_ticker(timerange_begin, csv)
    results_len.append(len(powers))

    # Generate result JSON array
    result = []
    for i in range(min(results_len) - 1, 0, -1):
        i_json = {}
        # Set temperatures
        for sensor in sensors_addresses['Temperatures']:
            i_json[str(sensor)[:-15]] = temperatures[sensor][i][0]
        # Set pressures
        for sensor in sensors_addresses['Pressures']:
            i_json[str(sensor)[:-15]] = pressures[sensor][i][0]
        # Set flows
        for sensor in sensors_addresses['Flows']:
            i_json[str(sensor)[:-15]] = flows[sensor][i][0]
        # Set power
        i_json['P'] = powers[i][0]
        i_json['t_con'] = get_temperature_from_pressure("R404A", i_json['h_p']) 
        i_json['t_env'] = get_temperature_from_pressure("R404A", i_json['l_p']) 
        i_json['Q1'] = count_q(i_json['flow_1'], i_json['t_wy_1'], i_json['t_we_1']) 
        i_json['Q2'] = count_q(i_json['flow_2'], i_json['t_wy_2'], i_json['t_we_2']) 
        i_json['CoP'] = count_cop(i_json['Q1'], i_json['Q2'], powers[i][0]) 
        i_json['date'] = times[i][0]
        i_json['timestamp'] = times[i][1]
        result.append(i_json)
        if i == min(results_len) - 1:
            print(times[i], times[0])
    if csv is None:
        print(len(times), " ", min(results_len), len(result))
        print(results_len)
        print(times[len(times) - 1])
        return jsonify(result)
    else:
        return convert_json_to_csv(result)


        

        

