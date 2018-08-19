from .getDS18B20Sensors import get_connected_sensors as fetch_all_ds18b20

from flask import jsonify

def get_sensors():
    sensors = {'sensors': []}

    # Micro DPM 680

    name = 'micro_dpm_680'
    sensors_list = ['micro_dpm_680_1']
    route = '/micro_dmp_680/get_data'
    params = {'time_range_begin': 'timestamp', 'time_range_end': 'timestamp', 'csv': 'boolean'}

    micro_dpm_680 = {'name': name, 'sensors_list': sensors_list, 'route': route, 'params': params}
    sensors['sensors'].append(micro_dpm_680)


    # DS18B20

    name = 'ds18b20'
    sensors_list = fetch_all_ds18b20(True)
    route = '/ds18b20/get_data'
    params = {'id': 'sensor_id', 'time_range_begin': 'timestamp', 'time_range_end': 'timestamp', 'csv': 'boolean'}

    ds18b20 = {'name': name, 'sensors_list': sensors_list, 'route': route, 'params': params}
    sensors['sensors'].append(ds18b20)

    # QBE2002_P25

    name = 'qbe2002_b25'
    sensors_list = ['qbe2002_b25_1']
    route = '/qbe2002_p25/get_data'
    params = {'time_range_begin': 'timestamp', 'time_range_end': 'timestamp', 'csv': 'boolean'}

    qbe2002_b25 = {'name': name, 'sensors_list': sensors_list, 'route': route, 'params': params}
    sensors['sensors'].append(qbe2002_b25)

    # Flow Meter 

    name = 'flow_meter'
    sensors_list = ['flow_meter_1']
    route = '/flow_meter/get_data'
    params = {'time_range_begin': 'timestamp', 'time_range_end': 'timestamp', 'csv': 'boolean'}

    flow_meter = {'name': name, 'sensors_list': sensors_list, 'route': route, 'params': params}
    sensors['sensors'].append(flow_meter)

    return jsonify(sensors)
