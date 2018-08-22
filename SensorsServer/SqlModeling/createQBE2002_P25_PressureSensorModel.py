from sqlalchemy import Column, ForeignKey, Integer, String, Float, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class QBE2002P25Readings(Base):
    __tablename__ = 'qbe2002p25_readings'

    id = Column(Integer, primary_key=True, nullable=True, autoincrement=True)
    timestamp = Column(BigInteger, nullable=False)
    date = Column(String, nullable=False)

    sensor_id = Column(String, nullable=True)

    reading = Column(Float, nullable=False)


db_directory = 'sqlite:///bolidLab_readings.db'
engine = create_engine(db_directory)
 
Base.metadata.create_all(engine)