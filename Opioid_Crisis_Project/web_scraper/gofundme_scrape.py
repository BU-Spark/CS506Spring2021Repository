from bs4 import BeautifulSoup
from selenium import webdriver
from os import getcwd 
import requests
import time
PATH = getcwd() +'/chromedriver' #update with your Chromedriver path
print(PATH)
def get_urls(keywords_list):
    '''
    get_urls(): this function takes in a list of search terms, and scrapes all of the URLS for 
    GoFundMe campaigns associated with the search term and outputs it as a list
    '''
    urls = []
    driver = webdriver.Chrome(PATH) 
    for keyword in keywords:
        lastpage = 79 if keyword == 'fentanyl' else 85 #all search results have 85 pages except fentanyl with 79 pages
        for pg in range(1, lastpage):
            sub_url = "https://www.gofundme.com/s?q="+keyword+"&pg="+str(pg)
            driver.get(sub_url)
            html = driver.page_source #parse HTML from Chromedriver
            time.sleep(3)
            parsed_html = BeautifulSoup(html, features="lxml")
            for link in parsed_html.find_all('a', {"class": "a-link a-link--unstyled"}, href=True):
                urls.append('https://www.gofundme.com'+ link['href']) #store links in URL
    print(urls)
    return urls
# keywords = ['opiate']
keywords = ['opiate', 'opioid', 'addiction', 'addict', 'heroin', 'drugs', 'overdose', 
'dependency', 'demon', 'recovery', 'rehabilitation', 'rehab']
get_urls(keywords)
