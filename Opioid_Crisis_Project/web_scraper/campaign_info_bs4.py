from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import getcwd
from lxml import html
import requests
from requests.models import Response
from datetime import datetime, timedelta
import json
import re
from time import time
import pandas as pd
import numpy as np
from os import getcwd

URLPATH = getcwd() + '/data/urls.csv'
cols = [
    'URL',
    'All_Keywords',
    'Title',
    'Reason_For_Fund',
    'Total_Raised',
    'Total_Goal',
    'Percent_Reached',
    'Campaign_Date',
    'Organizer',
    'Beneficiary',
    'Location',
    'Donors',
    'Shares',
    'Followers',
    "is_charity",
     "charity", "currency_code", "donation_count", "comments_enable", "donations_enabled", "country", "is_business", "is_team"
]

def scrape_campaign(url_row):
    page = requests.get(url_row[0])
    soup = BeautifulSoup(page.text, "lxml")

    # list containing all the information (roughly matching Heather's format)
    # [Name, Reason for Fund, Total Raised, Total Requested, Raised Ratio, Date Created, Organizer, Beneficiary, Location]
    information_list = [url_row[0], reformat_keyword_list(url_row[1])]

    '''
    extract the title of the campaign.
    '''
    try:
        info = soup.find(class_='a-campaign-title')
        title = info.text
        #print("This campaign is titled: " + title)
        information_list.append(title)
    except:
        #print("No title found")
        information_list.append(float('nan'))


    '''
    extract campaign tag, which tells the reason for campaign
    '''
    try:
        info = soup.find(class_='m-campaign-byline-type divider-prefix meta-divider flex-container align-middle color-dark-gray a-link--unstyled a-link')
        tag = info.text
        #print("This campaign has the tags: " + tag)
        information_list.append(tag)
    except:
        #print("No tags found")
        information_list.append(float('nan'))


    '''
    extracts the amount raised
    '''
    try:
        info = soup.find(class_='m-progress-meter-heading')
        info = info.text
        amount_raised = info.split(" raised")[0]
        amount_raised = int(amount_raised[1:].replace(',',''))
        information_list.append(amount_raised)
    except:
        information_list.append(float('nan'))

    '''
    extracts the total goal of a campaign.
    then calculate how much of the goal was reached in terms of a percentage.
    '''
    try:
        info = soup.find(class_='m-progress-meter-heading')
        info = info.text
        total_goal = info.split("of")[1]
        total_goal = total_goal.split("goal")[0]
        total_goal = int(total_goal[2:].replace(',',''))

        percent_goal_reached = round((amount_raised/total_goal), 2)
        #print("This campaign reached " + str(percent_goal_reached) + "% of its goal.")
        information_list.append(total_goal)
        information_list.append(percent_goal_reached)
    except:
        #print("This campaign raised $" + str(amount_raised) + ". There was no total goal.")
        information_list.append(float('nan'))
        information_list.append(float('nan'))

    '''
    extract date that campaign was created
    '''
    try:
        info = soup.find(class_='m-campaign-byline-created a-created-date')
        days_ago = info.text.split("days ago")[0]
        days_ago = int(days_ago[len("Created "):])

        date_created = datetime.date(datetime.now()) - timedelta(days=days_ago)
        date_created = date_created.strftime('%B %d, %Y')
        information_list.append(date_created)
    except:
        try:
            info = soup.find(class_='m-campaign-byline-created a-created-date')
            date = info.text[len("Created "):]
            #print("This campaign was created on: " + date)
            information_list.append(date)
        except:
            #print("No date found")
            information_list.append(float('nan'))


    '''
    extract the organizer of the campaign.
    '''
    try:
        info = soup.find(class_='m-campaign-members-main-organizer')
        organizer = info.text.split("Organizer")[0]
        organizer = organizer.replace(u'\xa0', u'')
        #print("This campaign is organized by: " + organizer)
        information_list.append(organizer)
    except:
        #print("No organizer found")
        information_list.append(float('nan'))


    '''
    extract the beneficiary of the campaign.
    '''
    try:
        info = soup.find(class_='m-campaign-byline-description')
        beneficiary = info.text.split("behalf of ")[1][:-1]
        #print("This campaign is created to help: " + beneficiary)
        information_list.append(beneficiary)
    except:
        try:
            info = soup.find(class_='m-campaign-byline-description')
            beneficiary = info.text.split("benefit ")[1][:-1]
            #print("This campaign is created to help: " + beneficiary)
            information_list.append(beneficiary)
        except:
            #print("No beneficiary found")
            information_list.append(float('nan'))


    '''
    extract the location of the campaign.
    '''
    try:
        info = soup.find(class_='m-campaign-members-main-organizer')
        location = info.text.split("donations")[1]
        #print("This campaign is located at: " + location)
        information_list.append(location)
    except:
        try:
            location = info.text.split("Organizer")[1]
            #print("This campaign is located at: " + location)
            information_list.append(location)
        except:
            #print("No location found")
            information_list.append(float('nan'))

    '''
    extracting dynamic parts of the page: donors, followers, shares
    '''
    driver = webdriver.Chrome(getcwd()+'/chromedriver')
    driver.get(url_row[0])

    html = driver.page_source
    soup = BeautifulSoup(html, features="lxml")

    try:
        info = soup.find(class_='o-campaign-sidebar-wrapper')
        info = info.text.split('goal')[1]
        donors = int(info.split('donors')[0])
        information_list.append(donors)

        info = info.split('donors')[1]
        shares = int(info.split('shares')[0])
        information_list.append(shares)

        info = info.split('shares')[1]
        followers = int(info.split('followers')[0])
        information_list.append(followers)

    except:
        for i in range(3):
            information_list.append(float('nan'))

    

    '''
    NIKITA'S EXTRA CAMPAIGN CODE
    '''

    '''
    get_script_data(): this function takes a URL for a GoFundMe campaign and returns 
    information stored in JSON format inside the page's window\.initialState script tag 
    
    Args:
        urls (list of strings): list of GoFundMe urls
    Returns:
        has_beneficiary (list of bools): T/F list where True if campaign has beneficiary, False if not
        is_charity (list of bools): T/F list where True if campaign is a charity, False if not
        charity (list of strings): list of charity name if provided
        currency_code (list of strings): list of campaign currency codes
        donation_count (list of ints): list of # of campaign donations
        comments_enabled (list of bools): T/F list where True if campaign has comments enabled, False if not
        donations_enabled (list of bools): T/F list where True if campaign has donations enabled, False if not
        has_donations (list of bools): T/F list where True if campaign has donations, False if not
        country (list of strings): list of country codes
        is_business (list of bools): T/F list where True if campaign is business, False if not
        is_team (list of bools): T/F list where True if campaign has team, False if not
    '''
    
    html = requests.get(url_row[0]).text 
    data = json.loads(re.findall(r'window\.initialState = ({.*?});', html)[0]) #output "initialState" script that contains campaign info


    try:
        is_charity_data = data['feed']['campaign']['is_charity']
    except KeyError:
        is_charity_data = ''

    try: 
        charity_data = data['feed']['campaign']['charity']
    except KeyError:
        charity_data = ''
    
    try:
        currency_code_data = data['feed']['campaign']['currencycode']
    except KeyError:
        currency_code_data = ''

    try:
        donation_count_data = int(data['feed']['campaign']['donation_count'])
    except KeyError:
        donation_count_data = ''
    try:
        comments_enabled_data = data['feed']['campaign']['comments_enabled']
    except KeyError:
        comments_enabled_data = ''

    try:
        donations_enabled_data = data['feed']['campaign']['donations_enabled']
    except KeyError:
        donations_enabled_data = ''
    
    try:
        country_data =  data['feed']['campaign']['location']['country']
    except KeyError:
        country_data = ''
    
    try:
        is_business_data = data['feed']['campaign']['is_business']
    except KeyError:
        is_business_data = ''
    
    try:
        is_team_data = data['feed']['campaign']['is_team']
    except KeyError:
        is_team_data = ''

    information_list.append(is_charity_data)
    information_list.append(charity_data) if charity_data == {} else information_list.append('')
    information_list.append(currency_code_data)
    information_list.append(donation_count_data)
    information_list.append(comments_enabled_data)
    information_list.append(donations_enabled_data)
    information_list.append(country_data)
    information_list.append(is_business_data)
    information_list.append(is_team_data)

    return information_list



def reformat_keyword_list(keywords):
    """
    Converts string version of keywords list back to a python list

    Args:
        keywords (string): Keyword list as one string

    Returns:
        [list]: Python list of each keyword separated into strings
    """    
    kw = keywords.replace('[', '').replace(']', '').replace('\'', '').replace(' ', '')
    kw = kw.split(",")
    return list(set(kw))


def generate_df(url_csv):
    """
    Calls scraper on each row of url dataframe and returns scraped data

    Args:
        url_csv ([DataFrame]): csv with all urls

    Returns:
        [DataFrame]: scraped data
    """    
    # test with number of urls
    data = pd.DataFrame(url_csv.apply(scrape_campaign, axis=1).tolist(), columns=cols)
    return data


def main():
    start = time()

    # import csv with urls
    url_csv = pd.read_csv(URLPATH)
    print(np.shape(url_csv))

    #url_csv = url_csv[url_csv['urls'] == "https://www.gofundme.com/f/jaynasdream"]
    data = generate_df(url_csv)
    data.to_csv(getcwd() + '/data/campaign_bs4_data.csv', index=False)
    end = time()
    print(f'TIme to run: {(end - start) / 60} minutes')

if __name__ == '__main__':
    main()

