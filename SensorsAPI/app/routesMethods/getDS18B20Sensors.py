from SqlModeling.DS18B20DatabaseClient import ds18b20_DbClient

from flask import jsonify

is_any_device_recognized = True

try:
    import w1thermsensor 
except:
    is_any_device_recognized = False


def get_connected_sensors(not_jsonified=None):
    if is_any_device_recognized:
        devices = w1thermsensor.W1ThermSensor.get_available_sensors()

        result = []
        for sensor in devices:
            result.append(sensor.id)

        if result is []:
            result = ds18b20_DbClient.select_distinct("sensor_id")
            return jsonify({'error': 'no device is currently connected, historical data will be retuned', 'result': result})
    if not_jsonified is None:
        return jsonify({'result': result})
    else:
        return result

    result = ds18b20_DbClient.select_distinct("sensor_id")
    if not_jsonified is None:
        return jsonify({'error': 'no device is currently connected, historical data will be retuned', 'result': result})
    else:
        return result