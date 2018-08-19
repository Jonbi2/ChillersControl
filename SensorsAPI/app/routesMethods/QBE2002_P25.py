from SqlModeling.QBE2002_P25_PressureSensorDatabaseClient import qbe2002p25_DbClient

from flask import jsonify, send_file

import csv
import io

import time


def qbe2002_p25_get_data(device_id=None ,time_range_begin=None, time_range_end=None, is_result_csv=None):

    if time_range_begin is None and time_range_end is None and device_id is None:
            result = qbe2002p25_DbClient.select_data()

    elif time_range_begin is None and time_range_end is None:
        result = qbe2002p25_DbClient.select_data("*", "WHERE sensor_id = " + str(device_id))

    elif time_range_begin is int and time_range_end is int:  # timestamp is int !
        where_query = "WHERE timestamp > " + str(time_range_begin) + " AND timestamp < " + str(time_range_end) + " AND sensor_id = " + "'" +str(device_id) + "'"
        result =  qbe2002p25_DbClient.select_data("*", where_query)

    elif time_range_end is None:
        where_query = "WHERE timestamp > " + str(time_range_begin) + " AND timestamp < " + str(round(time.time())) + " AND sensor_id = " + str(device_id)
        result =  qbe2002p25_DbClient.select_data("*", where_query)

    else:
        return jsonify({'error': 'wrong arguments have been given'})

    if is_result_csv is not True:
        result = jsonify(result)

    else:
        rows_list = []
        for json in result:
            rows_list.append(list(json.values()))

        proxy = io.StringIO()

        writer = csv.writer(proxy)
        for row in rows_list:
            writer.writerow(row)

        mem = io.BytesIO()
        mem.write(proxy.getvalue().encode('utf-8'))
        mem.seek(0)
        proxy.close()

        result = send_file(
            mem,
            as_attachment=True,
            attachment_filename='QBE2002_P25.csv',
            mimetype='text/csv'
        )

    return result


    
