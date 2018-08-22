import requests
import xmltodict
import json
import time
import termcolor

try:
    import w1thermsensor 
except:
    print("Kernel is not configured to use 1wire protocol")

from tqdm import tqdm

from SqlModeling.DS18B20DatabaseClient import DS18B20DatabaseClient

def get_ds18b20_data():
    devices = w1thermsensor.W1ThermSensor.get_available_sensors()
    result = []
    for sensor in devices:
        try:
            params = {}
            params['reading'] = sensor.get_temperature()
            params['sensor_id'] = sensor.id
            result.append(params)
        except w1thermsensor.errors.SensorNotReadyError:
            raise RuntimeError("DS18B20 sensors are not ready to start measurments")
    return result

