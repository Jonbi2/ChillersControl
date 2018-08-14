from SqlModeling.DS18B20DatabaseClient import ds18b20_DbClient

from flask import jsonify

import time


def ds18b20_get_data(device_id=None ,time_range_begin=None, time_range_end=None):

    if time_range_begin is None and time_range_end is None and device_id is None:
            result = ds18b20_DbClient.select_data()
            result = jsonify(result)
            return result

    if time_range_begin is int and time_range_end is int:  # timestamp is int !
        where_query = "WHERE timestamp > " + str(time_range_begin) + " AND timestamp < " + str(time_range_end) + " AND sensor_id = " + "'" +str(device_id) + "'"
        result =  ds18b20_DbClient.select_data("*", where_query)
        result = jsonify(result)
        return result

    if time_range_begin is None and time_range_end is None:
        result = ds18b20_DbClient.select_data("*", "WHERE sensor_id = " + str(device_id))
        result = jsonify(str(result))
        return result

    if time_range_end is None:
        where_query = "WHERE timestamp > " + str(time_range_begin) + " AND timestamp < " + str(round(time.time())) + " AND sensor_id = " + str(device_id)
        result =  ds18b20_DbClient.select_data("*", where_query)
        result = jsonify(result)
        return result


    return jsonify({'error': 'wrong arguments have been given'})


    
