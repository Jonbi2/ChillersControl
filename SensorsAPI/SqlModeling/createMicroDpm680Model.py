from sqlalchemy import Column, ForeignKey, Integer, String, Float, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class microDpm680Readings(Base):
    __tablename__ = 'micro_dpm680_readings'

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


db_directory = 'sqlite:///bolidLab_readings.db'
engine = create_engine(db_directory)
 
Base.metadata.create_all(engine)