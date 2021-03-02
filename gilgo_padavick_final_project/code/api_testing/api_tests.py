import json
import tweepy
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

# Import keys (kept locally)
with open('keys.json') as config_file:
    config = json.load(config_file)

# Alpha Vantage Test
api_key = config['alpha_vantage']

starting_stocks = ['XSPA', 'GNUS', 'IBIO', 'GME', 'OPES']

def plot_intraday(symbol, ts_object):
        data, meta_data = ts_object.get_intraday(symbol=symbol,interval='1min', outputsize='full')
        data['4. close'].plot()
        plt.title('Intraday Times Series for the {} stock (1 min)'.format(symbol))
        plt.show()

def test_alpha_vantage(stocks):
    '''
    Plot the 1min intraday price for each stock to ensure data is available
    '''
    ts = TimeSeries(key=api_key, output_format='pandas')
    for stock in starting_stocks:
        try:
            plot_intraday(stock, ts)
        except:
            print("Error occured with {} stock".format(stock))

# Yahoo Finance API

def test_yahoo_finance(starting_stocks):
    '''
    Perfrom tests on the starting stocks to confirm if data is available.
    '''

# Finnhub API



# Twitter API (using Tweepy)
'''
Steps:
1. Create a twitter acount
2. Apply for developer API
3. Save api key and secret key to keys.json
'''
def test_twitter_api():
    auth = tweepy.OAuthHandler(config['twitter']['API_key'], config['twitter']['API_secret_key'])
    # auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    # Get the User object for twitter...
    user = api.get_user('alexcutler247')
    print("Screen name: {}".format(user.screen_name))
    print("Number of followers: {}".format(user.followers_count))
    print("Friends: ")
    for friend in user.friends():
        print(friend.screen_name)



if __name__ == "__main__":
    test_alpha_vantage(starting_stocks)
    # test_yahoo_finance(starting_stocks)
    # test_twitter_api()

