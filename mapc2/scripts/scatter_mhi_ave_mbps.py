# This script generates a scatter plot for MBPS against median household income.
# 
# Author: Nathan Lauer, Adam Streich
# Please feel free to ask me any questions, I hope you're having a nice day!

import pandas as pd 
import matplotlib.pyplot as plt
import argparse
import mpld3
import numpy as np

# Returns 1 if the city is in MAPC list, 0 otherwise
def city_in_mapc(city, mapc_list):
  if city in mapc_list:
    return 1
  return 0

#################### Main Control Flow
parser = argparse.ArgumentParser(description='Scatter of MBPS against MHI')
parser.add_argument('--mhi-file', dest="mhi_file", help="Census file")
parser.add_argument('--mlab-file', dest="mlab_file", help="MLAB data")
parser.add_argument('--mapc-file', dest="mapc_file", help="MAPC municipalities file")
args = parser.parse_args()

# Read input files
df_mhi = pd.read_csv(args.mhi_file)
df_mlab = pd.read_csv(args.mlab_file)
mapc_cities = pd.read_csv(args.mapc_file)['municipal'].to_list()

# First, compute average MBPS per city in mlab data
mlab_avg_mbps = df_mlab.groupby(['City']).mean().drop(columns=['MinRTT', 'Latitude'  ,'Longitude' ,'ProviderNumber'])

# Rename 'municipal' in MHI file to City
df_mhi['City'] = df_mhi['municipal']

# Join mlab_avg_mbps and df_mhi
joined = pd.merge(df_mhi, mlab_avg_mbps, on="City")
joined = joined[['mhi', 'City', 'MeanThroughputMbps']]
# Note: the join "auto-removed" any cities that did not appear in both data sets.
# It would be interesting to have a list of these.

# Add a new column that indicates if the city is in MAPC munis, and build a color array from it
joined['InMapc'] = joined.apply(lambda row: city_in_mapc(row['City'], mapc_cities), axis=1)
out_color = '#7d7975'
in_color = '#eba134'
colors = np.array([in_color if city == 1 else out_color for city in joined['InMapc']])

# Plot City against mhi
fig, ax = plt.subplots(figsize=(15,10))
x = joined['mhi']
y = joined['MeanThroughputMbps']
scatter = ax.scatter(x, y, alpha=0.9, c=colors)

# Label each data point with the associated city
labels = joined['City'].to_list()
tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=labels)
mpld3.plugins.connect(fig, tooltip)

# Set labels
ax.set_xlabel("Median Household Income, 2014-2018, Dollars", size=20)
ax.set_ylabel("Mean Throughput Mbps, MLAB 2020 data", size=20)
ax.set_title("MLAB: Average Broadband Speed against Median Household Income", size=30)
xvalues = np.arange(40000,240000, 20000)
yvalues = np.arange(0, 400, 50)
ax.set_xticklabels(xvalues, fontsize=16)
ax.set_yticklabels(yvalues, fontsize=16)
# ax.legend()

# Configure colors
ax.set_facecolor('#EEEEEE')
ax.grid(linestyle='--', linewidth=0.5, alpha=0.3)

# Add a trendline
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
ax.plot(x,p(x),"r--", label='All')

# Add trendlines for each of the two categories of municipalities
in_mapc_data = joined[joined['InMapc'] == 1]
out_mapc_data = joined[joined['InMapc'] != 1]
# In MAPC trendline
x_in = in_mapc_data['mhi']
y_in = in_mapc_data['MeanThroughputMbps']
z_in = np.polyfit(x_in, y_in, 1)
p_in = np.poly1d(z_in)
ax.plot(x_in,p_in(x_in),"--", c=in_color, label='MAPC Tracked Municipalities')
# Not in MAPC trendline
x_out = out_mapc_data['mhi']
y_out = out_mapc_data['MeanThroughputMbps']
z_out = np.polyfit(x_out, y_out, 1)
p_out = np.poly1d(z_out)
ax.plot(x_out,p_out(x_out),"--", c=out_color, label='Non-Tracked Municipalities')

# Finally, show the plot
ax.legend()
# mpld3.show()

mpld3.save_html(fig, "output/mlab_mhi_vs_mbps_2020.html")

# Some ideas:
# - Produce second plot, with data points that are above 150 MBPS removed
# - Trend lines for each category of municipalities