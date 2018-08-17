from flask import jsonify

from SqlModeling.DS18B20DatabaseClient import ds18b20_DbClient
from SqlModeling.microDpm680DatabaseClient import microDpm680_DbClient
from SqlModeling.QBE2002_P25_PressureSensorDatabaseClient import qbe2002p25_DbClient
from SqlModeling.flowMeterDatabaseClient import flow_meter_DbClient

import time
import datetime
import json


def get_parameters_ticker():
    result = {'datetime': str(datetime.datetime.now()),
              'timestamp': round(time.time()),
              'temperature_on_compressor_output': None,
              'temperature_on_condenser_input': None,
              'temperature_on_condenser_output': None,
              'liquid_freon_temperature_on_input': None, 
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

