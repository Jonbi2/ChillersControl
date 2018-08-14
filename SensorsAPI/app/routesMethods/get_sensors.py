from .getDS18B20Sensors import get_connected_sensors as fetch_all_ds18b20

from flask import jsonify

def get_sensors():
    sensors = {'sensors': []}

    # Micro DPM 680

    name = 'micro_dpm_680'
    sensors_list = ['micro_dpm_680_1']
    route = '/micro_dmp_680/get_data'
    params = {'time_range_begin': 'timestamp', 'time_range_end': 'timestamp'}

    micro_dpm_680 = {'name': name, 'sensors_list': sensors_list, 'route': route, 'params': params}
    sensors['sensors'].append(micro_dpm_680)


    # DS18B20

    name = 'ds18b20'
    sensors_list = fetch_all_ds18b20()
    route = '/ds18b20/get_data'
    params = {'id': 'sensor_id', 'time_range_begin': 'timestamp', 'time_range_end': 'timestamp'}

    ds18b20 = {'name': name, 'sensors_list': sensors_list, 'route': route, 'params': params}
    sensors['sensors'].append(ds18b20)

    print(sensors)

    return jsonify(sensors)
