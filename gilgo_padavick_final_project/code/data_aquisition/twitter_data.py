# Functions for pulling data from twitter via tweepy
import json
import tweepy
import datetime as dt
import pandas as pd
import os
import glob

cur_path = os.path.dirname(__file__)
file_path = cur_path + '\\keys.json'


'''
Data Aquisition using Tweepy
'''

with open(file_path) as keys:
    config = json.load(keys)
auth = tweepy.OAuthHandler(config['twitter']['API_key'], config['twitter']['API_secret_key'])

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def get_stock_tweets_list(stock, start_date, end_date=None):
    searched_tweets = [status for status in tweepy.Cursor(api.search, q="${}".format(stock), since=start_date, until=end_date).items()]
    return searched_tweets

def generate_df(stocks, start_date=None, end_date=None, save_results=False):
    # If start date not supplied, go back 8 days (will be cut off by twitter api 7 day limit)
    if not start_date:
        start_date = dt.date.today() - dt.timedelta(days=8)
    # If end date not supplied, set it to current date
    if not end_date:
        end_date = dt.date.today()
    
    data = pd.DataFrame()
    for stock in stocks:
        print("Fetching data for {} from {} to {} ...".format(stock, start_date, end_date))
        tweets = get_stock_tweets_list(stock, start_date, end_date)
        json_data = [tweet._json for tweet in tweets]
        stock_data = pd.io.json.json_normalize(json_data)
        stock_data['stock'] = stock
        print("Tweets found: {}".format(stock_data.shape[0]))
        stock_data['Datetime'] = pd.to_datetime(stock_data['created_at'])
        stock_data = stock_data.set_index('Datetime')
        if save_results:
            stock_data.to_pickle("./twitter_raw_data/clean_data/{0}_{1}_to_{2}.pkl".format(stock, start_date, end_date))
        data = data.append(stock_data)
        
    return data
    
def read_all_twitter_data(folder='./twitter_raw_data/clean_data/'):
    all_tweets_df = pd.DataFrame()
    os.chdir(folder)
    for tweet_file in glob.glob('*.pkl'):
        all_tweets_df = all_tweets_df.append(pd.read_pickle(tweet_file))

    all_tweets_df.drop_duplicates(subset=['id'], inplace=True)
    return all_tweets_df


