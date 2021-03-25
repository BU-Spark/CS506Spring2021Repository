# Functions for pulling data from twitter via tweepy
import json
import tweepy
import datetime as dt
import pandas as pd
import os

cur_path = os.path.dirname(__file__)
file_path = cur_path + '\\keys.json'

with open(file_path) as keys:
    config = json.load(keys)
auth = tweepy.OAuthHandler(config['twitter']['API_key'], config['twitter']['API_secret_key'])

api = tweepy.API(auth)

def get_stock_tweets_list(stock, start_date, end_date=None):
    searched_tweets = [status for status in tweepy.Cursor(api.search, q="${}".format(stock), since=start_date, until=end_date).items()]
    return searched_tweets

def generate_df(stocks, start_date, end_date):
    data = pd.DataFrame()
    for stock in stocks:
        tweets = get_stock_tweets_list(stock, start_date, end_date)
        json_data = [tweet._json for tweet in tweets]
        stock_data = pd.io.json.json_normalize(json_data)
        stock_data['stock'] = stock
        data = data.append(stock_data)
    data['created_at'] = pd.to_datetime(data['created_at'])
    data = data.set_index('created_at')
    return data

