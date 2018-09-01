import csv
import io
import time
import json

from SqlModeling.DS18B20DatabaseClient import ds18b20_DbClient
from SqlModeling.microDpm680DatabaseClient import microDpm680_powers_DbClient, microDpm680_voltage_and_currents_DbClient
from SqlModeling.QBE2002_P25_PressureSensorDatabaseClient import qbe2002p25_DbClient
from SqlModeling.flowMeterDatabaseClient import flow_meter_DbClient

from sqlalchemy.exc import OperationalError


sensors_addresses = json.load(open('config.json'))['parameterTickerEndpointConfiguration']

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

def getHistoricalData(timerange_begin, csv=None):

    # Select all temperatures in the given timerange

    sql_query = "SELECT * FROM ds18b20_readings WHERE timestamp > " + timerange_begin + " ORDER BY id DESC"
    try:
        ds18b20_db_table_result = list(ds18b20_DbClient.session.execute(sql_query).fetchall())
    except OperationalError:
        time.sleep(0.01)
        return getHistoricalData(timerange_begin, csv)
    
    # Select all flows in the given timerange

    sql_query = "SELECT * FROM flow_meters_readings WHERE timestamp > " + timerange_begin + " ORDER BY id DESC"
    try:
        flows_db_table_result = list(flow_meter_DbClient.session.execute(sql_query).fetchall())
    except OperationalError:
        time.sleep(0.01)
        return getHistoricalData(timerange_begin, csv)

    # Select all pressures in the given timerange 

    sql_query = "SELECT * FROM qbe2002p25_readings WHERE timestamp > " + timerange_begin + " ORDER BY id DESC"
    try:
        pressures_db_table_result = list(qbe2002p25_DbClient.session.execute(sql_query).fetchall())
    except OperationalError:
        time.sleep(0.01)
        return getHistoricalData(timerange_begin, csv)

    # Select all power usages in the given timerange

    sql_query = "SELECT * FROM micro_dpm680_power_readings WHERE timestamp > " + timerange_begin + " ORDER BY id DESC"
    try:
        powers_db_table_result = list(microDpm680_powers_DbClient.session.execute(sql_query).fetchall())
    except OperationalError:
        time.sleep(0.01)
        return getHistoricalData(timerange_begin, csv)

    # Check results lengths

    results = [ds18b20_db_table_result, flows_db_table_result, pressures_db_table_result, powers_db_table_result]
    results_lengths = []
    for result_length in results:
        results_lengths.append(len(result_length))

    for result in results:
        if len(result) == max(results_lengths):
            while len(result) > min(results_lengths):
                result.pop(result[len(result) - 1])

    for i in range(1, len(results)):
        if len(result[i] != len(result[i - 1])):
            print("You made a mistake")
    
    # Create JSONs

