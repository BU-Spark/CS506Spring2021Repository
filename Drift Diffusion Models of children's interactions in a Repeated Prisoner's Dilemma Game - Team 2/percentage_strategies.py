#code to create correlation matrix to look at potential regressions to use 
import numpy as np
import pandas as pd 
import csv
#read in the dataset 
import matplotlib.pyplot as plt

# Use CS506 library to import the CSV with the twins data
df = pd.read_csv("dataset_with_strategies.csv")
print(df.head())

#gets the percentage of each type of strategy 
#stored under the variable 'percentage'

#df.groupby('Strategy').count()
percentage = df['Strategy'].value_counts(normalize=True)
print(percentage)

#plot a pie chart of each strategy

percentage.plot.pie(y='percentage', figsize=(5,5))
fig = plt.figure('percentage of strategies')
#keeps pie chart open after code ends
plt.show(block=True)