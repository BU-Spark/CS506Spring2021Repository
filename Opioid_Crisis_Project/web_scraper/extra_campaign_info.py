from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import pandas as pd
from os import getcwd
from bs4 import BeautifulSoup
import requests
import json
import os

def get_updatecomment_count(urls):
    cwd = getcwd()
    os.chdir("..")
    PATH = getcwd() + '/chromedriver'
    driver = webdriver.Chrome(PATH)

    '''
    get_updatecomment_count(): this function takes a URL for a GoFundMe campaign and returns 
    the number of campaign comments & updates if applicable 
    
    Args:
        urls (list of strings): list of GoFundMe urls

    Returns:
        num_updates (list of ints): list of # of campaign updates
        num_comments (list of ints): list of # of campaign comments
    '''
    num_updates = []
    num_comments = []

    for url in urls:
        driver.get(url)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # scroll to bottom of GoFundMe page
        time.sleep(3) # wait for updates and comments section to load

        html = driver.page_source
        parsed_html = BeautifulSoup(html, features="lxml") # parse HTML from Chromedriver
        driver.close()

        updates = parsed_html.find('div', class_='p-campaign-updates')
        comments = parsed_html.find('div', class_='p-campaign-comments')

        num_updates.append(0) if updates == None else num_updates.append(int(re.sub("[^0-9]", "", updates.h2.text))) # regex to remove text, keep only updates as number
        num_comments.append(0) if comments == None else num_comments.append(int(re.sub("[^0-9]", "", comments.h2.text))) # regex remove text, keep only comments as number
    
    return num_updates, num_comments

def get_script_data(urls):
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
    has_beneficiary = []
    is_charity = []
    charity = []
    currency_code = []
    donation_count = []
    comments_enabled = []
    donations_enabled = []
    has_donations = []
    country = []
    is_business = []
    is_team = []
    photo_url = []

    for url in urls:
        html = requests.get(url).text 
        data = json.loads(re.findall(r'window\.initialState = ({.*?});', html)[0]) #output "initialState" script that contains campaign info

        # print( json.dumps(data, indent=4))  #output JSON

        # print('Has_Beneficiary: ', data['feed']['campaign']['has_beneficiary'])
        # print('Is_Charity: ', data['feed']['campaign']['is_charity'])
        # print('Charity: ', data['feed']['campaign']['charity'])
        # print('Currency_Code: ', data['feed']['campaign']['currencycode'])
        # print('Donation_Count: ', data['feed']['campaign']['donation_count'])
        # print('Comments_Enabled: ', data['feed']['campaign']['comments_enabled'])
        # print('Donations_Enabled: ', data['feed']['campaign']['donations_enabled'])
        # print('Has_Donations: ', data['feed']['campaign']['has_donations'])
        # print('Country: ', data['feed']['campaign']['location']['country'])
        # print('Is_Business: ', data['feed']['campaign']['is_business'])
        # print('Is_Team: ', data['feed']['campaign']['is_team'])
        # print('Photo_Url: ', data['feed']['campaign']['campaign_image_url'])
        
        try:    
            has_beneficiary_data = data['feed']['campaign']['has_beneficiary']
        except KeyError:
            has_beneficiary_data = ''
        
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
            has_donations_data = data['feed']['campaign']['has_donations']
        except KeyError:
            has_donations_data = ''

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

        try:
            photo_url_data = data['feed']['campaign']['campaign_image_url']
        except KeyError:
            photo_url_data = ''

        has_beneficiary.append(has_beneficiary_data)
        is_charity.append(is_charity_data)
        charity.append(charity_data) if charity_data == {} else charity.append('')
        currency_code.append(currency_code_data)
        donation_count.append(donation_count_data)
        comments_enabled.append(comments_enabled_data)
        has_donations.append(has_donations_data)
        country.append(country_data)
        is_business.append(is_business_data)
        is_team.append(is_team_data)
        photo_url.append(photo_url_data)
    return has_beneficiary, is_charity, charity, currency_code, donation_count, comments_enabled, has_donations, country, is_business, is_team, photo_url

urls = ["https://www.gofundme.com/f/whose-corner-is-it-anyway?qid=30352514c51c3880fb30bc9429c27736", "https://www.gofundme.com/f/1wlddigtio?qid=067af41e16867d4d13a291ad6df401d0", "https://www.gofundme.com/f/stop-kenney-from-shutting-down-ioat?qid=a64ddf83d13463c4b63db182661b2c1e", "https://www.gofundme.com/f/pups-need-veterinary-care-amp-family-help?qid=90c8529e6c4593f41a1916048b306c2c"]
print(get_updatecomment_count(urls))
print(get_script_data(urls))
