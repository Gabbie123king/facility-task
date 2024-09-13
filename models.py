from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Faclity Table
class Facility(Base):
    __tablename__ = 'facilities'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    dhis2_code = Column(Integer, unique=True)

# Indicators table
class Indicator(Base):
    __tablename__ = 'indicators'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    dhis2_code = Column(Integer, unique=True)

# Periods table
class Period(Base):
    __tablename__ = 'periods'
    id = Column(Integer, primary_key=True)
    period_code = Column(String)

# Define the Raw Data table
class RawData(Base):
    __tablename__ = 'raw_data'
    id = Column(Integer, primary_key=True)
    dhis2_code_indicator = Column(Integer, ForeignKey('indicators.dhis2_code'))
    dhis2_code_facility = Column(Integer, ForeignKey('facilities.dhis2_code'))
    value = Column(Float)
    period = Column(String)