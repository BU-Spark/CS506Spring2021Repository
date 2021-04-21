import sys
import os
sys.path.append(os.path.dirname(__file__))

import datetime as dt
import pandas as pd
import seaborn as sns
import pyarrow.parquet as pq
import matplotlib.pyplot as plt
import glob
import emojis
import vocab
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer




def plot_vs_time(df, col, start_date, end_date, save_loc='./'):
    # Plots a df with a datetime index - plots col vs time
    fig, ax = plt.subplots(figsize=(30,10))
    sns.scatterplot(data=df, x=df.index, y=col, s=120)
    ax.set_xlim(start_date, end_date)
    ax.set_title(col,fontsize=20)
    ax.set_xlabel("Time",fontsize=20)
    ax.set_ylabel(col,fontsize=20)
    ax.tick_params(labelsize=20)
    
    if save_loc:
        fig.savefig(save_loc)
    else:
        fig.show()


def plot_vs_price(df, col, start, end, save_loc=None):
    # Plots a df with a datetime index and stock price data from yfanance - plots col vs time
    fig, ax1 = plt.subplots(figsize=(30,10))
    ax1 = sns.scatterplot(data=df, x=df['Datetime'], y=col, s=120)
    ax1.set_xlim(start, end)
    ax1.set_title(col,fontsize=20)
    ax1.set_xlabel("Time",fontsize=20)
    ax1.set_ylabel(col,fontsize=20)
    ax1.tick_params(labelsize=20)
    ax2 = ax1.twinx()
    ax2 = sns.lineplot(data=df, x=df['Datetime'], y="Open", color='red')
    ax2.set_ylabel("Price",fontsize=20)
    ax2.tick_params(labelsize=20)
    if save_loc:
        fig.savefig(save_loc)
    else:
        fig.show()

def import_labeled_data(path='../../data'):
    labeled_data = pd.DataFrame()
    old_dir = os.getcwd()
    os.chdir(path)
    for label_file in glob.glob('*.csv'):
        data = pd.read_csv(label_file)
        data = data[data['Sentiment'].notna()]
        data['id_str'] = data['id_str'].str.replace("a", "")
        labeled_data = labeled_data.append(data)
    os.chdir(old_dir)
    return labeled_data


def clean_twitter_text(tweets_data):
    # Change all text to lowercase
    tweets_data['text'] = tweets_data['text'].str.lower()
    tweets_data['text'] = tweets_data['text'].str.replace(',', '')
    tweets_data['text'] = tweets_data['text'].str.replace('.', '')
    tweets_data['text'] = tweets_data['text'].str.strip()
    # Remove the '...'
    tweets_data['text'] = tweets_data['text'].str.replace(r'…', '', regex=True)
    # Remove hyperlinks
    tweets_data['text'] = tweets_data['text'].replace(r'http\S+', '', regex=True)
    # Replace \n with a space 
    tweets_data['text'] = tweets_data['text'].replace(r'\n', ' ', regex=True)
    # Remove stock tags
    tweets_data['text'] = tweets_data['text'].replace(r'\$\S+', '', regex=True)
    # Remove tags
    tweets_data['text'] = tweets_data['text'].replace(r'\@\S+', '', regex=True)
    # Add eastern standard time column
    tweets_data['Datetime_eastern'] = tweets_data.index.tz_convert('US/Eastern')
    # Create decoded version of text field
    tweets_data['text_dec'] = tweets_data['text'].map(lambda x: emojis.decode(x))
    # Add spaces around emojis so they can be separated as words 
    tweets_data['text_dec'] = tweets_data['text_dec'].replace(r'(:[a-z]+:)', ' \\1 ', regex=True)

    return tweets_data

def apply_countvectorizer(df, text_col, min_df=1, vocab_def=None):
    vectorizer = CountVectorizer(stop_words='english', token_pattern='\w+|\$[\d\.]+|\S+|:[a-z]+:', min_df=min_df, strip_accents='ascii', vocabulary=vocab_def)
    train_data_vec = vectorizer.fit_transform(df[text_col])
    print("Count vector shape of vectorized data: {}".format(train_data_vec.shape))
    # Code for adding feature back on df 
    count_vect_df = pd.DataFrame(train_data_vec.todense(), columns=vectorizer.get_feature_names())
    train_data_cv = pd.concat([df, count_vect_df], axis=1)
    return train_data_cv

def apply_tfidf(df, text_col, min_df=1, vocab_def=None):
    vectorizer = TfidfVectorizer(stop_words='english', token_pattern='\w+|\$[\d\.]+|\S+|:[a-z]+:', min_df=min_df, strip_accents='ascii', vocabulary=vocab_def)
    train_data_vec = vectorizer.fit_transform(df[text_col])
    print("Count vector shape of vectorized data: {}".format(train_data_vec.shape))
    # Code for adding feature back on df 
    count_vect_df = pd.DataFrame(train_data_vec.todense(), columns=vectorizer.get_feature_names())
    train_data_tf = pd.concat([df, count_vect_df], axis=1)
    return train_data_tf

def create_tweet_features(tweets_data, run_countvec=False, run_tfidf=False):
    # clean_twitter_text should be run before this function for the best results
    # Create feature for number of exclamation marks
    tweets_data['exc_count'] = tweets_data['text'].map(lambda x: x.count("!"))
    # Create a column for number of characters 
    tweets_data['characters_nb'] = tweets_data.text.apply(len)
    # Add count for emojis
    tweets_data['emoji_count'] = tweets_data['text'].map(lambda x: emojis.count(x))

    # Add text features
    vocab_list = vocab.get_all_vocab()
    if run_countvec:
        tweets_data_vocab = apply_countvectorizer(tweets_data, 'text_dec', vocab_def=vocab_list)
    elif run_tfidf:
        tweets_data_vocab = apply_tfidf(tweets_data, 'text_dec', vocab_def=vocab_list)
    
    return tweets_data_vocab
