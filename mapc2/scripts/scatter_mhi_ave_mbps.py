# This script generates a scatter plot for MBPS against median household income.
# 
# Author: Nathan Lauer, Adam Streich
# Please feel free to ask me any questions, I hope you're having a nice day!

import pandas as pd 
import matplotlib.pyplot as plt
import argparse
import mpld3
import numpy as np

#################### Main Control Flow
parser = argparse.ArgumentParser(description='Scatter of MBPS against MHI')
parser.add_argument('--mhi-file', dest="mhi_file", help="Census file")
parser.add_argument('--mlab-file', dest="mlab_file", help="MLAB data")
args = parser.parse_args()

# Read input files
df_mhi = pd.read_csv(args.mhi_file)
df_mlab = pd.read_csv(args.mlab_file)

# First, compute average MBPS per city in mlab data
mlab_avg_mbps = df_mlab.groupby(['City']).mean().drop(columns=['MinRTT', 'Latitude'  ,'Longitude' ,'ProviderNumber'])

# Rename 'municipal' in MHI file to City
df_mhi['City'] = df_mhi['municipal']

# Join mlab_avg_mbps and df_mhi
joined = pd.merge(df_mhi, mlab_avg_mbps, on="City")
joined = joined[['mhi', 'City', 'MeanThroughputMbps']]
# Note: the join "auto-removed" any cities that did not appear in both data sets.
# It would be interesting to have a list of these.

# Plot City against mhi
fig, ax = plt.subplots(figsize=(15,10)) # Grey background
scatter = ax.scatter(joined['mhi'], joined['MeanThroughputMbps'], alpha=0.9)

# Label each data point with the associated city
labels = joined['City'].to_list()
tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=labels)
mpld3.plugins.connect(fig, tooltip)

# Set labels
ax.set_xlabel("Median Household Income, 2014-2018, Dollars", size=20)
ax.set_ylabel("Mean Throughput Mbps, MLAB 2020 data", size=20)
ax.set_title("Average Broadband Speed against Median Household Income", size=30)
xvalues = np.arange(40000,240000, 20000)
yvalues = np.arange(0, 400, 50)
ax.set_xticklabels(xvalues, fontsize=16)
ax.set_yticklabels(yvalues, fontsize=16)

# Configure colors
ax.set_facecolor('#EEEEEE')
ax.grid(color='w', linestyle='--', linewidth=0.5)

# Finally, show the plot
mpld3.show()