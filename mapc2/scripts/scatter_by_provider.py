# This script calls the MhiMbpsSCatter class for each relevant provider
# 
# author: Nathan Lauer, Jenny Li, 
# Please feel free to ask me any questions, I hope you're having a nice day!

import pandas as pd
from .scatter_mhi_ave_mbps import MhiMbpsScatter

# Given a provider, call the scatter class with appropriate args
def scatter_for_provider(df_mlab, provider_name):
  # TODO: filter df_mlab by provider
  df_provider = df_mlab[df_mlab.ProviderName == provider_name]

  speed_col = "MeanThroughputMbps"
  output = "../output/mlab_by_provider_{}_2020.html".format(provider_name)
  title = "MLAB {}: Mean Throughput Broadband Speed against Median Household Income".format(provider_name)
  xlabel = "Median Household Income, 2014-2018, Dollars"
  ylabel = "Mean Throughput Mbps, MLAB {} 2020 data".format(provider_name)

  scatter = MhiMbpsScatter(df_provider, speed_col, output, title, xlabel, ylabel)

#################### Main Control Flow
# Since providers only come from MLAB, just hardcode the path
df_mlab = pd.read_csv("../data/mlab_2020.csv")

# Example with Comcast
scatter_for_provider(df_mlab, "COMCAST-7922 - Comcast Cable Communications, Inc.")

