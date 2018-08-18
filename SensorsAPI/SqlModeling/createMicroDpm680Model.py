from sqlalchemy import Column, ForeignKey, Integer, String, Float, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class MicroDpm680CurrentAndVoltageReadings(Base):
    __tablename__ = 'micro_dpm680_voltage_and_currents_readings'

    id = Column(Integer, primary_key=True, nullable=True, autoincrement=True)
    timestamp = Column(BigInteger, nullable=False)
    date = Column(String, nullable=False)

    Us1 = Column(Float, nullable=False)
    Us2 = Column(Float, nullable=False)
    Us3 = Column(Float, nullable=False)

    Ud1 = Column(Float, nullable=False)
    Ud2 = Column(Float, nullable=False)
    Ud3 = Column(Float, nullable=False)

    Up1 = Column(Float, nullable=False)
    Up2 = Column(Float, nullable=False)
    Up3 = Column(Float, nullable=False)

    I1 = Column(Float, nullable=False)
    I2 = Column(Float, nullable=False)
    I3 = Column(Float, nullable=False)
    I4 = Column(Float, nullable=False)

    Ip1 = Column(Float, nullable=False)
    Ip2 = Column(Float, nullable=False)
    Ip3 = Column(Float, nullable=False)
    Ip4 = Column(Float, nullable=False)

    Ic1 = Column(Float, nullable=False)
    Ic2 = Column(Float, nullable=False)
    Ic3 = Column(Float, nullable=False)

    Uc1 = Column(Float, nullable=False)
    Uc2 = Column(Float, nullable=False)
    Uc3 = Column(Float, nullable=False)

    ITh1 = Column(Float, nullable=False)
    ITh2 = Column(Float, nullable=False)
    ITh3 = Column(Float, nullable=False)

    UTh1 = Column(Float, nullable=False)
    UTh2 = Column(Float, nullable=False)
    UTh3 = Column(Float, nullable=False)

    Freq = Column(Float, nullable=False)


class MicroDpm680PowerReadings(Base):
    __tablename__ = 'micro_dpm680_power_readings'

    id = Column(Integer, primary_key=True, nullable=True, autoincrement=True)
    timestamp = Column(BigInteger, nullable=False)
    date = Column(String, nullable=False)

    P1 = Column(Float, nullable=False)
    P2 = Column(Float, nullable=False)
    P3 = Column(Float, nullable=False)
    P4 = Column(Float, nullable=False)

    Q1 = Column(Float, nullable=False)
    Q2 = Column(Float, nullable=False)
    Q3 = Column(Float, nullable=False)
    Q4 = Column(Float, nullable=False)

    S1 = Column(Float, nullable=False)
    S2 = Column(Float, nullable=False)
    S3 = Column(Float, nullable=False)
    S4 = Column(Float, nullable=False)

    Wh1 = Column(Float, nullable=False)
    Wh2 = Column(Float, nullable=False)
    Wh3 = Column(Float, nullable=False)
    Wh4 = Column(Float, nullable=False)

    varh1 = Column(Float, nullable=False)
    varh2 = Column(Float, nullable=False)
    varh3 = Column(Float, nullable=False)
    varh4 = Column(Float, nullable=False)

    Vah1 = Column(Float, nullable=False)
    Vah2 = Column(Float, nullable=False)
    Vah3 = Column(Float, nullable=False)
    Vah4 = Column(Float, nullable=False)

    IWh1 = Column(Float, nullable=False)
    IWh2 = Column(Float, nullable=False)
    IWh3 = Column(Float, nullable=False)

    XWh1 = Column(Float, nullable=False)
    XWh2 = Column(Float, nullable=False)
    XWh3 = Column(Float, nullable=False)

    Ivarh1 = Column(Float, nullable=False)
    Ivarh2 = Column(Float, nullable=False)
    Ivarh3 = Column(Float, nullable=False)

    Xvarh1 = Column(Float, nullable=False)
    Xvarh2 = Column(Float, nullable=False)
    Xvarh3 = Column(Float, nullable=False)

    IVAh1 = Column(Float, nullable-False)
    IVAh2 = Column(Float, nullable-False)
    IVAh3 = Column(Float, nullable-False)

    XVAh1 = Column(Float, nullable-False)
    XVAh2 = Column(Float, nullable-False)
    XVAh3 = Column(Float, nullable-False)

    dpf1 = Column(Float, nullable-False)
    dpf2 = Column(Float, nullable-False)
    dpf3 = Column(Float, nullable-False)

    ddpf1 = Column(Float, nullable-False)
    ddpf2 = Column(Float, nullable-False)
    ddpf3 = Column(Float, nullable-False)

    tpf1 = Column(Float, nullable-False)
    tpf2 = Column(Float, nullable-False)
    tpf3 = Column(Float, nullable-False)
    tpf4 = Column(Float, nullable-False)

    dtpf1 = Column(Float, nullable-False)
    dtpf2 = Column(Float, nullable-False)
    dtpf3 = Column(Float, nullable-False)
    dtpf4 = Column(Float, nullable-False)

    Id1 = Column(Float, nullable-False)
    Id2 = Column(Float, nullable-False)
    Id3 = Column(Float, nullable-False)

    Idp1 = Column(Float, nullable-False)
    Idp2 = Column(Float, nullable-False)
    Idp3 = Column(Float, nullable-False)

    Pd1 = Column(Float, nullable-False)
    Pd2 = Column(Float, nullable-False)
    Pd3 = Column(Float, nullable-False)

    Pdp1 = Column(Float, nullable-False)
    Pdp2 = Column(Float, nullable-False)
    Pdp3 = Column(Float, nullable-False)




db_directory = 'sqlite:///bolidLab_readings.db'
engine = create_engine(db_directory)
 
Base.metadata.create_all(engine)