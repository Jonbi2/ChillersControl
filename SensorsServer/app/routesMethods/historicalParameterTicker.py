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
    
    # Set temperatures
    temperatures = {} 

    for sensor in sensors_addresses['Temperatures']:
        sql_query = "SELECT reading FROM ds18b20_readings WHERE timestamp > " + str(timerange_begin) + " AND sensor_id=" + '"' + sensors_addresses['Temperatures'][sensor] + '"'
        temperatures[sensor] = list(ds18b20_DbClient.session.execute(sql_query).fetchall())
        print(len(temperatures[sensor]))

    # Set pressures
    pressures = {}
    for sensor in sensors_addresses['Pressures']:
        sql_query = "SELECT reading FROM qbe2002p25_readings WHERE timestamp > " + str(timerange_begin) + " AND sensor_id=" + '"' + str(sensors_addresses['Pressures'][sensor]) + '"'
        pressures[sensor] = list(qbe2002p25_DbClient.session.execute(sql_query).fetchall())
        print(len(pressures[sensor]))

    # Set flows
    flows = {}
    for sensor in sensors_addresses['Flows']:
        sql_query = "SELECT reading FROM qbe2002p25_readings WHERE timestamp > " + str(timerange_begin) + " AND sensor_id=" + '"' + str(sensors_addresses['Flows'][sensor]) + '"'
        flows[sensor] = list(flow_meter_DbClient.session.execute(sql_query).fetchall())
        print(len(flows[sensor]))

    # Set powers
    powers = {}
    


get_historical_ticker()
        

        

