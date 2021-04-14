# Author: Joey_Cheng
# Date: 2021 / 4 / 13

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../data/Special-Events-2020-updated.csv")

plt.figure(figsize=(18, 12))
plt.title("Special Events OTHOURS 2020")
plt.xlabel("OT Hours")
plt.ylabel("Description")

OTHours = data.groupby("DESCRIPTION")["OTHOURS"].sum().sort_values()
bars = plt.barh(OTHours.index, OTHours.values, color=["sienna", "olive", "brown", "peru"])

# add annotates
for bar, label in zip(bars, OTHours.values):
    plt.annotate(label, xy=(label, bar.get_y() + 0.4), ha='left', va='center')

plt.tight_layout()
plt.savefig("../img/OTHOURS by Description 2020.png")