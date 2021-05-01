# Author: Joey_Cheng
# Date: 2021/4/13
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# get all labels
data = pd.DataFrame()
for i in range(2015, 2021):
    new_data = pd.read_csv("../data/Special-Events-" + str(i) + ".csv")
    new_data = new_data.loc[new_data["CHARGED"] == "SPECIAL EVENTS"]
    data = data.append(new_data, ignore_index=True)

labels = data.DESCRIPTION.value_counts(ascending=True).index
values = data.DESCRIPTION.value_counts(ascending=True).values
# print(labels, values)

# plot
fig, ax = plt.subplots()
fig.set_size_inches(12, 18, forward=True)
left = np.zeros(len(labels))

for i in range(2015, 2021):
    data = pd.read_csv("../data/Special-Events-" + str(i) + ".csv")
    data = data.loc[data["CHARGED"] == "SPECIAL EVENTS"]
    counts = np.zeros(0)

    for l in labels:
        value_counts = data.DESCRIPTION.value_counts()
        # if recorded
        if l in value_counts.index:
            counts = np.append(counts, value_counts[l])
        else:
            counts = np.append(counts, 0)

    # plot
    bars = ax.barh(list(labels), counts, left=left, label = i)
    left = np.add(left, counts)

# add annotation
for bar, value in zip(bars, values):
    plt.annotate(value, xy=(value, bar.get_y() + 0.4), ha='left', va='center')

# save fig
ax.set_xlabel("Record Counts")
ax.set_ylabel("Event")
ax.set_title("Record Counts by Year")
ax.legend(loc=4)
plt.ylim((-1, 72))
plt.tight_layout()
plt.savefig("../img/Record Counts by Year.png")
