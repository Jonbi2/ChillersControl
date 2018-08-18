from SqlModeling.QBE2002_P25_PressureSensorDatabaseClient import qbe2002p25_DbClient

from flask import jsonify

import time


def qbe2002_p25_get_data(device_id=None ,time_range_begin=None, time_range_end=None):

    if time_range_begin is None and time_range_end is None and device_id is None:
            result = qbe2002p25_DbClient.select_data()
            result = jsonify(result)
            return result

    if time_range_begin is None and time_range_end is None:
        result = qbe2002p25_DbClient.select_data("*", "WHERE sensor_id = " + str(device_id))
        result = jsonify(result)
        return result

    if time_range_begin is int and time_range_end is int:  # timestamp is int !
        where_query = "WHERE timestamp > " + str(time_range_begin) + " AND timestamp < " + str(time_range_end) + " AND sensor_id = " + "'" +str(device_id) + "'"
        result =  qbe2002p25_DbClient.select_data("*", where_query)
        result = jsonify(result)
        return result

    if time_range_end is None:
        where_query = "WHERE timestamp > " + str(time_range_begin) + " AND timestamp < " + str(round(time.time())) + " AND sensor_id = " + str(device_id)
        result =  qbe2002p25_DbClient.select_data("*", where_query)
        result = jsonify(result)
        return result


    return jsonify({'error': 'wrong arguments have been given'})


    