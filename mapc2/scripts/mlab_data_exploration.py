# In this script, we explore the MLAB data, and compute various interesting 
# statistics over the entire data set.
# 
# Author: Nathan Lauer
# Please feel free to ask me any questions, I hope you're having a nice day!

import pandas as pd
import argparse

########## Main execution flow
parser = argparse.ArgumentParser(description='Map AS Numbers to Provider Name')
parser.add_argument('--mlab-data', dest='mlab_data', help='The input MLAB data csv file')
args = parser.parse_args()

pd.set_option('display.max_rows', 500)

# Read the MLAB data
df = pd.read_csv(args.mlab_data)

# Round the average speeds
df = df.round({'MeanThroughputMbps': 1})
df = df.round({'MinRTT': 1})

# Overall basic statistics
overall_ave = round(df.MeanThroughputMbps.mean(), 1)
overall_median = df.MeanThroughputMbps.median()
overall_mode = df.MeanThroughputMbps.mode()
overall_stddev = round(df.MeanThroughputMbps.std(), 2)
print("Basic Statistics")
print("-------------")
print("average MeanThroughputMbps: {}".format(overall_ave))
print("median MeanThroughputMbps: {}".format(overall_median))
print("mode MeanThroughputMbps: {}".format(overall_mode))
print("Std Dev MeanThroughputMbps: {}".format(overall_stddev))
print()

# Fastest and slowest providers
print("Fastest and Slowest Providers, with at least 50 measurements")
print("-------------")
agg_mean_and_count = df[['ProviderName', 'MeanThroughputMbps']].groupby(['ProviderName']).agg(['mean', 'count'])
select_at_least_x = agg_mean_and_count.loc[agg_mean_and_count[('MeanThroughputMbps', 'count')] > 50]
fastest_providers = pd.Series(data=select_at_least_x[('MeanThroughputMbps', 'mean')]).nlargest(5)
slowest_providers = pd.Series(data=select_at_least_x[('MeanThroughputMbps', 'mean')]).nsmallest(5)
print("Top 5 fastest providers on average")
print("-------------")
print(fastest_providers)
print()
print("Botton 5 slowest providers on average")
print("-------------")
print(slowest_providers)
print()

# Repeat, but now with a minimum of 10000 measurements
print("Fastest and Slowest Providers, with at least 1,000 measurements")
print("-------------")
agg_mean_and_count = df[['ProviderName', 'MeanThroughputMbps']].groupby(['ProviderName']).agg(['mean', 'count'])
select_at_least_x = agg_mean_and_count.loc[agg_mean_and_count[('MeanThroughputMbps', 'count')] > 1000]
fastest_providers = pd.Series(data=select_at_least_x[('MeanThroughputMbps', 'mean')]).nlargest(5)
slowest_providers = pd.Series(data=select_at_least_x[('MeanThroughputMbps', 'mean')]).nsmallest(5)
print("Top 5 fastest providers on average")
print("-------------")
print(fastest_providers)
print()
print("Botton 5 slowest providers on average")
print("-------------")
print(slowest_providers)
print()

# Find the 25 fastest and slowest speeds
fastest_speeds = pd.Series(data=df.MeanThroughputMbps).nlargest(25)
print("Top 25 fastest measured speeds")
print("-------------")
print(fastest_speeds)
print()
slowest_speeds = pd.Series(data=df.MeanThroughputMbps).nsmallest(25)
print("Bottom 25 slowest measured speeds")
print("-------------")
print(slowest_speeds)
print()


# Count the number of measurements for each Provider
provider_count = df[['ProviderName', 'MeanThroughputMbps']].groupby(['ProviderName']).count()
print("Count of measurements per Provider")
print("-------------")
print(provider_count.rename(columns={"MeanThroughputMbps": "Count"}).sort_values(by=['Count'], ascending=False))
print()

# Number of measurements in each city
city_count = df[['City', 'MeanThroughputMbps']].groupby(['City']).count()
print("Count of measurements per City")
print("-------------")
print(city_count.rename(columns={"MeanThroughputMbps": "Count"}).sort_values(by=['Count'], ascending=False))
print()
