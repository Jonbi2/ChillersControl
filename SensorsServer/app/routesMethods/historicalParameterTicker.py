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


sensors_addresses = json.load(open('config.json'))['parameterTickerEndpointConfiguration']

def get_historical_ticker(timerange_begin=None, csv=None):
    if timerange_begin is None:
        timerange_begin = time.time() - 24 * 60 * 60

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

    # Set powers
    sql_query = "SELECT P4 FROM micro_dpm680_power_readings WHERE timestamp > " + str(timerange_begin)
    powers = list(microDpm680_powers_DbClient.session.execute(sql_query).fetchall())
    results_len.append(len(powers))

    # Generate result JSON array

    result = []
    for i in range(min(results_len), -1, -1, -1):
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
        i_json['t_con'] = None
        i_json['t_env'] = None
        i_json['Q1'] = None
        i_json['Q2'] = None
        i_json['CoP'] = None
        result.append(i_json)
    return result


get_historical_ticker()
        

        

