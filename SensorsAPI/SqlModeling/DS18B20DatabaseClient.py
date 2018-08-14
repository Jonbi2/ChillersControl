from .createDS18B20Model import Base, DS18B20Readings
from .createDS18B20Model import create_engine
from .createDS18B20Model import db_directory

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

import datetime
import time


class DS18B20DatabaseClient:
    def __init__(self):
        self.engine = create_engine(db_directory)
        Base.metadata.bind = self.engine
        self.DBSession = sessionmaker(bind=self.engine)
        self.session = scoped_session(self.DBSession)

    def push_data(self, params):
        if not isinstance(params, list):
            raise AttributeError("Wrong argument has been given params argument is not a list")

        push_session = self.DBSession()

        for reading in params:

            _reading = reading['reading']
            _sensor_id = reading['sensor_id']
            _date = datetime.datetime.now()
            _timestamp = int(round(time.time()))

            new_data_push = DS18B20Readings(
                timestamp=_timestamp,
                date=_date,
                sensor_id=_sensor_id,
                reading=_reading
            )

            self.session.add(new_data_push)
            self.session.commit()
            self.session.close()

    def select_data(self, param=None, where_sql_query=None, additional_list=None):
        if param is None:
            param = "*"

        if where_sql_query is None:
            where_sql_query = ""

        result = []
        sql_query = "SELECT " + param + " FROM ds18b20_readings " + where_sql_query

        db_result = self.session.execute(sql_query, additional_list).fetchall()

        for i in range(len(db_result) - 1, -1, -1):
            db_result[i] = list(db_result[i])
            i_json = {}
            i_json['id'] = db_result[i][0]
            i_json['timestamp'] = db_result[i][1]
            i_json['date'] = db_result[i][2]

            i_json['sensor_id'] = db_result[i][3]
            i_json['temperature'] = db_result[i][4]

            result.append(i_json)    

        print(sql_query)
        return result

    def select_distinct(self, column_name):
        sql_query = "SELECT DISTINCT " + column_name + " FROM ds18b20_readings"
        db_result = self.session.execute(sql_query).fetchall()
        for i in range(len(db_result) - 1, -1, -1):
            db_result[i] = list(db_result[i])[i]
            db_result[i] = ''.join(db_result[i])
        return db_result
ds18b20_DbClient = DS18B20DatabaseClient()

