# Author: Joey_Cheng
# Date: 2021/3/21

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def most_frequent_events():
    events = []
    counts = []

    for y in range(15, 21):
        data = pd.read_csv("../data/Special-Events-20" + str(y) + ".csv")

        events.append(data.OTCODE.value_counts().idxmax())
        counts.append(data.OTCODE.value_counts().max())

    return events, counts

# Return the top n events index and occurrence time
def most_frequent_event_total(n):
    OTCode = pd.Series()

    for y in range(15, 21):
        data = pd.read_csv("../data/Special-Events-20" + str(y) + ".csv")
        OTCode = pd.concat([OTCode, data.OTCODE], ignore_index=True)

    return OTCode.value_counts()[:n].index.values, OTCode.value_counts()[:n].values

def least_frequent_events():
    events = []
    counts = []

    for y in range(15, 21):
        data = pd.read_csv("../data/Special-Events-20" + str(y) + ".csv")

        vc = data.OTCODE.value_counts()
        events.append(vc[vc == vc.min()].index.values)
        counts.append(vc.min())

    return events, counts

def plot_most_frequent_events():
    events, counts = most_frequent_events()

    bars = plt.bar(x=range(2015, 2021), height=counts, color = ["sienna", "olive", "brown"])

    for bar, label in zip(bars, events):
        height = bar.get_height()
        plt.annotate(label, xy=(bar.get_x() + bar.get_width() / 2, 300), ha='center', color = "white")
        plt.annotate(height, xy=(bar.get_x() + bar.get_width() / 2, height), ha='center', va='bottom')

    plt.xlabel("Year")
    plt.ylabel("OT times")
    plt.title("Most frequent OT events by year")

    plt.show()


def plot_most_frequent_events_total(n):
    events, counts = most_frequent_event_total(n)
    # print(events, counts)

    plt.figure(figsize=(10, 7))
    bars = plt.bar(x=events.astype(str), height=counts, color=["sienna", "olive", "brown", "peru"])

    for bar, label in zip(bars, events):
        height = bar.get_height()
        plt.annotate(height, xy=(bar.get_x() + bar.get_width() / 2, height), ha='center', va='bottom')

    plt.xlabel("Event Code")
    plt.ylabel("OT times")
    plt.title("Most frequent OT events 2015-2020")

    plt.show()

if __name__ == '__main__':
    # most_frequent_events()
    # least_frequent_events()
    # plot_most_frequent_events()
    plot_most_frequent_events_total(10)