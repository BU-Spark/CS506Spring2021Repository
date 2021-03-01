import pandas as pd 
import sqlite3
from sqlalchemy import create_engine

def readData(filename):
    data = pd.read_csv(filename)
    return data

def insertDataToDB(tablename, df,conn):
    df.to_sql(tablename,conn, if_exists="replace")

#connect to database cs506MAPC.db
conn = sqlite3.connect('cs506MAPC.db')

#uncomment if never created before
# df = readData("fcc_data_june2019.csv")
# insertDataToDB("fcc_data_t",df,conn)


qrystr ="SELECT DISTINCT ProviderName,substr(BlockCode,0,12) as tractNum,MaxAdDown,MaxAdUp FROM FCC_DATA_T ORDER BY substr(BlockCode,0,12) ASC"

# normal query execution
#cursor = conn.execute(qrystr)
# for row in cursor:
#     print(row)

#convert query results into dataframe
df_filtered = pd.read_sql_query(qrystr, conn)
print(df_filtered.head(10))




df = readData("median_income.csv")
print(df.head(10))
df_filtered = df[['ct10_id','mhi','mhi_me','o_mhi','o_mhi_me','r_mhi','r_mhi_me']]
insertDataToDB("median_income_t",df_filtered,conn)


#todo: filter data from fcc data which has 0 max_ad_up and max_ad_down
#this means company doesnt supply that area. 