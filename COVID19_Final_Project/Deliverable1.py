import pandas as pd
import numpy as np

csvr = pd.read_csv("usa_county_wise.csv")

# get relevant columns
covid = csvr.loc[:,['Admin2', 'Province_State', 'Date', 'Confirmed', 'Deaths']]

RESULT = pd.DataFrame(covid, index=covid.index, columns=covid.columns)

rows = [103540, 203740, 307280, 407480, 497661] # March-July
monthNames = ["March", "April", "May", "June", "July"]
stateNames = ["American Samoa", "Guam", "Northern Mariana Islands", "Puerto Rico", "Virgin Islands", "Alabama", "Alaska", 
              "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", 
              "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", 
              "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", 
              "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", 
              "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", 
              "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

RES = pd.DataFrame(index = range(55), columns=['States', 'Confirmed March', 'Confirmed April', 
                  'Confirmed May', 'Confirmed June', 'Confirmed July', 'Deaths March', 'Deaths April', 
                  'Deaths May', 'Deaths June', 'Deaths July'])

RES['States'] = stateNames

# process the data to get average values
# replace arguments for different months
for i in range(len(stateNames)):
    confirmed = 0
    death = 0
    for j in range(103540+1):
        if (stateNames[i] == RESULT['Province_State'][j]):
            confirmed = confirmed + RESULT['Confirmed'][j]
            death = death + RESULT['Deaths'][j]
        confirmed_avg = confirmed/31
        death_avg = death/31
        RES['Confirmed March'][i] = confirmed_avg
        RES['Deaths March'][i] = death_avg

print(RES)
