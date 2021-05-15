import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data19 = pd.read_csv('data2019/WorkforceUtilizationSummaryReport2019.csv')
data20 = pd.read_csv('data2020/WorkforceUtilizationSummaryReport2020.csv')

# Creates a dataframe for a year:
df = pd.read_csv("data2020/WorkforceUtilizationSummaryReport202001.csv")
df2 = pd.read_csv("data2020/WorkforceUtilizationSummaryReport202002.csv")
df = df.append(df2)
df2 = pd.read_csv("data2020/WorkforceUtilizationSummaryReport202003.csv")
df = df.append(df2)
df2 = pd.read_csv("data2020/WorkforceUtilizationSummaryReport202004.csv")
df = df.append(df2)
df2 = pd.read_csv("data2020/WorkforceUtilizationSummaryReport202005.csv")
df = df.append(df2)
df2 = pd.read_csv("data2020/WorkforceUtilizationSummaryReport202006.csv")
df = df.append(df2)
df2 = pd.read_csv("data2020/WorkforceUtilizationSummaryReport202007.csv")
df = df.append(df2)
df2 = pd.read_csv("data2020/WorkforceUtilizationSummaryReport202008.csv")
df = df.append(df2)
df2 = pd.read_csv("data2020/WorkforceUtilizationSummaryReport202009.csv")
df = df.append(df2)
df2 = pd.read_csv("data2020/WorkforceUtilizationSummaryReport202010.csv")
df = df.append(df2)
df2 = pd.read_csv("data2020/WorkforceUtilizationSummaryReport202011.csv")
df = df.append(df2)
df2 = pd.read_csv("data2020/WorkforceUtilizationSummaryReport202012.csv")
df = df.append(df2)

df.to_csv("data2020/WorkforceUtilizationSummaryReport2020.csv", index=False)
