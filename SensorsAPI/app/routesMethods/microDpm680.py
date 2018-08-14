from SqlModeling.microDpm680DatabaseClient import microDpm680_DbClient
from flask import jsonify

import time


def micro_dmp_680_get_data(time_range_begin=None, time_range_end=None):
    if time_range_begin is int and time_range_end is int:  # timestamp is int !
        where_query = "WHERE timestamp > " + str(time_range_begin) + " AND timestamp < " + str(time_range_end)
        result =  microDpm680_DbClient.select_data("*", where_query)
        result = jsonify(result)
        return result

    if time_range_begin is None and time_range_end is None:
        result = microDpm680_DbClient.select_data()
        result = jsonify(result)
        return result

    if time_range_end is None:
        where_query = "WHERE timestamp > " + str(time_range_begin) + " AND timestamp < " + str(round(time.time()))
        result =  microDpm680_DbClient.select_data("*", where_query)
        result = jsonify(result)
        return result

    return jsonify({'error': 'wrong arguments have been given'})

    
