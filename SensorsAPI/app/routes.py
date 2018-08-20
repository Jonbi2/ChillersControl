from flask_restful import Resource, Api
from flask import request

from . import app

from .routesMethods.microDpm680 import micro_dmp_680_get_voltages_data, micro_dmp_680_get_powers_data
from .routesMethods.DS18B20 import ds18b20_get_data
from .routesMethods.getDS18B20Sensors import get_connected_sensors as fetch_all_ds18b20
from .routesMethods.get_sensors import get_sensors as fetch_all_sensors
from .routesMethods.parametersTicker import get_parameters_ticker
from .routesMethods.flowMeter import flow_meter_get_data
from .routesMethods.QBE2002_P25 import qbe2002_p25_get_data


@app.route('/getSensors', methods=['GET'])
def get_sensors():
    return fetch_all_sensors()

@app.route('/qbe2002_p25/get_data')
def pressure_sensor():
    sensor_id = request.args.get('sensor_id')

    time_range_begin = request.args.get('time_range_begin')
    time_range_end = request.args.get('time_begin_end')

    csv = request.args.get('csv')
    if csv is not None:
        csv = True

    return qbe2002_p25_get_data(sensor_id, time_range_begin, time_range_end, csv)

@app.route('/micro_dmp_680_currents/get_data', methods=['GET'])
def micro_dmp_680_currents():
    time_range_begin = request.args.get('time_range_begin')
    time_range_end = request.args.get('time_range_end')

    csv = request.args.get('csv')
    if csv is not None:
        csv = True

    return micro_dmp_680_get_voltages_data(None, time_range_begin, time_range_end, csv)

@app.route('/micro_dmp_680_powers/get_data', methods=['GET'])
def micro_dmp_680_powers():
    time_range_begin = request.args.get('time_range_begin')
    time_range_end = request.args.get('time_range_end')

    csv = request.args.get('csv')
    if csv is not None:
        csv = True
        
    return micro_dmp_680_get_powers_data(None ,time_range_begin, time_range_end, csv)

@app.route('/flow_meter/get_data', methods=['GET'])
def flow_meter():
    sensor_id = request.args.get('sensor_id')

    time_range_begin = request.args.get('time_range_begin')
    time_range_end = request.args.get('time_begin_end')

    csv = request.args.get('csv')
    if csv is not None:
        csv = True
        
    return flow_meter_get_data(sensor_id, time_range_begin, time_range_end, csv)

@app.route('/ds18b20/get_data', methods=['GET'])
def ds18b20():
    sensor_id = request.args.get('sensor_id')

    time_range_begin = request.args.get('time_range_begin')
    time_range_end = request.args.get('time_begin_end')

    csv = request.args.get('csv')
    if csv is not None:
        csv = True
        
    return ds18b20_get_data(sensor_id, time_range_begin, time_range_end, csv)

@app.route('/get_connected_ds18b20', methods=['GET'])
def get_connected_ds18b20():
    return fetch_all_ds18b20()

@app.route('/parametersTicker.json', methods=['GET'])
def parameters_ticker():
    return get_parameters_ticker()
