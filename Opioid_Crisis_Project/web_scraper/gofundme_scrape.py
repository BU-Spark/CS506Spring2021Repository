from bs4 import BeautifulSoup
from selenium import webdriver
from os import getcwd
import requests
import time
import pandas as pd
import numpy as np

PATH = getcwd() + '/chromedriver'


def get_urls(keywords_list):
    '''
    get_urls(): this function takes in a list of search terms, and scrapes all of the URLS for 
    GoFundMe campaigns associated with the search term and outputs it as a list
    
    Args:
        keywords_list (list of strings): list of search terms

    Returns:
        urls (list of strings): list of GoFundMe urls 
        labels (list of strings): search terms associated with GoFundMe urls
    '''
    urls = []
    labels = []
    driver = webdriver.Chrome(PATH)
    for keyword in keywords:
        # all search results have 85 pages except fentanyl with 79 pages
        lastpage = 79 if keyword == 'fentanyl' else 85
        for pg in range(1, lastpage):
            sub_url = "https://www.gofundme.com/s?q="+keyword+"&pg="+str(pg)
            driver.get(sub_url)
            html = driver.page_source  # parse HTML from Chromedriver
            time.sleep(3)
            parsed_html = BeautifulSoup(html, features="lxml")
            for link in parsed_html.find_all('a', {"class": "a-link a-link--unstyled"}, href=True):
                urls.append('https://www.gofundme.com' +
                            link['href'])  # store links in URL
                labels.append(keyword)

    return urls, labels


def convert_to_raw_df(all_urls, labels):
    """
    Generates pandas dataframe to pair urls with the keywords used to find it

    Args:
        all_urls (list of strings): contains all urls

        keywords (list of strings): list of keywords corresponding to keyword for
        each url in all_urls

    Returns:
        dataframe: formatted dataframe for urls and keywords
    """
    urls = np.array(all_urls).T
    labels = np.array(labels).T
    data = np.array([urls, labels]).T
    dataframe = pd.DataFrame(data)
    dataframe.columns = ['urls', 'keyword']
    return dataframe


def drop_qid_from_entry(x):
    # Helper method to remove qid from urls using pandas
    return x[:-37]


def drop_query_id(df):
    """
    Remove query ID so urls are clean for filtering

    Args:
        df (dataframe): dataframe

    Returns:
        df: dataframe with cleaned urls
    """    
    df.urls = df.urls.apply(drop_qid_from_entry)
    return df


def merge_redundant_urls(df):
    """
    Find all urls that were found multiple times and merges their entries into one, 
    saving each keyword in that entry

    Args:
        df ([dataframe]): raw dataframe

    Returns:
        df [dataframe]: filtered dataframe
    """
    # find all urls that appear more than once
    found_multiple = df[df.duplicated(subset=['urls'])]
    found_multiple = set(found_multiple.urls.to_list())

    # aggregate all redundant urls to first appearance, with keywords maintained
    for url in found_multiple:  # all unique urls
        # get all indices where url matches
        matches = np.where(df['urls'] == url)[0].tolist()
        for match in range(len(matches)):
            if match == 0:  # change entry of first appearance to list and add first keyword to it
                word = df.iloc[matches[match]]['keyword']
                df.iloc[matches[match]]['keyword'] = []
                df.iloc[matches[match]]['keyword'].append(word)
            else:  # add keyword of redundant url to first appearance
                df.iloc[matches[0]]['keyword'].append(
                    df.iloc[matches[match]]['keyword'])
    df = df.drop_duplicates(subset='urls', keep='first')  # drop all appearances but first
    return df


#keywords = ['opiate', 'opiates']
keywords = ['opiate', 'opioid', 'addiction', 'addict', 'heroin', 'drugs', 'overdose',
dependency', 'demon', 'recovery', 'rehabilitation', 'rehab']
all_urls, labels = get_urls(keywords)
df = convert_to_raw_df(all_urls, labels)
df = drop_query_id(df)
merged_df = merge_redundant_urls(df)
merged_df.to_csv(getcwd() + '/data/urls.csv', index=False)
