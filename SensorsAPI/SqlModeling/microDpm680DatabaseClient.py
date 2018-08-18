from .createMicroDpm680Model import create_engine
from .createMicroDpm680Model import MicroDpm680CurrentAndVoltageReadings,MicroDpm680PowerReadings, Base
from .createMicroDpm680Model import db_directory

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

import datetime
import time


class MicroDpm680VoltageAndCurrentsDbClient:
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

        new_data_push = MicroDpm680CurrentAndVoltageReadings(
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
        sql_query = "SELECT " + param + " FROM micro_dpm680_voltage_and_currents_readings " + where_sql_query
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


#################################################################################################


class MicroDpm680PowerDbClient:
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

        p1 = params['P1']
        p2 = params['P2']
        p3 = params['P3']
        p4 = params['P4']

        q1 = params['Q1']
        q2 = params['Q2']
        q3 = params['Q3']
        q4 = params['Q4']

        s1 = params['S1']
        s2 = params['S2']
        s3 = params['S3']
        s4 = params['S4']

        Wh1 = params['Wh1']
        Wh2 = params['Wh2']
        Wh3 = params['Wh3']
        Wh4 = params['Wh4']

        varh1 = params['varh1']
        varh2 = params['varh2']
        varh3 = params['varh3']
        varh4 = params['varh4']

        Vah1 = params['VAh1']
        Vah2 = params['VAh2']
        Vah3 = params['VAh3']
        Vah4 = params['VAh4']

        IWh1 = params['IWh1']
        IWh2 = params['IWh2']
        IWh3 = params['IWh3']

        XWh1 = params['XWh1']
        XWh2 = params['XWh2']
        XWh3 = params['XWh3']

        Ivarh1 = params['Ivarh1']
        Ivarh2 = params['Ivarh2']
        Ivarh3 = params['Ivarh3']

        Xvarh1 = params['Xvarh1']
        Xvarh2 = params['Xvarh2']
        Xvarh3 = params['Xvarh3']

        IVah1 = params['IVAh1']
        IVah2 = params['IVAh2']
        IVah3 = params['IVAh3']

        XVah1 = params['XVAh1']
        XVah2 = params['XVAh2']
        XVah3 = params['XVAh3']

        dpf1 = params['dpf1']
        dpf2 = params['dpf2']
        dpf3 = params['dpf3']

        ddpf1 = params['ddpf1']
        ddpf2 = params['ddpf2']
        ddpf3 = params['ddpf3']

        tpf1 = params['tpf1']
        tpf2 = params['tpf2']
        tpf3 = params['tpf3']
        tpf4 = params['tpf4']

        dtpf1 = params['dtpf1']
        dtpf2 = params['dtpf2']
        dtpf3 = params['dtpf3']
        dtpf4 = params['dtpf4']

        Id1 = params['Id1']
        Id2 = params['Id2']
        Id3 = params['Id3']

        Idp1 = params['Idp1']
        Idp2 = params['Idp2']
        Idp3 = params['Idp3']

        Pd1 = params['Pd1']
        Pd2 = params['Pd2']
        Pd3 = params['Pd3']

        Pdp1 = params['Pdp1']
        Pdp2 = params['Pdp2']
        Pdp3 = params['Pdp3']

        new_data_push = MicroDpm680VoltageAndCurrentsDbClient(
        date=date,
        timestamp=timestamp,
        p1=p1,
        p2=p2,
        p3=p3,
        p4=p4,

        q1=q1,
        q2=q2,
        q3=q3,
        q4=q4,

        s1=s1,
        s2=s2,
        s3=s3,
        s4=s4,

        Wh1=Wh1,
        Wh2=Wh2,
        Wh3=Wh3,
        Wh4=Wh4,

        varh1=varh1,
        varh2=varh2,
        varh3=varh3,
        varh4=varh4,

        Vah1=Vah1,
        Vah2=Vah2,
        Vah3=Vah3,
        Vah4=Vah4,

        IWh1=IWh1,
        IWh2=IWh2,
        IWh3=IWh3,

        XWh1=XWh1,
        XWh2=XWh2,
        XWh3=XWh3,

        Ivarh1=Ivarh1,
        Ivarh2=Ivarh2,
        Ivarh3=Ivarh3,

        Xvarh1= Xvarh1,
        Xvarh2=Xvarh2,
        Xvarh3=Xvarh3,

        IVah1=IVah1,
        IVah2=IVah2,
        IVah3=IVah3,

        XVah1=XVah1,
        XVah2=XVah2,
        XVah3=XVah3,

        dpf1=dpf1,
        dpf2=dpf2,
        dpf3=dpf3,

        ddpf1= ddpf1,
        ddpf2=ddpf2,
        ddpf3=ddpf3,

        tpf1=tpf1,
        tpf2=tpf2,
        tpf3=tpf3,
        tpf4=tpf4,

        dtpf1=dtpf1,
        dtpf2=dtpf2,
        dtpf3=dtpf3,
        dtpf4=dtpf4,

        Id1=Id1,
        Id2=Id2,
        Id3=Id3,

        Idp1=Ipd1,
        Idp2=Idp2,
        Idp3=Idp3,

        Pd1=Pd1,
        Pd2=Pd2,
        Pd3=Pd3,

        Pdp1=Pdp1,
        Pdp2=Pdp2,
        Pdp3=Pdp3)


        self.session.add(new_data_push)
        self.session.commit()
        self.session.close()

    def select_data(self, param=None, where_sql_query=None):
        if param is None:
            param = "*"

        if where_sql_query is None:
            where_sql_query = ""

        result = []
        sql_query = "SELECT " + param + " FROM micro_dpm680_voltage_and_currents_readings " + where_sql_query
        db_result = self.session.execute(sql_query).fetchall()

        for i in range(len(db_result) - 1, -1, -1):
            db_result[i] = list(db_result[i])
            i_json = {}
            i_json['id'] = db_result[i][0]
            i_json['timestamp'] = db_result[i][1]
            i_json['date'] = db_result[i][2]

            i_json['P1'] = db_result[i][3]
            i_json['P2'] = db_result[i][4]
            i_json['P3'] = db_result[i][5]

            i_json['P4'] = db_result[i][6]
            i_json['Q1'] = db_result[i][7]
            i_json['Q2'] = db_result[i][8]

            i_json['Q3'] = db_result[i][9]
            i_json['Q4'] = db_result[i][10]
            i_json['S1'] = db_result[i][11]

            i_json['S2'] = db_result[i][12]
            i_json['S3'] = db_result[i][13]
            i_json['S4'] = db_result[i][14]
            i_json['Wh1'] = db_result[i][15]

            i_json['Wh2'] = db_result[i][16]
            i_json['Wh3'] = db_result[i][17]
            i_json['Wh4'] = db_result[i][18]
            i_json['varh1'] = db_result[i][19]

            i_json['varh2'] = db_result[i][20]
            i_json['varh3'] = db_result[i][21]
            i_json['varh4'] = db_result[i][22]

            i_json['Vah1'] = db_result[i][23]
            i_json['Vah2'] = db_result[i][24]
            i_json['Vah3'] = db_result[i][25]

            i_json['Vah4'] = db_result[i][26]
            i_json['IWh1'] = db_result[i][27]
            i_json['IWh2'] = db_result[i][28]

            i_json['IWh3'] = db_result[i][29]
            i_json['xWh1'] = db_result[i][30]
            i_json['xWh2'] = db_result[i][31]

            i_json['xWh3'] = db_result[i][32]
            i_json['Ivarh1'] = db_result[i][33]
            i_json['Ivarh2'] = db_result[i][34]

            i_json['Ivarh3'] = db_result[i][35]
            i_json['Xvarh1'] = db_result[i][36]
            i_json['Xvarh2'] = db_result[i][37]

            i_json['Xvarh3'] = db_result[i][38]
            i_json['IVah1'] = db_result[i][39]
            i_json['IVah2'] = db_result[i][40]

            i_json['IVah3'] = db_result[i][41]
            i_json['XVah1'] = db_result[i][42]
            i_json['XVah2'] = db_result[i][43]

            i_json['XVah3'] = db_result[i][44]
            i_json['dpf1'] = db_result[i][45]
            i_json['dpf2'] = db_result[i][46]

            i_json['dpf3'] = db_result[i][47]
            i_json['ddpf1'] = db_result[i][48]
            i_json['ddpf2'] = db_result[i][49]

            i_json['ddpf3'] = db_result[i][50]
            i_json['tpf1'] = db_result[i][51]
            i_json['tpf2'] = db_result[i][52]

            i_json['tpf3'] = db_result[i][53]
            i_json['tpf4'] = db_result[i][54]
            i_json['dtpf1'] = db_result[i][55]
            
            i_json['dtpf2'] = db_result[i][56]
            i_json['dtpf3'] = db_result[i][57]
            i_json['dtpf4'] = db_result[i][58]
            
            i_json['Idp1'] = db_result[i][59]
            i_json['Idp2'] = db_result[i][60]
            i_json['Idp3'] = db_result[i][61]

            i_json['Pd1'] = db_result[i][62]
            i_json['Pd2'] = db_result[i][63]
            i_json['Pd3'] = db_result[i][64]

            i_json['Pdp1'] = db_result[i][65]
            i_json['Pdp2'] = db_result[i][66]
            i_json['Pdp3'] = db_result[i][67]

            result.append(i_json)  

        print(sql_query)
        self.session.commit()
        self.session.close()
        return result
    


microDpm680_voltage_and_currents_DbClient = MicroDpm680VoltageAndCurrentsDbClient()
microDpm680_powers_DbClient = MicroDpm680PowerDbClient()



        



