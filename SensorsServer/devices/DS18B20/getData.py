try:
    import w1thermsensor 
except:
    print("Kernel is not configured to use 1wire protocol")

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

