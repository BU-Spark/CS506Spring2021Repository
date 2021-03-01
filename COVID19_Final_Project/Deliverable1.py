import pandas as pd
import numpy as np

csvr = pd.read_csv("usa_county_wise.csv")

# get relevant columns
covid = csvr.loc[:,['Admin2', 'Province_State', 'Date', 'Confirmed', 'Deaths']]

RESULT = pd.DataFrame(covid, index=covid.index, columns=covid.columns)


rows = [0, 103540, 203740, 307280, 407480, 497661] # March-July
monthNames = ["March", "April", "May", "June", "July"]

for i in range(len(rows) - 1):
    month = RESULT[rows[i]:rows[i + 1]] # data from one month
    
    #con = RESULT.loc[RESULT.index[rows[i]:rows[i + 1]], 'Confirmed']
    print(monthNames[i], "2020 Covid Means:")
    print(month.mean(axis = 0, skipna = True))
    print()
