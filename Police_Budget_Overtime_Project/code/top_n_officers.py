"""
Joshua Cominelli
CS506
top_n_officers.py
"""

import pandas as pd
import matplotlib.pyplot as plt

# n: Number of officers to display
def find_top_officers(n):

    # Iterate each year 2015-2020
    all_years = []
    for i in range(15,21):
        df = pd.read_csv('../data/Special Events 2015 - present - 20'+str(i)+'.csv')[['NAME','OTDATE','OTHOURS']]
        df.set_index(['NAME'])
        all_years.append(df)

        df_20xx = df.groupby(['NAME']).sum()
        df_20xx = df_20xx.sort_values(by=['OTHOURS'],ascending=False)
        df_20xx = df_20xx[:n]

        pd.set_option('display.max_rows', n)
        plt.rcParams["figure.figsize"] = [17, 8]

        print('\n~~ BEGIN 20'+str(i)+' ~~')
        print(df_20xx.head(n))
        print('\n~~ END 20'+str(i)+' ~~')

        df_20xx.plot(kind='bar')
        plt.title("BPD Special Event Overtime Hours: 20"+str(i))
        plt.xlabel("Officer Name")
        plt.ylabel("Overtime Hours")
        plt.tight_layout()
        plt.show()

    # Show total 2015-2020
    df_total = pd.concat(all_years, ignore_index=True) 
    df_total.set_index(['NAME'])
    df_total = df_total.groupby(['NAME']).sum()
    df_total = df_total.sort_values(by=['OTHOURS'],ascending=False)
    df_total = df_total[:n]

    pd.set_option('display.max_rows', n)
    plt.rcParams["figure.figsize"] = [17, 8]

    print('\n~~ BEGIN 2015-2020 ~~')
    print(df_total.head(n))
    print('\n~~ END 2015-2020 ~~')

    df_total.plot(kind='bar')
    plt.title("BPD Special Event Overtime Hours: Total 2015-2020")
    plt.xlabel("Officer Name")
    plt.ylabel("Overtime Hours")
    plt.tight_layout()
    plt.show()

find_top_officers(100)