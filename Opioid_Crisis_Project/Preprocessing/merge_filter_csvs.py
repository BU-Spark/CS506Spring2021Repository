import os
import glob
import pandas as pd
import numpy as np
import sys

from datetime import datetime

def merge_csvs(folder,new_file_name):
    '''
    folder: folder containing split up csvs with same columns titles
    new_file_name: name you want the merged file written to
    
    Function merges the csv files and saves to a new file
    '''

    # -Change into the directory with all of the unmerged csv files
    os.chdir('./'+folder)
    #print(os.getcwd()) 

    # -Use glob pattern matching to gather all files with extension .csv
    # -Save to list --> all_filenames
    file_extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(file_extension))]
    #print("{} these are all the filenames ending in .csv".format(all_filenames))

    # -Combine files in the list using pd.concat() and export to csv
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
    
    path = os.getcwd() #need to get back to data folder
    parent = os.path.join(path,os.pardir)
    os.chdir(parent)

    combined_csv.to_csv(new_file_name,index=False)

    return

def filter_empty_rows(csv_file):
    '''
    csv_file: the old file that needs filtering
    
    Drops all rows from empty campaign by checking for blank cells under Title column, returns updated dataframe
    '''
    csv = pd.read_csv(csv_file)
    csv.drop(csv.index[(csv["Title"].isnull()==True)],axis=0,inplace=True)
    
    #check_for_nan = csv['Title'].isnull()
    #rows_to_remove = np.where(check_for_nan==True)[0]
    #update_df = csv.drop(rows_to_remove,axis=0,inplace=True)

    return csv

def filter_country(dataframe):
    '''
    dataframe: pandas dataframe that is the most updated based on previous filtering functions

    Filters out international campaign by checking for currency codes other than 'USD', returns updated dataframe
    '''
    dataframe.drop(dataframe.index[(dataframe["Currency_Code"] != "USD")],axis=0,inplace=True)
    
    return dataframe

def convert_datetime(dataframe):
    '''
    dataframe: pandas dataframe that is most updated based on previous filtering functions
    
    Iterates over the column for Campaign Date and converts strings to datetime objects
    '''
    
    for index, row in dataframe.iterrows():
        try:
            dt = datetime.strptime(row['Campaign_Date'],'%B %d, %Y') # Converts Month day, year
            #datetime.strptime(row['Campaign_Date'],'%B %d, %Y')
        except:
            dt = datetime.strptime(row['Campaign_Date'],'%d-%b-%y') # Converts d-mmm-yy

            #datetime.strptime(row['Campaign_Date'],'%d-%b-%y')
    
        dataframe.at[index,'Campaign_Date'] = dt
        #print(type(row['Campaign_Date']))
    
    #try:
    #    dataframe['Campaign_Date'] = pd.to_datetime(dataframe['Campaign_Date'], format='%B %d, %Y')
    #except:
    #    dataframe['Campaign_Date'] = pd.to_datetime(dataframe['Campaign_Date'], format='%d-%b-%Y')
    
    #print(dataframe['Campaign_Date'])

    #print(dataframe['Campaign_Date'][6057])
    #print(dataframe['Campaign_Date'].dtypes)
    
    return dataframe


def main():
    '''
    Directions: 
    1) If you have unmerged files from the web scraper, create a new folder in 
    ./data and move all the unmerged csv files to that folder
        - it will write the merged csvs to a new csv--> this is merged, but unprocessed

    2) Call merge_csvs() on that folder with an attribute as the new csv you want
    the merged dataframe written to

    3) Call any other functions which further process the data:
        - filter_empty_rows()
        - filter_country()
        - convert_datetime()
    
    4) Write to a new csv which represents the merged, filtered data in the ./data folder
    
    '''

    # -Navigate from /preprocessing folder into into /data folder
    cwd = os.getcwd()
    os.chdir("..")
    os.chdir(cwd+'/data')

    # -Merge broken up csvs
    folder = 'all' #move all individual unmerged files to a new folder in './data', place the name of that folder here
    new_file_name = 'campaign_bs4_data_FINAL2.csv' #choose the title of the merged files
    merge_csvs(folder,new_file_name) #merge files and write to csv in data folder
    
    # -Do further processing by calling other filtering functions based on the original merged file
    updated_csv = filter_empty_rows('campaign_bs4_data_FINAL.csv') #filter out empty rows
    updated_csv = filter_country(updated_csv) #filter out international campaigns
    
    #updated_csv.to_csv('updated_csv_countries.csv',index=False)
    #dataframe = pd.read_csv('updated_csv_countries.csv')

    # -Convert campaign dates to datetime objects, so we can perform computations and visualize data over time
    updated_csv = convert_datetime(updated_csv) 

    # -Create new csv with filtered data, this file will be further processed in 'processing_sentiment_local.py'
    
    updated_csv.to_csv('updated_csv_filtered_FINAL.csv',index=False)
    
if __name__ == '__main__':
    main()

