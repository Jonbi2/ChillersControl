from flask_restful import Resource, Api
from flask import request
from flask import jsonify

from . import app

from .routesMethods.microDpm680 import micro_dmp_680_get_data
from .routesMethods.DS18B20 import ds18b20_get_data
from .routesMethods.getDS18B20Sensors import get_connected_sensors as fetch_all_ds18b20
from .routesMethods.get_sensors import get_sensors as fetch_all_sensors


@app.route('/getSensors', methods=['GET'])
def get_sensors():
    return fetch_all_sensors()

@app.route('/micro_dmp_680/get_data', methods=['GET'])
def micro_dmp_680():
    time_range_begin = request.args.get('time_range_begin')
    time_range_end = request.args.get('time_range_end')
    return micro_dmp_680_get_data(time_range_begin, time_range_end)

@app.route('/ds18b20/get_data', methods=['GET'])
def ds18b20():
    sensor_id = request.args.get('sensor_id')

    if sensor_id is None:
        return jsonify({'error': 'sensor_id is not specified'})

    time_range_begin = request.args.get('time_range_begin')
    time_range_end = request.args.get('time_begin_end')
    return ds18b20_get_data(sensor_id, time_range_begin, time_range_end)

@app.route('/get_connected_ds18b20', methods=['GET'])
def get_connected_ds18b20():
    return fetch_all_ds18b20()
