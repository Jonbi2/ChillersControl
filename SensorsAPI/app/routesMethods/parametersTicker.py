from flask import jsonify

from SqlModeling.DS18B20DatabaseClient import ds18b20_DbClient
from SqlModeling.microDpm680DatabaseClient import microDpm680_powers_DbClient, microDpm680_voltage_and_currents_DbClient
from SqlModeling.QBE2002_P25_PressureSensorDatabaseClient import qbe2002p25_DbClient
from SqlModeling.flowMeterDatabaseClient import flow_meter_DbClient

import time
import datetime


def get_parameters_ticker():

    try:
        flow = flow_meter_DbClient.select_data()[0]['reading']
    except IndexError:
        flow = None
    try:
        power_usage = microDpm680_powers_DbClient.select_data()[0]['P1']
    except IndexError:
        print(microDpm680_powers_DbClient.select_data())
        power_usage = None
    try:
        temperature = ds18b20_DbClient.select_data()[0]['temperature']
    except IndexError:
        temperature = None
        

    result = {'datetime': str(datetime.datetime.now()),
              'timestamp': round(time.time()),
              'flow': flow,
              'power_usage': power_usage,
              'temperature': temperature, 
              'freons_temperature_on_compressor_output': None,
              'vapor_temperature_on_compressor_input': None,
              'temperature_inside_the_container': None,
              'neighbourhood_temperature': None,
              'temperature_on_the_roof': None,
              'superheating': None,
              'supercooling': None,
              'low_pressure': None,
              'high_pressure': None,
              'electric_power_collected': None,
              'temperature_on_roof_exchanger': None}

    result = {'result': result}

    # temperature = ds18b20_DbClient.select_data("*", "WHERE sensor_id = " + str("011316bc4db8"))[0]

    return jsonify(result)

