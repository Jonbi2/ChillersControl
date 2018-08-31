from flask import jsonify

from SqlModeling.DS18B20DatabaseClient import ds18b20_DbClient
from SqlModeling.microDpm680DatabaseClient import microDpm680_powers_DbClient, microDpm680_voltage_and_currents_DbClient
from SqlModeling.QBE2002_P25_PressureSensorDatabaseClient import qbe2002p25_DbClient
from SqlModeling.flowMeterDatabaseClient import flow_meter_DbClient

from app.routesMethods.getDS18B20Sensors import get_connected_sensors

import time
import datetime
import json 


def get_parameters_ticker():
    # power_usage = microDpm680_powers_DbClient.select_data()[0]['P1']

    sensors_addresses = json.load(open('config.json'))['parameterTickerEndpointConfiguration']

    def get_temperature_from_sensor(sensor_id):
        sensor_id = '"' + str(sensor_id) + '"'
        db_result = ds18b20_DbClient.select_data("*", "WHERE sensor_id=" + sensor_id + " ORDER BY id DESC LIMIT 1")
        if len(db_result) < 1:
            return None
        else:
            return db_result[0]['temperature']
    def get_pressure_from_sensor(sensor_id):
        sensor_id = '"' + str(sensor_id) + '"'
        db_result = qbe2002p25_DbClient.select_data("*", "WHERE sensor_id=" + sensor_id + " ORDER BY id DESC LIMIT 1")
        if len(db_result) < 1:
            return None
        else:
            return db_result[0]['pressure']
    def get_flow_from_sensor(sensor_id):
        sensor_id = '"' + str(sensor_id) + '"'
        db_result = flow_meter_DbClient.select_data("*", "WHERE sensor_id=" + sensor_id + " ORDER BY id DESC LIMIT 1")
        if len(db_result) < 1:
            return None
        else:
            return db_result[0]['reading']

    # Temperatures setup

    t_zb_sensor_address = sensors_addresses['Temperatures']['t_zb_sensor_address']
    t_ot_sensor_address = sensors_addresses['Temperatures']['t_ot_sensor_address']
    t_p1_sensor_address = sensors_addresses['Temperatures']['t_p1_sensor_address']
    t_p2_sensor_address = sensors_addresses['Temperatures']['t_p2_sensor_address']
    t_p3_sensor_address = sensors_addresses['Temperatures']['t_p3_sensor_address']
    t_p4_sensor_address = sensors_addresses['Temperatures']['t_p4_sensor_address']
    t_we_2_sensor_address = sensors_addresses['Temperatures']['t_we_2_sensor_address']
    t_sh_sensor_address = sensors_addresses['Temperatures']['t_sh_sensor_address']
    t_sc_sensor_address = sensors_addresses['Temperatures']['t_sc_sensor_address']
    t_wy_1_sensor_address = sensors_addresses['Temperatures']['t_wy_1_sensor_address']
    t_we_1_sensor_address = sensors_addresses['Temperatures']['t_we_1_sensor_address']
    t_wy_2_sensor_address = sensors_addresses['Temperatures']['t_wy_2_sensor_address']

    # Pressures setup

    h_p_sensor_address = sensors_addresses['Pressures']['h_p_sensor_address']
    l_p_sensor_address = sensors_addresses['Pressures']['l_p_sensor_address']

    # Flows setup

    flow_1_sensor_address = sensors_addresses['Flows']['flow_1_sensor_address']
    flow_2_sensor_address = sensors_addresses['Flows']['flow_2_sensor_address']

    # Power setup

    power_usage = microDpm680_powers_DbClient.select_data("*", "ORDER BY id DESC LIMIT 1")[0]['P4']

    result = {'datetime': str(datetime.datetime.now()),
              'timestamp': round(time.time()),
              't_zb': get_temperature_from_sensor(t_zb_sensor_address),
              't_ot': get_temperature_from_sensor(t_ot_sensor_address),
              't_p1': get_temperature_from_sensor(t_p1_sensor_address), 
              't_p2': get_temperature_from_sensor(t_p2_sensor_address),
              't_p3': get_temperature_from_sensor(t_p3_sensor_address),
              't_p4': get_temperature_from_sensor(t_p4_sensor_address),
              'l_p': get_pressure_from_sensor(l_p_sensor_address),
              't_we_2': get_temperature_from_sensor(t_we_2_sensor_address),
              't_sh': get_temperature_from_sensor(t_sh_sensor_address),
              'h_p': get_pressure_from_sensor(h_p_sensor_address),
              't_sc': get_temperature_from_sensor(t_sc_sensor_address),
              'flow_1': get_flow_from_sensor(flow_1_sensor_address),
              't_wy_1': get_temperature_from_sensor(t_wy_1_sensor_address),
              't_we_1': get_temperature_from_sensor(t_we_1_sensor_address),
              'flow_2': get_flow_from_sensor(flow_2_sensor_address),
              't_wy_2': get_temperature_from_sensor(t_wy_2_sensor_address),
              'p': power_usage
              }

    result = {'result': result}
    return jsonify(result)

