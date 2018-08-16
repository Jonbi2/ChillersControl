from .createMicroDpm680Model import create_engine
from .createMicroDpm680Model import microDpm680Readings, Base
from .createMicroDpm680Model import db_directory

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

import datetime
import time


class MicroDpm680_DbClient:
    def __init__(self):
        self.engine = create_engine(db_directory)
        Base.metadata.bind = self.engine
        db_session = sessionmaker(bind=self.engine)
        self.session = scoped_session(db_session)

    def push_data(self, params):
        if not isinstance(params, dict):
            raise AttributeError("Wrong argument has been given params argument is not a dictionary")

        date = datetime.datetime.now()
        timestamp = int(round(time.time()))

        us1 = params['Us1']
        us2 = params['Us2']
        us3 = params['Us3']

        ud1 = params['Us1']
        ud2 = params['Ud2']
        ud3 = params['Ud3']

        up1 = params['Up1']
        up2 = params['Up2']
        up3 = params['Up3']

        i1 = params['I1']
        i2 = params['I2']
        i3 = params['I3']
        i4 = params['I4']

        ip1 = params['Ip1']
        ip2 = params['Ip2']
        ip3 = params['Ip3']
        ip4 = params['Ip4']

        ic1 = params['Ip1']
        ic2 = params['Ip2']
        ic3 = params['Ip3']

        uc1 = params['Uc1']
        uc2 = params['Uc2']
        uc3 = params['Uc3']

        iTh1 = params['ITh1']
        iTh2 = params['ITh2']
        iTh3 = params['ITh3']

        uTh1 = params['UTh1']
        uTh2 = params['UTh2']
        uTh3 = params['UTh3']

        freq = params['freq']

        new_data_push = microDpm680Readings(
        date=date,
        timestamp=timestamp,
        Us1=us1,
        Us2=us2,
        Us3=us3, 
        Ud1=ud1, 
        Ud2=ud2, 
        Ud3=ud3, 
        Up1=up1, 
        Up2=up2, 
        Up3=up3, 
        I1=i1, 
        I2=i2, 
        I3=i3, 
        I4=i4, 
        Ip1=ip1, 
        Ip2=ip2, 
        Ip3=ip3, 
        Ip4=ip4,
        Ic1=ic1, 
        Ic2=ic2, 
        Ic3=ic3, 
        Uc1=uc1, 
        Uc2=uc2, 
        Uc3=uc3, 
        ITh1=iTh1, 
        ITh2=iTh2, 
        ITh3=iTh3, 
        UTh1=uTh1, 
        UTh2=uTh2, 
        UTh3=uTh3, 
        Freq=freq)

        self.session.add(new_data_push)
        self.session.commit()
        self.session.close()

    def select_data(self, param=None, where_sql_query=None):
        if param is None:
            param = "*"

        if where_sql_query is None:
            where_sql_query = ""

        result = []
        sql_query = "SELECT " + param + " FROM micro_dpm680_readings " + where_sql_query
        db_result = self.session.execute(sql_query).fetchall()

        for i in range(len(db_result) - 1, -1, -1):
            db_result[i] = list(db_result[i])
            i_json = {}
            i_json['id'] = db_result[i][0]
            i_json['timestamp'] = db_result[i][1]
            i_json['date'] = db_result[i][2]

            i_json['Us1'] = db_result[i][3]
            i_json['Us2'] = db_result[i][4]
            i_json['Us3'] = db_result[i][5]

            i_json['Ud1'] = db_result[i][6]
            i_json['Ud2'] = db_result[i][7]
            i_json['Ud3'] = db_result[i][8]

            i_json['Up1'] = db_result[i][9]
            i_json['Up2'] = db_result[i][10]
            i_json['Up3'] = db_result[i][11]

            i_json['I1'] = db_result[i][12]
            i_json['I2'] = db_result[i][13]
            i_json['I3'] = db_result[i][14]
            i_json['I4'] = db_result[i][15]

            i_json['Ip1'] = db_result[i][16]
            i_json['Ip2'] = db_result[i][17]
            i_json['Ip3'] = db_result[i][18]
            i_json['Ip4'] = db_result[i][19]

            i_json['Ic1'] = db_result[i][20]
            i_json['Ic2'] = db_result[i][21]
            i_json['Ic3'] = db_result[i][22]

            i_json['Uc1'] = db_result[i][23]
            i_json['Uc2'] = db_result[i][24]
            i_json['Uc3'] = db_result[i][25]

            i_json['ITh1'] = db_result[i][26]
            i_json['ITh2'] = db_result[i][27]
            i_json['ITh3'] = db_result[i][28]

            i_json['UTh1'] = db_result[i][29]
            i_json['Uth2'] = db_result[i][30]
            i_json['Uth3'] = db_result[i][31]

            i_json['Freq'] = db_result[i][32]

            result.append(i_json)  

        print(sql_query)
        self.session.commit()
        self.session.close()
        return result
    


microDpm680_DbClient = MicroDpm680_DbClient()



        



