import matplotlib
import pandas as pd

df = pd.read_csv("data2/WorkforceUtilizationSummaryReport201901.csv")
df2 = pd.read_csv("data2/WorkforceUtilizationSummaryReport201902.csv")
df = df.append(df2)
df2 = pd.read_csv("data2/WorkforceUtilizationSummaryReport201903.csv")
df = df.append(df2)
df2 = pd.read_csv("data2/WorkforceUtilizationSummaryReport201904.csv")
df = df.append(df2)
df2 = pd.read_csv("data2/WorkforceUtilizationSummaryReport201905.csv")
df = df.append(df2)
df2 = pd.read_csv("data2/WorkforceUtilizationSummaryReport201906.csv")
df = df.append(df2)
df2 = pd.read_csv("data2/WorkforceUtilizationSummaryReport201907.csv")
df = df.append(df2)
df2 = pd.read_csv("data2/WorkforceUtilizationSummaryReport201908.csv")
df = df.append(df2)
df2 = pd.read_csv("data2/WorkforceUtilizationSummaryReport201909.csv")
df = df.append(df2)
df2 = pd.read_csv("data2/WorkforceUtilizationSummaryReport201910.csv")
df = df.append(df2)
df2 = pd.read_csv("data2/WorkforceUtilizationSummaryReport201911.csv")
df = df.append(df2)
df2 = pd.read_csv("data2/WorkforceUtilizationSummaryReport201912.csv")
df = df.append(df2)

df.head(50)

nh = pd.read_csv("data2/WorkforceUtilizationSummaryReportNH201901.csv")
nh1 = pd.read_csv("data2/WorkforceUtilizationSummaryReportNH201902.csv")
nh = nh.append(nh1)
nh1 = pd.read_csv("data2/WorkforceUtilizationSummaryReportNH201903.csv")
nh = nh.append(nh1)
nh1 = pd.read_csv("data2/WorkforceUtilizationSummaryReportNH201904.csv")
nh = nh.append(nh1)
nh1 = pd.read_csv("data2/WorkforceUtilizationSummaryReportNH201905.csv")
nh = nh.append(nh1)
nh1 = pd.read_csv("data2/WorkforceUtilizationSummaryReportNH201906.csv")
nh = nh.append(nh1)
nh1 = pd.read_csv("data2/WorkforceUtilizationSummaryReportNH201907.csv")
nh = nh.append(nh1)
nh1 = pd.read_csv("data2/WorkforceUtilizationSummaryReportNH201908.csv")
nh = nh.append(nh1)
nh1 = pd.read_csv("data2/WorkforceUtilizationSummaryReportNH201909.csv")
nh = nh.append(nh1)
nh1 = pd.read_csv("data2/WorkforceUtilizationSummaryReportNH201910.csv")
nh = nh.append(nh1)
nh1 = pd.read_csv("data2/WorkforceUtilizationSummaryReportNH201911.csv")
nh = nh.append(nh1)
nh1 = pd.read_csv("data2/WorkforceUtilizationSummaryReportNH201912.csv")
nh = nh.append(nh1)

nh.head(50)
df.to_csv("data/WorkforceUtilizationSummaryReport2019.csv", index=False)
nh.to_csv("data/WorkforceUtilizationSummaryReportNH2019.csv", index=False)
type_of_hire = ['Total  Journey Hours', 'Total Apprentice Hours']


df.columns= ['MONTH', 'YEAR', 'PROJECT', 'PROJECT_CODE', 'CONTRACTOR',
       'CONSTRUCTION_TRADE', 'CRAFT_LEVEL', 'TOTAL_EMPLOYEE', 'CAUCASIAN',
       'AFRICAN_AMERICAN', 'HISPANIC', 'ASIAN', 'NATIVE_AMERICAN', 'OTHER',
       'NOT_SPECIFIED', 'TOTAL_FEMALE', 'TOTAL_MALE',
       'HOURS_WORKED_PER_MONTH']

WorkSum = df.groupby(['CRAFT_LEVEL'], as_index=False).sum()
WorkMSum = df.groupby(['CRAFT_LEVEL','MONTH'], as_index=False).sum()
WorkSum = WorkSum.drop(columns=['MONTH', 'YEAR'])
WorkMSum = WorkMSum.drop(columns=['YEAR'])
WorkSum.to_csv("data/WorkforceCraftSummaryReport2019.csv", index=False)
WorkMSum.to_csv("data/WorkforceCraftMonthlySummaryReport2019.csv", index=False)

df1 = df1.T.reset_index()
df1

df1.columns = df1.iloc[0].tolist()
df1 = df1.drop(0)

df1


# %matplotlib
# df1=df[:5]

df1.plot('craft_level',kind = 'bar', figsize=(10,7))

df2 = pd.concat([df1['craft_level'], df1[df1.columns.tolist()[1:]].sum(axis=1) ], axis=1)
df2.columns = ['craft_level', 'total_hours']
df2

df2[:8]

df2[:8].plot('craft_level',kind = 'line', figsize=(10,7))

df3 = df2[8:].set_index('craft_level')
df3.columns = ['']

df3.plot.pie(subplots=True, figsize=(11, 6))

df3 = df2[1:3]
df3.iloc[1,1] = df2[3:8]['TOTAL_EMPLOYEE'].sum()
df3.iloc[1,0] = 'ALL_ETHNS'
df3 = df3.set_index('CRAFT_LEVEL')
# df3.columns = ['']
df3

df3.plot.pie(subplots=True, figsize=(11, 6))
