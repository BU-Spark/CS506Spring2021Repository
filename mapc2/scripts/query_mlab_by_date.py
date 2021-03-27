# This script queries the MLAB data on Google BigQuery at specific times, 
# throughout a year. It then outputs the results to an output file

from google.cloud import bigquery
import pandas as pd
from datetime import date
import argparse

"""
Executes a query against the MLAB data on BigQuery, and 
returns the results. Specifically, we limit the results
to a certain timeframe, which is specified by the passed in 
parameters

We grab results from 4 different times throughout the day:
8:00am - 8:30am
12:00pm - 12:30pm
3:30pm - 4:00pm
8:00pm - 8:30pm

These times are considered representative throughout the day.

Attributes:
year - relevant year, e.g. 2020
month_num - relevant month, e.g. 1 (numeric)
day_num - relevant day of the monet, e.g. 27 (numeric)

Note: this function internally handles daylight savings time, but only roughly.
"""
def query_mlab(year, month_num, day_num):
  # This is a rough estimate for daylight savings
  # These are when we are not in daylight savings, and EST is UTC -5
  first_hour = "01"
  second_hour = "13"
  third_hour = "17"
  fourth_hour = "20"
  fifth_hour = "21"

  if month_num >= 3 and month_num <= 10:
    # These are when we are in daylight savings, and EDT is UTC -4
    first_hour = "00"
    second_hour = "12"
    third_hour = "16"
    fourth_hour = "19"
    fifth_hour = "20"

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
      AND (
        (
          a.TestTime BETWEEN TIMESTAMP("{year}-{month_num}-{day_num} {first_hour}:00:00.000", "UTC")
          AND TIMESTAMP("{year}-{month_num}-{day_num} {first_hour}:30:00.000", "UTC")
        )
        OR (
          a.TestTime BETWEEN TIMESTAMP("{year}-{month_num}-{day_num} {second_hour}:00:00.000", "UTC")
          AND TIMESTAMP("{year}-{month_num}-{day_num} {second_hour}:30:00.000", "UTC")
        )
        OR (
          a.TestTime BETWEEN TIMESTAMP("{year}-{month_num}-{day_num} {third_hour}:00:00.000", "UTC")
          AND TIMESTAMP("{year}-{month_num}-{day_num} {third_hour}:30:00.000", "UTC")
        )
        OR (
          a.TestTime BETWEEN TIMESTAMP("{year}-{month_num}-{day_num} {fourth_hour}:30:00.000", "UTC")
          AND TIMESTAMP("{year}-{month_num}-{day_num} {fifth_hour}:00:00.000", "UTC")
        )
      )
    """.format(year=year, month_num=month_num, day_num=day_num, first_hour=first_hour, second_hour=second_hour, third_hour=third_hour, fourth_hour=fourth_hour, fifth_hour=fifth_hour)
    
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
start_date = date.fromisoformat('2020-01-01')
end_date = date.fromisoformat('2020-12-31')

parser = argparse.ArgumentParser(description='Pass dates to query mlab')
parser.add_argument('--start_date', dest="start_date")
parser.add_argument('--end_date', dest='end_date')

args = parser.parse_args()
if args.start_date:
  start_date = args.start_date

if args.end_date:
  end_date = args.end_date

outfile = "data/mlab_{}_to_{}.csv".format(start_date, end_date)

for index, single_date in enumerate(pd.date_range(start_date, end_date)):
  print("Working on month: {}, day: {}".format(single_date.month, single_date.day))
  print("----------------------------------------")
  results = query_mlab(year, single_date.month, single_date.day)
  
  if index == 0:
    results.to_csv(outfile, index=False, index_label=False)
  else:
    results.to_csv(outfile, index=False, index_label=False, mode='a', header=False)


