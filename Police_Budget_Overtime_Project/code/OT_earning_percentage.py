# Author: Joey_Cheng
# Date: 2021/3/21

import pandas as pd
import matplotlib.pyplot as plt

# Calculate the OT earning percentage
def calculate_OT_pct():

    pct = []

    for y in range(11, 21):
        data = pd.read_csv("../data/police-earnings-report-20" + str(y) + ".csv", encoding='latin-1')

        data[data.columns[6]] = data[data.columns[6]].str.replace('$', '').str.replace(',', '').str.replace('-', '0')
        data[data.columns[10]] = data[data.columns[10]].str.replace('$', '').str.replace(',', '')

        data[data.columns[6]].fillna(0, inplace=True)
        data[data.columns[10]].fillna(0, inplace=True)

        data[data.columns[6]] = data[data.columns[6]].astype(float)
        data[data.columns[10]] = data[data.columns[10]].astype(float)

        pct.append(data[data.columns[6]].sum() / data[data.columns[10]].sum())

    return pct


def plot_OT_pct():
    plt.xlabel("Year", color = "brown")
    plt.ylabel("OT earning percentage", color = "brown")
    plt.title("Percentage of OT earnings by year")
    plt.xlim((2011, 2021))
    plt.plot(range(2011, 2021, 1), calculate_OT_pct(), color = "red")
    plt.xticks(range(2011, 2021, 1))
    plt.show()

if __name__ == '__main__':
    print(calculate_OT_pct())
    plot_OT_pct()