#Objective: Navigate file paths to access html documents prior to feeding into html parser
from html_parser import *
from bulk_10k_extraction import local_location
from bs4 import BeautifulSoup, NavigableString, Tag
from pathlib import Path
import pandas as pd



# #importing index information 
# file = 'IBB-holdings.csv'
# IBB = pd.read_csv(file,skiprows=13)
# # alphabet order
# IBB.sort_values(by=['Symbol'], inplace=True) 
# # just ticker symbol
# holdings = list(IBB["Symbol"])
# holdings = holdings[:-2]

file = pd.read_csv('actual.csv')
holdings = list(file["holdings"])
holdings = holdings[:-1]

#local location that will sync with where user downloads data
# Example: /Users/nick/Documents/cs506/project
sec = '/sec-edgar-filings/'
# path to first file

#/Users/nick/Documents/cs506/project/sec-edgar-filings/ABUS
full_path = Path(local_location + sec + holdings[0])

# full list of directory's with html files
# first two 10k files for ABUS
full_set = list(full_path.glob('**/*.html'))



#works but needs adjustments to filter years 
#maybe reg expression 
def file_paths(year):
    ''' Returns a list of all of the local file paths to downloaded 10k files via bulk_10k_extraction.py,
    year = 2019 or 2020
    Output is fed into html parser function'''
    path_list =[]
    year = str(year)
    #if year != '2019' or year != '2020':
        #raise ValueError(' Years must be 2019 or 2020')
    
    if str(year) == '2019':
        index = 1
    else:
        index = 0
    base_path = local_location + sec 

    for company in holdings:
        company_path = Path(base_path + company)
        company_10ks = list(company_path.glob('**/*.html'))
<<<<<<< HEAD
        print(company)
        path_list.append(company_10ks[index])
=======
        #2019 only
        if str(company_10ks[0])[75] == '1':
            paths_19.append(str(company_10ks[0]))
        if len(company_10ks) > 1:

            #2020
            if str(company_10ks[0])[75] == '2':
                paths_20.append(str(company_10ks[0]))
            #2019
            if str(company_10ks[1])[75] == '1':
                paths_19.append(str(company_10ks[1]))

        
    #import pdb;pdb.set_trace()  
    year = str(year)
    if year == '2019':
        return paths_19
    else:
        return paths_20
>>>>>>>  working on structure data branch

    import pdb;pdb.set_trace()
    return path_list[index]
       

    




