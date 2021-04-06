#Authors: Nicholas Mosca, Evie Wan, Eric South


''' Steps for this Script 

1. generate lists of file paths for 2019 and 2020 versions

2. extract ticker from each path for dict key (list)

3. run list through html parser and save outputs to list for sort_values

4. Create Dict of Ticker: html parser result  for 2019 and 2020 versions

5. Convert to pandas DF

6. Write to csv 

''' 

from pathlib import Path
import pandas as pd
from html_parser import *
from path_mover import local_location # Example: /Users/nick/Documents/cs506/project
from path_mover import file_paths 

# list of file paths as strings 

Paths_2019 = file_paths(2019) # 170
Paths_2020 = file_paths(2020) # 111

#extracting tickers to list 

Ticker_2019 = []
Ticker_2020 = []

for p19 in Paths_2019:
    Ticker_2019.append(p19[54:58])

for p20 in Paths_2020:
    Ticker_2020.append(p20[54:58])


# grabbing html parser outputs new function = main_path

#2019
Risk_2019 = []

for x in Paths_2019:
    Risk_2019.append(main_path((x)))


#2020

Risk_2020 = []

for x2 in Paths_2020:
    Risk_2020.append(main_path(x2))

#removing repeated words 

#2019
clean_text_2019 = []
for company in Risk_2019:
    clean_text_2019.append(set(company))

clean_text_2020 = []
for company in Risk_2020:
    clean_text_2020.append(set(company))




#converting to Dictionary

Dict_2019 = dict(zip(Ticker_2019,Risk_2019))
Dict_2020 = dict(zip(Ticker_2020,Risk_2020))

#v2
Dict_2019v2 = dict(zip(Ticker_2019,clean_text_2019))
Dict_2020v2 = dict(zip(Ticker_2020,clean_text_2020))


DF_2019 = pd.DataFrame(Dict_2019.items(),columns = ['Ticker', "Risk Text"])
DF_2020 = pd.DataFrame(Dict_2020.items(),columns = ['Ticker', "Risk Text"])

#v2
DF_2019v2 = pd.DataFrame(Dict_2019v2.items(),columns = ['Ticker', "Risk Text"])
DF_2020v2 = pd.DataFrame(Dict_2020v2.items(),columns = ['Ticker', "Risk Text"])


#write to csv

DF_2019.to_csv('data/10k_2019.csv')
DF_2020.to_csv('data/10k_2020.csv')

#v2
DF_2019v2.to_csv('data/10k_2019v2.csv')
DF_2020v2.to_csv('data/10k_2020v2.csv')