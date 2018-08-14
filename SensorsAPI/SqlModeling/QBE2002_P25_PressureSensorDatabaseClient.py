from .createQBE2002_P25_PressureSensorModel import Base, QBE2002P25Readings
from .createQBE2002_P25_PressureSensorModel import create_engine
from .createQBE2002_P25_PressureSensorModel import db_directory

from sqlalchemy.orm import sessionmaker

import datetime
import time

class QBE2002P25DatabaseClient:
    def __init__(self):
        self.engine = create_engine(db_directory)
        Base.metadata.bind = self.engine
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()

    def push_data(self, params):
        if not isinstance(params, dict):
            raise AttributeError("Wrong argument has been given params argument is not a dictionary")

        _reading = params['reading']
        _sensor_id = params['sensor_id']
        _date = datetime.datetime.now()
        _timestamp = int(round(time.time()))

        new_data_push = QBE2002P25Readings(
            timestamp=_timestamp,
            date=_date,
            sensor_id=_sensor_id,
            reading=_reading
        )

        self.session.add(new_data_push)
        self.session.commit()

    def select_data(self, param=None, where_sql_query=None):
        if param is None:
            param = "*"

        if where_sql_query is None:
            where_sql_query = ""

        result = []
        sql_query = "SELECT " + param + " FROM qbe2002p25_readings " + where_sql_query
        db_result = self.session.execute(sql_query).fetchall()

        for i in range(len(db_result) - 1, -1, -1):
            db_result[i] = list(db_result[i])
            i_json = {}
            i_json['id'] = db_result[i][0]
            i_json['timestamp'] = db_result[i][1]
            i_json['date'] = db_result[i][2]

            i_json['sensor_id'] = db_result[i][3]
            i_json['pressure'] = db_result[i][4]

            result.append(i_json)    
        return result 


qbe2002p25_DbClient = QBE2002P25DatabaseClient()