# This script queries the MLAB data on Google BigQuery at specific times, 
# throughout a year. It then outputs the results to an output file

from google.cloud import bigquery
import pandas as pd
from datetime import date

"""
Executes a query against the MLAB data on BigQuery, and 
returns the results. Specifically, we limit the results
to a certain timeframe, which is specified by the passed in 
parameters

Attributes:
year - relevant year, e.g. 2020
month_num - relevant month, e.g. 1 (numeric)
day_num - relevant day of the monet, e.g. 27 (numeric)
start_hour - the starting hour for the query, e.g. 8
start_minute - the starting minute for the query, e.g. 0 (with the above, this would start at 8:00am)
end_hour - the ending hour for the query, e.g 8
end_minute - the ending minute for the query, e.g 10 (with the above, this would end at 8:10am)

Note: it is assumed that these times are given as EST/EDT. BigQuery stores results as UTC, and 
therefore we need to specify EST or EDT in the query. This function handles that conversion
internally.
"""
def query_mlab(year, month_num, day_num, start_hour, start_minute, end_hour, end_minute):
  # The first step is to determine how many hours to add. We basically 
  # just assume that March through October are in daylight sayings, so its UTC -4
  plus_hours = 5
  if month_num >= 3 and month_num <= 10:
    plus_hours = 4 

  start_hour += plus_hours
  end_hour += plus_hours

  # Construct the text of the query
  query_text = """
    SELECT
      a.TestTime AS TestTime,
      NET.SAFE_IP_FROM_STRING (client.IP) AS IP,
      a.MeanThroughputMbps AS MeanThroughputMbps,
      a.MinRTT AS MinRTT,
      client.Geo.city AS City,
      client.Geo.Latitude AS Latitude,
      client.Geo.Longitude AS Longitude,
      client.Network.ASNumber AS ProviderNumber,
    FROM
      `measurement-lab.ndt.unified_uploads`
    WHERE
      client.geo.CountryCode = "US"
      AND client.Geo.region = "MA"
      AND date BETWEEN "{year}-{month_num}-{day_num}"
      AND "{year}-{month_num}-{day_num}"
      AND a.TestTime BETWEEN TIMESTAMP("{year}-{month_num}-{day_num} {start_hour}:{start_minute}:00.000", "UTC")
      AND TIMESTAMP("{year}-{month_num}-{day_num} {end_hour}:{end_minute}:00.000", "UTC")
    """.format(year=year, month_num=month_num, day_num=day_num, start_hour=start_hour, start_minute=start_minute, end_hour=end_hour, end_minute=end_minute)


  # Execute the query. This will return a list of BigQuery Rows
  client = bigquery.Client()
  query_job = client.query(query_text)
  big_query_results = query_job.result()

  # Process the results into a more useful format
 

  rows = []
  for big_query_row in big_query_results:
    row = []
    row.append(str(big_query_row.get('TestTime'))) # The test time is returned as a DateTime object
    row.append(big_query_row.get('IP')) # TODO: this comes in as a weird byte string, which I'm having trouble decoding
    row.append(big_query_row.get('MeanThroughputMbps'))
    row.append(big_query_row.get('MinRTT'))
    row.append(big_query_row.get('City'))
    row.append(big_query_row.get('Latitude'))
    row.append(big_query_row.get('Longitude'))
    row.append(big_query_row.get('ProviderNumber'))

    # Add this row
    rows.append(row)

  column_names = ['TestTime', 'IP', 'MeanThroughputMbps', 'MinRTT', 'City', 'Latitude', 'Longitude', 'ProviderNumber']
  return pd.DataFrame(rows, columns=column_names)

############## Main execution flow

# Set up dates
year = 2020
start_date = date.fromisoformat('2020-03-18')
end_date = date.fromisoformat('2020-12-31')

# And time
start_hour = 8
start_minute = 0
end_hour = 8
end_minute = 30

for index, single_date in enumerate(pd.date_range(start_date, end_date)):
  print("Working on month: {}, day: {}".format(single_date.month, single_date.day))
  print("----------------------------------------")
  results = query_mlab(year, single_date.month, single_date.day, start_hour, start_minute, end_hour, end_minute)
  # Had to rerun, commented out to modify
  # if index == 0:
  #   results.to_csv("data/mlab_2020_8_to_830_am.csv", index=False, index_label=False)
  # else:
  results.to_csv("data/mlab_2020_8_to_830_am.csv", index=False, index_label=False, mode='a', header=False)

# results = query_mlab(2020, 10, 1, 8, 0, 8, 30)


# SELECT
#   a.TestTime AS TestTime,
#   NET.SAFE_IP_FROM_STRING (client.IP) AS ip,
#   a.MeanThroughputMbps AS MeanThroughputMbps,
#   a.MinRTT AS MinRTT,
#   client.Geo.city AS City,
#   client.Geo.Latitude AS Latitude,
#   client.Geo.Longitude AS Longitude,
#   client.Network.ASNumber AS ProviderNumber,
#   client.Network.ASName AS ProviderName
# FROM
#   `measurement-lab.ndt.unified_uploads`
# WHERE
#   client.geo.CountryCode = "US"
#   AND client.Geo.region = "MA"
#   AND date BETWEEN "2020-10-01"
#   AND "2020-10-01"
#   AND (
#     (
#       a.TestTime BETWEEN TIMESTAMP("2020-10-01 00:00:00.000", "UTC")
#       AND TIMESTAMP("2020-10-01 00:30:00.000", "UTC")
#     )
#     OR (
#       a.TestTime BETWEEN TIMESTAMP("2020-10-01 12:00:00.000", "UTC")
#       AND TIMESTAMP("2020-10-01 12:30:00.000", "UTC")
#     )
#     OR (
#       a.TestTime BETWEEN TIMESTAMP("2020-10-01 16:00:00.000", "UTC")
#       AND TIMESTAMP("2020-10-01 16:30:00.000", "UTC")
#     )
#     OR (
#       a.TestTime BETWEEN TIMESTAMP("2020-10-01 19:30:00.000", "UTC")
#       AND TIMESTAMP("2020-10-01 20:00:00.000", "UTC")
#     )
#   )