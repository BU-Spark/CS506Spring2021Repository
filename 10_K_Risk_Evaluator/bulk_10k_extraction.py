# Edgar SEC 10k extracting
import pandas as pd

from sec_edgar_downloader import Downloader

# importing IBB holdings. csv
file = 'IBB-holdings.csv'
IBB = pd.read_csv(file,skiprows=13)
holdings = list(IBB["Symbol"])


#setting Download location
# Example: /Users/nick/Documents/cs506/project
local_location = input(" Please enter local file path for bulk download")

def Bulk_extraction(ticker,filetype,date):
    ''' ticker = company ticker or list of tickers 
        filetype = type of financial doc (8-K,10-K)
        date = all filetypes after this date format: year-day-month
        location = local directory to store files as string''' 
    dl = Downloader(str(local_location))
    for company in ticker:
        dl.get(str(filetype),str(company),after = str(date),download_details = True)
    return "Complete"


# Have to double check to see if all funds are updated for 2019-2020
#Bulk_extraction(holdings,'10-K','2019-01-01',dl)