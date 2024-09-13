# insert_data.py
from database_conn import session
from models import Facility, Indicator, Period, RawData

# Insert data into Facilities
facilities_data = [
    Facility(id=1, name="St. Mary", dhis2_code=3),
    Facility(id=2, name="St. Annes", dhis2_code=7),
    Facility(id=3, name="St. Peter", dhis2_code=2)
]

# Insert data into Indicators
indicators_data = [
    Indicator(id=1, name="Immunization", dhis2_code=101),
    Indicator(id=2, name="Malaria Treatment", dhis2_code=102),
    Indicator(id=3, name="HIV Testing", dhis2_code=103)
]

# Insert data into Periods
periods_data = [
    Period(id=1, period_code="202401"),
    Period(id=2, period_code="202402"),
    Period(id=3, period_code="202403")
]

# Insert data into Raw Data
raw_data_entries = [
    RawData(dhis2_code_indicator=101, dhis2_code_facility=3, value=150, period="202401"),
    RawData(dhis2_code_indicator=102, dhis2_code_facility=7, value=200, period="202402"),
    RawData(dhis2_code_indicator=103, dhis2_code_facility=2, value=100, period="202403"),
    RawData(dhis2_code_indicator=101, dhis2_code_facility=3, value=180, period="202401"),
    RawData(dhis2_code_indicator=102, dhis2_code_facility=7, value=220, period="202402"),
    RawData(dhis2_code_indicator=103, dhis2_code_facility=2, value=130, period="202403")
]

# Add all data to the session
session.add_all(facilities_data + indicators_data + periods_data + raw_data_entries)

# Commit the transaction to the database
session.commit()
