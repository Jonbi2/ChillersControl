from flask import jsonify

from SqlModeling.DS18B20DatabaseClient import ds18b20_DbClient
from SqlModeling.microDpm680DatabaseClient import microDpm680_powers_DbClient, microDpm680_voltage_and_currents_DbClient
from SqlModeling.QBE2002_P25_PressureSensorDatabaseClient import qbe2002p25_DbClient
from SqlModeling.flowMeterDatabaseClient import flow_meter_DbClient

from app.routesMethods.getDS18B20Sensors import get_connected_sensors

# from start_sensors import pressures, flows, temperatures, powers, currents

# print(temperatures)
# print(flows)
# print(pressures)
# print(currents)
# print(powers)

import time
import datetime

import random

params_dict = {}

def get_parameters_ticker():

    # flow = flow_meter_DbClient.select_data()[0]['reading']
    # power_usage = microDpm680_powers_DbClient.select_data()[0]['P1']
    # temperature = ds18b20_DbClient.select_data()[0]['temperature']

    variable = random.randint(10, 99)

    sensors = get_connected_sensors(True)
    temperatures = {}

    for sensor_temperature in sensors:
        temperatures[sensor_temperature] = ds18b20_DbClient.select_data('*', "WHERE sensor_id=" + '"' + str(sensor_temperature) + '"')[0]['temperature']
    
    t_ot_address = str(list(temperatures.keys())[0])
    t_p1_address = str(list(temperatures.keys())[1])
    t_p2_address = str(list(temperatures.keys())[2])
    t_p3_address = str(list(temperatures.keys())[3])
    t_p4_address = str(list(temperatures.keys())[4])
    t_ev_address = str(list(temperatures.keys())[5])
    t_sh_address = str(list(temperatures.keys())[6])
    t_sc_address = str(list(temperatures.keys())[7])

    l_p = qbe2002p25_DbClient.select_data('*', 'WHERE sensor_id=0')[0]['pressure']
    h_p = qbe2002p25_DbClient.select_data('*', 'WHERE sensor_id=1')[0]['pressure']

    flow_1 = flow_meter_DbClient.select_data("*", "WHERE sensor_id=0")[0]['reading']
    flow_2 = flow_meter_DbClient.select_data("*", "WHERE sensor_id=1")[0]['reading']



    result = {'datetime': str(datetime.datetime.now()),
              'timestamp': round(time.time()),
              't_zb': variable,
              't_ot': temperatures[t_ot_address],
              't_p1': temperatures[t_p1_address], 
              't_p2': temperatures[t_p2_address],
              't_p3': temperatures[t_p3_address],
              't_p4': temperatures[t_p4_address],
              'l_p': l_p,
              't_ev': temperatures[t_ev_address],
              't_sh': temperatures[t_sh_address],
              'SH': None,
              'h_p': h_p,
              't_con': None,
              't_sc': temperatures[t_sc_address],
              's_c': None,
              'flow_1': flow_1,
              't_1': None,
              't_2': None,
              'delta_t': None,
              'p_1': None,
              'flow_2': flow_2,
              't_2_2': None,
              'delta_t_2': None,
              'p_2': None,
              'p': None
              }

    result = {'result': result}

    # temperature = ds18b20_DbClient.select_data("*", "WHERE sensor_id = " + str("011316bc4db8"))[0]

    return jsonify(result)

