import csv
import io
import time
import json

from SqlModeling.DS18B20DatabaseClient import ds18b20_DbClient
from SqlModeling.microDpm680DatabaseClient import microDpm680_powers_DbClient, microDpm680_voltage_and_currents_DbClient
from SqlModeling.QBE2002_P25_PressureSensorDatabaseClient import qbe2002p25_DbClient
from SqlModeling.flowMeterDatabaseClient import flow_meter_DbClient

from sqlalchemy.exc import OperationalError

from flask import jsonify


def convert_pressure_to_temperature(refrigerant, pressure):  
    if refrigerant == "R404A":
        directory = 'utils/refrigerantsTables/R404A.json'
    elif refrigerant == "R134A":
        directory = 'utils/refrigerantsTables/R134A.json'
    else:
        raise AttributeError("The given refrigerant is not supported")

    data_json = dict(json.load(open(directory)))

    # Convert json to array
    pressures_list = []
    for i in range(0, len(data_json.keys()) - 1):
        row = [float(list(data_json.keys())[i]), float(list(data_json.values())[i])]
        pressures_list.append(row)

    for i in range(0, len(pressures_list) - 1):
        if i == len(pressures_list) - 1:
            raise AttributeError("Out of range")
        
        range_begin = pressures_list[i][0]
        range_end = pressures_list[i + 1][0]

        if pressure >= range_begin and pressure <= range_end:
            x1 = range_begin
            x2 = range_end

            y1 = pressures_list[i][1]
            y2 = pressures_list[i + 1][1]

            a = (y2 - y1) / (x2 - x1)
            b = (y1 - a * x1)
            return a * pressure + b

def count_q(flow, output_temperature, input_temperature): 
    result = flow * 4.2 * 0.0995 * (output_temperature - input_temperature)
    return result

def count_cop(q_1, q_2, power):  
    result = (q_1 + q_2) / power
    return result

def convert_json_to_csv(json_variable):  # TODO
    pass

def get_historical_ticker(timerange_begin=None, csv=None):  
    if timerange_begin is None:
        timerange_begin = time.time() - 24 * 60 * 60

    sensors_addresses = json.load(open('config.json'))['parameterTickerEndpointConfiguration']
    results_len = []
    
    # Set temperatures
    temperatures = {} 

    for sensor in sensors_addresses['Temperatures']:
        sql_query = "SELECT reading FROM ds18b20_readings WHERE timestamp > " + str(timerange_begin) + " AND sensor_id=" + '"' + sensors_addresses['Temperatures'][sensor] + '"'
        temperatures[sensor] = list(ds18b20_DbClient.session.execute(sql_query).fetchall())
        results_len.append(len(temperatures[sensor]))

    # Set pressures
    pressures = {}
    for sensor in sensors_addresses['Pressures']:
        sql_query = "SELECT reading FROM qbe2002p25_readings WHERE timestamp > " + str(timerange_begin) + " AND sensor_id=" + '"' + str(sensors_addresses['Pressures'][sensor]) + '"'
        pressures[sensor] = list(qbe2002p25_DbClient.session.execute(sql_query).fetchall())
        results_len.append(len(pressures[sensor]))

    # Set flows
    flows = {}
    for sensor in sensors_addresses['Flows']:
        sql_query = "SELECT reading FROM flow_meters_readings WHERE timestamp > " + str(timerange_begin) + " AND sensor_id=" + '"' + str(sensors_addresses['Flows'][sensor]) + '"'
        flows[sensor] = list(flow_meter_DbClient.session.execute(sql_query).fetchall())
        results_len.append(len(flows[sensor]))
    
    # Set timestamp and datetime
    sql_query = "SELECT date, timestamp FROM flow_meters_readings WHERE timestamp > " + str(timerange_begin)
    times = list(flow_meter_DbClient.session.execute(sql_query).fetchall())

    # Set powers
    sql_query = "SELECT P4 FROM micro_dpm680_power_readings WHERE timestamp > " + str(timerange_begin)
    powers = list(microDpm680_powers_DbClient.session.execute(sql_query).fetchall())
    results_len.append(len(powers))

    # Generate result JSON array

    result = []
    for i in range(min(results_len) -1, -1, -1):
        i_json = {}
        # Set temperatures
        for sensor in sensors_addresses['Temperatures']:
            i_json[str(sensor)[:-15]] = temperatures[sensor][i]
        # Set pressures
        for sensor in sensors_addresses['Pressures']:
            i_json[str(sensor)[:-15]] = pressures[sensor][i]
        # Set flows
        for sensor in sensors_addresses['Flows']:
            i_json[str(sensor)[:-15]] = flows[sensor][i]
        # Set power
        i_json['P'] = powers[i]
        i_json['t_con'] = convert_pressure_to_temperature("R404A", i_json['h_p']) 
        i_json['t_env'] = convert_pressure_to_temperature("R404A", i_json['l_p']) 
        i_json['Q1'] = count_q(i_json['flow_1'], i_json['t_wy_1'], i_json['t_we_1']) 
        i_json['Q2'] = count_q(i_json['flow_2'], i_json['t_wy_2'], i_json['t_we_2']) 
        i_json['CoP'] = count_cop(i_json['Q1'], i_json['Q2'], powers[i]) 
        i_json['date'] = times[i][0]
        i_json['timestamp'] = times[i][1]
        result.append(i_json)
    if csv is None:
        return jsonify(result)


# get_historical_ticker()
        

        

