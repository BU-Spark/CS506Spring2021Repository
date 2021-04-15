# In this script, we use the as_map.csv data to map AS Numbers from the mlab_data
# to a new column, ProviderName. This will make it easier to understand which entities
# are acting in the MLAB data.
# 
# Author: Nathan Lauer
# Please feel free to ask me any questions, I hope you're having a nice day!

import argparse
import pandas as pd 

########## Main execution flow
parser = argparse.ArgumentParser(description='Map AS Numbers to Provider Name')
parser.add_argument('--as-map', dest='as_map', help='The input AS Map csv file')
parser.add_argument('--mlab-data', dest='mlab_data', help='The input MLAB data csv file')
parser.add_argument('--output', dest='output_file', help='Output file to write to')
args = parser.parse_args()

# Open the input files
as_df = pd.read_csv(args.as_map)
mlab_df = pd.read_csv(args.mlab_data)

# Add mapped AS name to mlab data
df = pd.merge(mlab_df, as_df, on='ProviderNumber', how='left') # left outer join, preseves all input
df.to_csv(args.output_file, index=False)