import pandas as pd

df = pd.read_csv("Blake_RPD_Dataset-1_Twins-03-19-21.csv")

col = df["C-EATQ_Aggression"]
max_value = col.max()

mean = col.mean()

bound1 = mean - 4
bound2 = mean + 4

newColStr = []
newCol = []

for i in range(len(col)):
    if col[i] < bound1: 
        newColStr.append("low")
        newCol.append(0)
    elif col[i] < bound2:
        newColStr.append("medium")
        newCol.append(1)
    else:
        newColStr.append("high")
        newCol.append(2)

df["Agg_level_str"] = newColStr
df["Agg_level_int"] = newCol

df.to_csv('dataset_with_agg_levels.csv',index = False)