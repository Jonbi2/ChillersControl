import requests
import xmltodict
import json
import time
import termcolor
import w1thermsensor 

from tqdm import tqdm

from SqlModeling.DS18B20DatabaseClient import DS18B20DatabaseClient

def get_ds18b20_data():
    devices = w1thermsensor.W1ThermSensor.get_available_sensors()
    result = []
    for sensor in devices:
        params = {}
        params['reading'] = sensor.get_temperature()
        params['sensor_id'] = sensor.id
        result.append(params)
    return result

