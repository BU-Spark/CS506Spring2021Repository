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


### Scatter Class
class MhiMbpsScatter:
  def __init__(self, df_input, speed_col, output, title, xlabel, ylabel):
    self.df_input = df_input
    self.speed_col = speed_col
    self.output = output
    self.title = title
    self.xlabel = xlabel
    self.ylabel = ylabel

  def run(self):
    # Read input files
    df_mhi = pd.read_csv("../data/median_income_2014_2018.csv")
    mapc_cities = pd.read_csv("../data/mapc_municipalities.csv")['municipal'].to_list()

    # Possibly rename municipal column in input file
    if 'municipal' in self.df_input.columns:
      self.df_input = df_input.rename(columns={"municipal": "City"})

    # First, compute average MBPS per city in mlab data
    mlab_avg_mbps = self.df_input.groupby(['City']).mean() #.drop(columns=['MinRTT', 'Latitude'  ,'Longitude' ,'ProviderNumber'])
    mlab_avg_mbps = round(mlab_avg_mbps[[self.speed_col]], 2)

    # Rename 'municipal' in MHI file to City
    df_mhi['City'] = df_mhi['municipal']

    # Join mlab_avg_mbps and df_mhi
    joined = pd.merge(df_mhi, mlab_avg_mbps, on="City")
    joined = joined[['mhi', 'City', self.speed_col]]

    if joined.shape[0] < 5:
      return

    # Filter outliers
    joined = joined[joined[self.speed_col]<150]

    # Note: the join "auto-removed" any cities that did not appear in both data sets.
    # It would be interesting to have a list of these.

    # Add a new column that indicates if the city is in MAPC munis, and build a color array from it
    # breakpoint()
    joined['InMapc'] = joined.apply(lambda row: city_in_mapc(row['City'], mapc_cities), axis=1)
    out_color = '#7d7975'
    in_color = '#eba134'
    colors = np.array([in_color if city == 1 else out_color for city in joined['InMapc']])

    # Plot City against mhi
    fig, ax = plt.subplots(figsize=(15,10))
    x = joined['mhi']
    y = joined[self.speed_col]
    scatter = ax.scatter(x, y, alpha=0.9, c=colors)

    # Label each data point with the associated city
    # city_labels = joined['City'].to_list()
    # speed_label = joined[self.speed_col].to_list()
    labels = (joined['City'] + " (" + joined[self.speed_col].astype(str) + " Mbps)").to_list()
    tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=labels)
    mpld3.plugins.connect(fig, tooltip)

    # Set labels: these need to be updated to allow for either Ookla or MLAB
    ax.set_xlabel(self.xlabel, size=20)
    ax.set_ylabel(self.ylabel, size=20)
    ax.set_title(self.title, size=30)
    # xvalues = np.arange(40000, 240000, 20000)
    # yvalues = np.arange(0, 1000000, 200000)
    # ax.set_xticklabels(xvalues, fontsize=16)
    # ax.set_yticklabels(yvalues, fontsize=16)
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
    if not in_mapc_data.empty:
      x_in = in_mapc_data['mhi']
      y_in = in_mapc_data[self.speed_col]
      z_in = np.polyfit(x_in, y_in, 1)
      p_in = np.poly1d(z_in)
      ax.plot(x_in,p_in(x_in),"--", c=in_color, label='MAPC Tracked Municipalities')
    
    # Not in MAPC trendline
    if not out_mapc_data.empty:
      x_out = out_mapc_data['mhi']
      y_out = out_mapc_data[self.speed_col]
      z_out = np.polyfit(x_out, y_out, 1)
      p_out = np.poly1d(z_out)
      ax.plot(x_out,p_out(x_out),"--", c=out_color, label='Non-Tracked Municipalities')

    # Finally, show the plot
    ax.legend()
    # mpld3.show()

    mpld3.save_html(fig, self.output)

def scatter_for_provider(df_mlab, provider_name, short_name):
  # TODO: filter df_mlab by provider
  df_provider = df_mlab[df_mlab.ProviderName == provider_name]

  speed_col = "MeanThroughputMbps"
  output = "../output/providers/mlab_by_provider_{}_2020.html".format(short_name)
  title = "MLAB {}: Mean Throughput Broadband Speed against Median Household Income".format(short_name)
  xlabel = "Median Household Income, 2014-2018, Dollars"
  ylabel = "Mean Throughput Mbps, MLAB {} 2020 data".format(short_name)

  scatter = MhiMbpsScatter(df_provider, speed_col, output, title, xlabel, ylabel)
  scatter.run()

#################### Main Control Flow
# parser = argparse.ArgumentParser(description='Scatter of MBPS against MHI')
# # parser.add_argument('--mhi-file', dest="mhi_file", help="Census file")
# parser.add_argument('--input-file', dest="input_file", help="MLAB data")
# # parser.add_argument('--mapc-file', dest="mapc_file", help="MAPC municipalities file")
# parser.add_argument('--speed-col', dest="speed_col", help='name of column that has speed value')
# parser.add_argument('--output', dest="out_file", help="Outputfile")
# args = parser.parse_args()

# # Read input 
# df_input = pd.read_csv(args.input_file)
# title = "MLAB: Mean Throughput Broadband Speed against Median Household Income"
# xlabel = "Median Household Income, 2014-2018, Dollars"
# ylabel = "Mean Throughput Mbps, MLAB 2020 data"
# scatterClass = MhiMbpsScatter(df_input, args.speed_col, args.out_file, title, xlabel, ylabel)
# scatterClass.run()

# Since providers only come from MLAB, just hardcode the path
df_mlab = pd.read_csv("../data/mlab_2020.csv")

# Example with Comcast
# scatter_for_provider(df_mlab, "ATT-INTERNET4 - AT&T Services, Inc.", "AT&T")
# scatter_for_provider(df_mlab, "ATT-INTERNET4 - AT&T Services, Inc.", "AT&T")

df_providers = pd.read_csv("../data/providers.csv")
# Generate a scatter plot for each provider
for _, row in df_providers.iterrows():
  provider_name = row[0].strip()
  short_name = row[1].strip()
  print("Generating plot for {}".format(short_name))
  scatter_for_provider(df_mlab, provider_name, short_name)
  


# Some ideas:
# - Produce second plot, with data points that are above 150 MBPS removed
# - Modify xvalues and yvalues to go from min to max, not hard coded.
# - Write scripts that automate the input values into this python script
# - Pass args for title, xlabel, and ylabel.
# - Modify tooltip to include MHI and speed value
# - Produce modified ookla data that has speeds measured in mbps, not just kbps.