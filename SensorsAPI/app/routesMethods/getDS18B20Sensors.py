from SqlModeling.DS18B20DatabaseClient import ds18b20_DbClient

from flask import jsonify

is_any_device_recognized = True

try:
    import w1thermsensor 
except:
    is_any_device_recognized = False


def get_connected_sensors():
    if is_any_device_recognized:
        devices = w1thermsensor.W1ThermSensor.get_available_sensors()
        result = []
        for sensor in devices:
            result.append(sensor.id)
        result = jsonify(result)
        return result
    result = ds18b20_DbClient.select_distinct("sensor_id")
    return jsonify({'error': 'no device is currently connected, historical data will be retuned', 'result': result})