# In this script, we extract out a list of all the Providers present in the MLAB data
# 
# Author: Nathan Lauer
# Please feel free to ask me any questions, I hope you're having a nice day!
import pandas as pd
import argparse

########## Main execution flow
parser = argparse.ArgumentParser(description='Map AS Numbers to Provider Name')
parser.add_argument('--mlab-data', dest='mlab_data', help='The input MLAB data csv file')
parser.add_argument('--output', dest='output_file', help='Output file to write to')
args = parser.parse_args()

# Read the MLAB data
df = pd.read_csv(args.mlab_data)
providers = df.ProviderName.unique()

providers_df = pd.DataFrame(data=providers, columns=['ProviderName'])
providers_df.to_csv(args.output_file, index=False)