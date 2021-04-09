import datetime as dt
import pandas as pd
import seaborn as sns
import pyarrow.parquet as pq
import matplotlib.pyplot as plt
import glob
import os




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