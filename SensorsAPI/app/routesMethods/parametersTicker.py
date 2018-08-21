from flask import jsonify

from SqlModeling.DS18B20DatabaseClient import ds18b20_DbClient
from SqlModeling.microDpm680DatabaseClient import microDpm680_powers_DbClient, microDpm680_voltage_and_currents_DbClient
from SqlModeling.QBE2002_P25_PressureSensorDatabaseClient import qbe2002p25_DbClient
from SqlModeling.flowMeterDatabaseClient import flow_meter_DbClient

# from start_sensors import pressures, flows, temperatures, powers, currents

# print(temperatures)
# print(flows)
# print(pressures)
# print(currents)
# print(powers)

import time
import datetime

import random
import requests

params_dict = {}

def get_parameters_ticker():

    # flow = flow_meter_DbClient.select_data()[0]['reading']
    # power_usage = microDpm680_powers_DbClient.select_data()[0]['P1']
    # temperature = ds18b20_DbClient.select_data()[0]['temperature']

    variable = random.randint(10, 99)

    sensors = requests.get('http://192.168.1.147:5000/get_connected_ds18b20').json()['result']
    temperatures = {}

    for sensor_temperature in sensors:
        temperatures[sensor_temperature] = ds18b20_DbClient.select_data('*', "WHERE sensor_id=" + '"' + str(sensor_temperature) + '"')[0]['temperature']
    
    print(temperatures)

    t_ot_address = str(list(temperatures.keys())[0])
    t_p1_address = str(list(temperatures.keys())[1])
    t_p2_address = str(list(temperatures.keys())[2])

    result = {'datetime': str(datetime.datetime.now()),
              'timestamp': round(time.time()),
              't_zb': variable,
              't_ot': temperatures[t_ot_address],
              't_p1': temperatures[t_p1_address], 
              't_p2': temperatures[t_p2_address],
              't_p3': None,
              't_p4': None,
              'p_lp': None,
              't_ev': None,
              't_sh': None,
              'SH': None,
              'p_hp': None,
              't_con': None,
              't_sc': None,
              's_c': None,
              'flow_1': None,
              't_1': None,
              't_2': None,
              'delta_t': None,
              'p_1': None,
              'flow_2': None,
              't_2_2': None,
              'delta_t_2': None,
              'p_2': None,
              'p': None
              }

    result = {'result': result}

    # temperature = ds18b20_DbClient.select_data("*", "WHERE sensor_id = " + str("011316bc4db8"))[0]

    return jsonify(result)

