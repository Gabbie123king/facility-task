import pandas as pd
from database_conn import engine


# Fetch Facility Data Function
def fetchFacilityData():
  query = "SELECT * FROM facilities"
  facilities_df = pd.read_sql(query, engine)
  
  if facilities_df.empty:
    print("The table is empty")
  else:
    print(facilities_df.to_string(index= False))  
    
# Fetch Indicator Data Function    
def fetchIndicators():
   query_indicator = "SELECT * FROM indicators"
   indicators_df = pd.read_sql(query_indicator, engine)
   if indicators_df.empty:
     print("The table is empty")
   else:
     print(indicators_df.to_string(index=False))
     
# Fetch Period Data Function    
def fetchPeriod():
   query_period = "SELECT * FROM periods"
   periods_df = pd.read_sql(query_period, engine)
   if periods_df.empty:
     print("The table is empty")
   else:
     print(periods_df.to_string(index=False))

# Fetch Period Data Function    
def fetchRawData():
   query_rawData = "SELECT * FROM raw_data"
   rawData_df = pd.read_sql(query_rawData, engine)
   if rawData_df.empty:
     print("The table is empty")
   else:
     print(rawData_df.to_string(index=False))
    
# fetchFacilityData()
# fetchIndicators()
# fetchPeriod()
# fetchRawData()