import numpy as np
import pandas as pd
# from pandasql import sqldf

# creat yearly tables
data19 = pd.read_csv('data2019/WorkforceUtilizationSummaryReport2019.csv')
data20 = pd.read_csv('data2020/WorkforceUtilizationSummaryReport2020.csv')
# create the two year file
two_yrs = data20.append(data19)

# Sum by_trade Report,  THESE ARE THE MOST IMPORTANT STATES.  FROM THIS MANY OTHER STATS CAN BE DERIVED.
data19  = data19.groupby([
       'CONSTRUCTION_TRADE', 'CRAFT_LEVEL'
       ], as_index=False).sum().drop(columns=['MONTH','YEAR']).sort_values(by=["CRAFT_LEVEL",'TOTAL_EMPLOYEE'], ascending=False)
data19.to_csv('data2019/WorkforceUtilizationSummaryReport2019by_trade.csv', index=False)
data20 = data20.groupby([
       'CONSTRUCTION_TRADE', 'CRAFT_LEVEL'
       ], as_index=False).sum().drop(columns=['MONTH','YEAR']).sort_values(by=["CRAFT_LEVEL",'TOTAL_EMPLOYEE'], ascending=False)
data20.to_csv('data2020/WorkforceUtilizationSummaryReport2020by_trade.csv', index=False)
two_yrs = two_yrs.groupby([
       'CONSTRUCTION_TRADE', 'CRAFT_LEVEL'
       ], as_index=False).sum().drop(columns=['MONTH','YEAR']).sort_values(by=["CRAFT_LEVEL",'TOTAL_EMPLOYEE'], ascending=False)
two_yrs.to_csv("data_19_20/WorkforceUtilizationSummaryReport20192020by_trade.csv", index=False)

data19_craft_lvl = data19.groupby(['CRAFT_LEVEL']).sum().sort_values(by=["CRAFT_LEVEL",'TOTAL_EMPLOYEE'], ascending=False)
data19_craft_lvl['FEMALE_%'] = np.round(data19_craft_lvl['TOTAL_FEMALE']/data19_craft_lvl['TOTAL_EMPLOYEE'] *100)
data19_craft_lvl['MALE_%'] = np.round(data19_craft_lvl['TOTAL_MALE']/data19_craft_lvl['TOTAL_EMPLOYEE'] * 100)
data19_craft_lvl['CAUCASIAN_%'] = np.round(data19_craft_lvl['CAUCASIAN']/data19_craft_lvl['TOTAL_EMPLOYEE'] *100)
data19_craft_lvl['AFRICAN_AMERICAN_%'] = np.round(data19_craft_lvl['AFRICAN_AMERICAN']/data19_craft_lvl['TOTAL_EMPLOYEE'] * 100)
data19_craft_lvl['HISPANIC_%'] = np.round(data19_craft_lvl['HISPANIC']/data19_craft_lvl['TOTAL_EMPLOYEE'] *100)
data19_craft_lvl['ASIAN_%'] = np.round(data19_craft_lvl['ASIAN']/data19_craft_lvl['TOTAL_EMPLOYEE'] * 100)
data19_craft_lvl['NATIVE_AMERICAN_%'] = np.round(data19_craft_lvl['NATIVE_AMERICAN']/data19_craft_lvl['TOTAL_EMPLOYEE'] *100)
data19_craft_lvl['OTHER_%'] = np.round(data19_craft_lvl['OTHER']/data19_craft_lvl['TOTAL_EMPLOYEE'] * 100)
data19_craft_lvl['NOT_SPECIFIED_%'] = np.round(data19_craft_lvl['NOT_SPECIFIED']/data19_craft_lvl['TOTAL_EMPLOYEE'] * 100)

data20_craft_lvl = data20.groupby(['CRAFT_LEVEL']).sum().sort_values(by=["CRAFT_LEVEL",'TOTAL_EMPLOYEE'], ascending=False)
data20_craft_lvl['FEMALE_%'] = np.round(data20_craft_lvl['TOTAL_FEMALE']/data20_craft_lvl['TOTAL_EMPLOYEE'] *100)
data20_craft_lvl['MALE_%'] = np.round(data20_craft_lvl['TOTAL_MALE']/data20_craft_lvl['TOTAL_EMPLOYEE'] * 100)
data20_craft_lvl['CAUCASIAN_%'] = np.round(data20_craft_lvl['CAUCASIAN']/data20_craft_lvl['TOTAL_EMPLOYEE'] *100)
data20_craft_lvl['AFRICAN_AMERICAN_%'] = np.round(data20_craft_lvl['AFRICAN_AMERICAN']/data20_craft_lvl['TOTAL_EMPLOYEE'] * 100)
data20_craft_lvl['HISPANIC_%'] = np.round(data20_craft_lvl['HISPANIC']/data20_craft_lvl['TOTAL_EMPLOYEE'] *100)
data20_craft_lvl['ASIAN_%'] = np.round(data20_craft_lvl['ASIAN']/data20_craft_lvl['TOTAL_EMPLOYEE'] * 100)
data20_craft_lvl['NATIVE_AMERICAN_%'] = np.round(data20_craft_lvl['NATIVE_AMERICAN']/data20_craft_lvl['TOTAL_EMPLOYEE'] *100)
data20_craft_lvl['OTHER_%'] = np.round(data20_craft_lvl['OTHER']/data20_craft_lvl['TOTAL_EMPLOYEE'] * 100)
data20_craft_lvl['NOT_SPECIFIED_%'] = np.round(data20_craft_lvl['NOT_SPECIFIED']/data20_craft_lvl['TOTAL_EMPLOYEE'] * 100)

two_yrs_craft_lvl = two_yrs.groupby(['CRAFT_LEVEL']).sum().sort_values(by=["CRAFT_LEVEL",'TOTAL_EMPLOYEE'], ascending=False)
two_yrs_craft_lvl['FEMALE_%'] = np.round(two_yrs_craft_lvl['TOTAL_FEMALE']/two_yrs_craft_lvl['TOTAL_EMPLOYEE'] *100)
two_yrs_craft_lvl['MALE_%'] = np.round(two_yrs_craft_lvl['TOTAL_MALE']/two_yrs_craft_lvl['TOTAL_EMPLOYEE'] * 100)
two_yrs_craft_lvl['CAUCASIAN_%'] = np.round(two_yrs_craft_lvl['CAUCASIAN']/two_yrs_craft_lvl['TOTAL_EMPLOYEE'] *100)
two_yrs_craft_lvl['AFRICAN_AMERICAN_%'] = np.round(two_yrs_craft_lvl['AFRICAN_AMERICAN']/two_yrs_craft_lvl['TOTAL_EMPLOYEE'] * 100)
two_yrs_craft_lvl['HISPANIC_%'] = np.round(two_yrs_craft_lvl['HISPANIC']/two_yrs_craft_lvl['TOTAL_EMPLOYEE'] *100)
two_yrs_craft_lvl['ASIAN_%'] = np.round(two_yrs_craft_lvl['ASIAN']/two_yrs_craft_lvl['TOTAL_EMPLOYEE'] * 100)
two_yrs_craft_lvl['NATIVE_AMERICAN_%'] = np.round(two_yrs_craft_lvl['NATIVE_AMERICAN']/two_yrs_craft_lvl['TOTAL_EMPLOYEE'] *100)
two_yrs_craft_lvl['OTHER_%'] = np.round(two_yrs_craft_lvl['OTHER']/two_yrs_craft_lvl['TOTAL_EMPLOYEE'] * 100)
two_yrs_craft_lvl['NOT_SPECIFIED_%'] = np.round(two_yrs_craft_lvl['NOT_SPECIFIED']/two_yrs_craft_lvl['TOTAL_EMPLOYEE'] * 100)
#save the craft level files
data19_craft_lvl.to_csv("data2019/WorkforceUtilizationSummaryReport2019appjour.csv", index=False)
data20_craft_lvl.to_csv("data2020/WorkforceUtilizationSummaryReport2020appjour.csv", index=False)
two_yrs_craft_lvl.to_csv("data_19_20/WorkforceUtilizationSummaryReport20192020appjour.csv", index=False)

# data19  = data19 .groupby([
#        'CONSTRUCTION_TRADE', 'CRAFT_LEVEL', 'TOTAL_EMPLOYEE', 'CAUCASIAN',
#        'AFRICAN_AMERICAN', 'HISPANIC', 'ASIAN', 'NATIVE_AMERICAN', 'OTHER',
#        'NOT_SPECIFIED', 'TOTAL_FEMALE', 'TOTAL_MALE',
#        ], as_index=False).sum().drop(columns=['MONTH','YEAR'])
# data19.to_csv('data2019/WorkforceUtilizationSummaryReport2019by_trade.csv', index=False)
# data20 = data20.groupby([
#        'CONSTRUCTION_TRADE', 'CRAFT_LEVEL', 'TOTAL_EMPLOYEE', 'CAUCASIAN',
#        'AFRICAN_AMERICAN', 'HISPANIC', 'ASIAN', 'NATIVE_AMERICAN', 'OTHER',
#        'NOT_SPECIFIED', 'TOTAL_FEMALE', 'TOTAL_MALE',
#        ], as_index=False).sum().drop(columns=['MONTH','YEAR'])
# data20.to_csv('data2020/WorkforceUtilizationSummaryReport2020by_trade.csv', index=False)
# two_yrs = two_yrs.groupby([
#        'CONSTRUCTION_TRADE', 'CRAFT_LEVEL', 'TOTAL_EMPLOYEE', 'CAUCASIAN',
#        'AFRICAN_AMERICAN', 'HISPANIC', 'ASIAN', 'NATIVE_AMERICAN', 'OTHER',
#        'NOT_SPECIFIED', 'TOTAL_FEMALE', 'TOTAL_MALE',
#        ], as_index=False).sum().drop(columns=['MONTH','YEAR'])
# two_yrs.to_csv("data_19_20/WorkforceUtilizationSummaryReport20192020by_trade.csv", index=False)

# ['CONSTRUCTION_TRADE', 'CRAFT_LEVEL', 'TOTAL_EMPLOYEE', 'CAUCASIAN',
#        'AFRICAN_AMERICAN', 'HISPANIC', 'ASIAN', 'NATIVE_AMERICAN', 'OTHER',
#        'NOT_SPECIFIED', 'TOTAL_FEMALE', 'TOTAL_MALE',
#        'HOURS_WORKED_PER_MONTH']

# Reduce columns for ethnicity perspectives and gender perspectives
data19_eth = data19.drop(columns=['TOTAL_FEMALE', 'TOTAL_MALE'])
data20_eth = data20.drop(columns=['TOTAL_FEMALE', 'TOTAL_MALE'])
two_yrs_eth = two_yrs.drop(columns=['TOTAL_FEMALE', 'TOTAL_MALE'])

data19_gen = data19.drop(columns=['CAUCASIAN','AFRICAN_AMERICAN', 'HISPANIC',
       'ASIAN', 'NATIVE_AMERICAN', 'OTHER', 'NOT_SPECIFIED'])

data20_gen = data20.drop(columns=['CAUCASIAN','AFRICAN_AMERICAN', 'HISPANIC',
       'ASIAN', 'NATIVE_AMERICAN', 'OTHER', 'NOT_SPECIFIED'])

two_yrs_gen = two_yrs.drop(columns=['CAUCASIAN','AFRICAN_AMERICAN', 'HISPANIC',
       'ASIAN', 'NATIVE_AMERICAN', 'OTHER', 'NOT_SPECIFIED'])

# Transform Columns to rows
data19_eth = data19_eth.melt(id_vars=['CONSTRUCTION_TRADE','CRAFT_LEVEL'], var_name="Ethnicity", value_name="Ethnicity_Hours")
data20_eth = data20_eth.melt(id_vars=['CONSTRUCTION_TRADE','CRAFT_LEVEL'], var_name="Ethnicity", value_name="Ethnicity_Hours")
two_yrs_eth = two_yrs_eth.melt(id_vars=['CONSTRUCTION_TRADE','CRAFT_LEVEL'], var_name="Ethnicity", value_name="Ethnicity_Hours")

data19_gen = data19_gen.melt(id_vars=['CONSTRUCTION_TRADE','CRAFT_LEVEL'], var_name="Gender", value_name="Gender_Hours")
data20_gen = data20_gen.melt(id_vars=['CONSTRUCTION_TRADE','CRAFT_LEVEL'], var_name="Gender", value_name="Gender_Hours")
two_yrs_gen = two_yrs_gen.melt(id_vars=['CONSTRUCTION_TRADE','CRAFT_LEVEL'], var_name="Gender", value_name="Gender_Hours")

#save the trade files
data19_eth.to_csv("data2019/WorkforceUtilizationSummaryReport2019EthnicAJTrade.csv", index=False)
data20_eth.to_csv("data2020/WorkforceUtilizationSummaryReport2020EthnicAJTrade.csv", index=False)
two_yrs_eth.to_csv("data_19_20/WorkforceUtilizationSummaryReport20192020EthnicAJTrade.csv", index=False)

#save the trade files
data19_gen.to_csv("data2019/WorkforceUtilizationSummaryReport2019GenderAJTrade.csv", index=False)
data20_gen.to_csv("data2020/WorkforceUtilizationSummaryReport2020GenderAJTrade.csv", index=False)
two_yrs_gen.to_csv("data_19_20/WorkforceUtilizationSummaryReport20192020GenderAJTrade.csv", index=False)

# These tables are viewable and some of the columns do will not show up in the stored table.
# data19_eth = data19_eth.groupby(["Ethnicity",'CONSTRUCTION_TRADE','CRAFT_LEVEL']).sum()
# data20_eth = data20_eth.groupby(["Ethnicity",'CONSTRUCTION_TRADE','CRAFT_LEVEL']).sum()
# two_yrs_eth = two_yrs_eth.groupby(["Ethnicity",'CONSTRUCTION_TRADE','CRAFT_LEVEL']).sum()
# two_yrs_eth['Percentage']=two_yrs_eth.div(two_yrs_eth.groupby(["Ethnicity"]).sum(), level="Ethnicity") * 100
# two_yrs_eth.sort_values(by=["Ethnicity",'Percentage'], ascending=False)

data19_gen = data19_gen.groupby(["Gender",'CONSTRUCTION_TRADE','CRAFT_LEVEL'], as_index=False).sum()
data20_gen = data20_gen.groupby(["Gender",'CONSTRUCTION_TRADE','CRAFT_LEVEL'], as_index=False).sum()
two_yrs_gen = two_yrs_gen.groupby(["Gender",'CONSTRUCTION_TRADE','CRAFT_LEVEL'], as_index=False).sum()

data19_gen_craft_lvl = data19_gen.groupby(['Gender', 'CRAFT_LEVEL']).sum()
# data19_gen_craft_lvl['Percentage']=data19_gen_craft_lvl.div(data19_gen.groupby(['Gender']).sum(), level='Gender') * 100

data20_gen_craft_lvl = data20_gen.groupby(['Gender','CRAFT_LEVEL']).sum()
# data20_gen_craft_lvl['Percentage']=data20_gen_craft_lvl.div(data20_gen.groupby(['Gender']).sum(), level='Gender') * 100

two_yrs_gen_craft_lvl = two_yrs_gen.groupby(['Gender','CRAFT_LEVEL']).sum()
# two_yrs_gen_craft_lvl['Percentage']=two_yrs_gen_craft_lvl.div(two_yrs_gen.groupby(['Gender']).sum(),level='Gender')*100
#save the trade files
# data19_gen_craft_lvl.to_csv("data2019/WorkforceUtilizationSummaryReport2019gen_craft_lvl.csv", index=False)
# data20_gen_craft_lvl.to_csv("data2020/WorkforceUtilizationSummaryReport2020gen_craft_lvl.csv", index=False)
# data19_gen_craft_lvl.to_csv("data_19_20/WorkforceUtilizationSummaryReport20192020gen_craft_lvl.csv", index=False)

data19_trade =  data19.groupby(['CONSTRUCTION_TRADE'], as_index=False).sum().sort_values(by='TOTAL_EMPLOYEE', ascending=False)
data19_trade['FEMALE_%'] = np.round(data19_trade['TOTAL_FEMALE']/data19_trade['TOTAL_EMPLOYEE'] *100)
data19_trade['MALE_%'] = np.round(data19_trade['TOTAL_MALE']/data19_trade['TOTAL_EMPLOYEE'] * 100)
data19_trade['CAUCASIAN_%'] = np.round(data19_trade['CAUCASIAN']/data19_trade['TOTAL_EMPLOYEE'] *100)
data19_trade['AFRICAN_AMERICAN_%'] = np.round(data19_trade['AFRICAN_AMERICAN']/data19_trade['TOTAL_EMPLOYEE'] * 100)
data19_trade['HISPANIC_%'] = np.round(data19_trade['HISPANIC']/data19_trade['TOTAL_EMPLOYEE'] *100)
data19_trade['ASIAN_%'] = np.round(data19_trade['ASIAN']/data19_trade['TOTAL_EMPLOYEE'] * 100)
data19_trade['NATIVE_AMERICAN_%'] = np.round(data19_trade['NATIVE_AMERICAN']/data19_trade['TOTAL_EMPLOYEE'] *100)
data19_trade['OTHER_%'] = np.round(data19_trade['OTHER']/data19_trade['TOTAL_EMPLOYEE'] * 100)
data19_trade['NOT_SPECIFIED_%'] = np.round(data19_trade['NOT_SPECIFIED']/data19_trade['TOTAL_EMPLOYEE'] * 100)

data20_trade =  data20.groupby(['CONSTRUCTION_TRADE'], as_index=False).sum().sort_values(by='TOTAL_EMPLOYEE', ascending=False)
data20_trade['FEMALE_%'] = np.round(data20_trade['TOTAL_FEMALE']/data20_trade['TOTAL_EMPLOYEE'] *100)
data20_trade['MALE_%'] = np.round(data20_trade['TOTAL_MALE']/data20_trade['TOTAL_EMPLOYEE'] * 100)
data20_trade['CAUCASIAN_%'] = np.round(data20_trade['CAUCASIAN']/data20_trade['TOTAL_EMPLOYEE'] *100)
data20_trade['AFRICAN_AMERICAN_%'] = np.round(data20_trade['AFRICAN_AMERICAN']/data20_trade['TOTAL_EMPLOYEE'] * 100)
data20_trade['HISPANIC_%'] = np.round(data20_trade['HISPANIC']/data20_trade['TOTAL_EMPLOYEE'] *100)
data20_trade['ASIAN_%'] = np.round(data20_trade['ASIAN']/data20_trade['TOTAL_EMPLOYEE'] * 100)
data20_trade['NATIVE_AMERICAN_%'] = np.round(data20_trade['NATIVE_AMERICAN']/data20_trade['TOTAL_EMPLOYEE'] *100)
data20_trade['OTHER_%'] = np.round(data20_trade['OTHER']/data20_trade['TOTAL_EMPLOYEE'] * 100)
data20_trade['NOT_SPECIFIED_%'] = np.round(data20_trade['NOT_SPECIFIED']/data20_trade['TOTAL_EMPLOYEE'] * 100)

two_yrs_trade = two_yrs.groupby(['CONSTRUCTION_TRADE'], as_index=False).sum().sort_values(by='TOTAL_EMPLOYEE', ascending=False)
two_yrs_trade['FEMALE_%'] = np.round(two_yrs_trade['TOTAL_FEMALE']/two_yrs_trade['TOTAL_EMPLOYEE'] *100)
two_yrs_trade['MALE_%'] = np.round(two_yrs_trade['TOTAL_MALE']/two_yrs_trade['TOTAL_EMPLOYEE'] * 100)
two_yrs_trade['CAUCASIAN_%'] = np.round(two_yrs_trade['CAUCASIAN']/two_yrs_trade['TOTAL_EMPLOYEE'] *100)
two_yrs_trade['AFRICAN_AMERICAN_%'] = np.round(two_yrs_trade['AFRICAN_AMERICAN']/two_yrs_trade['TOTAL_EMPLOYEE'] * 100)
two_yrs_trade['HISPANIC_%'] = np.round(two_yrs_trade['HISPANIC']/two_yrs_trade['TOTAL_EMPLOYEE'] *100)
two_yrs_trade['ASIAN_%'] = np.round(two_yrs_trade['ASIAN']/two_yrs_trade['TOTAL_EMPLOYEE'] * 100)
two_yrs_trade['NATIVE_AMERICAN_%'] = np.round(two_yrs_trade['NATIVE_AMERICAN']/two_yrs_trade['TOTAL_EMPLOYEE'] *100)
two_yrs_trade['OTHER_%'] = np.round(two_yrs_trade['OTHER']/two_yrs_trade['TOTAL_EMPLOYEE'] * 100)
two_yrs_trade['NOT_SPECIFIED_%'] = np.round(two_yrs_trade['NOT_SPECIFIED']/two_yrs_trade['TOTAL_EMPLOYEE'] * 100)
#save the trade files
data19_trade.to_csv("data2019/WorkforceUtilizationSummaryReport2019Trade.csv", index=False)
data20_trade.to_csv("data2020/WorkforceUtilizationSummaryReport2020Trade.csv", index=False)
two_yrs_trade.to_csv("data_19_20/WorkforceUtilizationSummaryReport20192020Trade.csv", index=False)


data19_eth_trade =  data19_eth.groupby(['Ethnicity','CONSTRUCTION_TRADE'], as_index=False).sum()
data20_eth_trade =  data20_eth.groupby(['Ethnicity','CONSTRUCTION_TRADE'], as_index=False).sum()
two_yrs_eth_trade = two_yrs_eth.groupby(['Ethnicity','CONSTRUCTION_TRADE'], as_index=False).sum()
data19_gen_trade =  data19_gen.groupby(['Gender','CONSTRUCTION_TRADE'], as_index=False).sum()
data20_gen_trade =  data20_gen.groupby(['Gender','CONSTRUCTION_TRADE'], as_index=False).sum()
two_yrs_gen_trade = two_yrs_gen.groupby(['Gender','CONSTRUCTION_TRADE'], as_index=False).sum()
#save the ethnicity trade files
data19_eth_trade.to_csv("data2019/WorkforceUtilizationSummaryReport2019EthnicTrade.csv", index=False)
data20_eth_trade.to_csv("data2020/WorkforceUtilizationSummaryReport2020EthnicTrade.csv", index=False)
two_yrs_eth_trade.to_csv("data_19_20/WorkforceUtilizationSummaryReport20192020EthnicTrade.csv", index=False)
#save the gender trade files
data19_gen_trade.to_csv("data2019/WorkforceUtilizationSummaryReport2019GenderTrade.csv", index=False)
data20_gen_trade.to_csv("data2020/WorkforceUtilizationSummaryReport2020GenderTrade.csv", index=False)
two_yrs_gen_trade.to_csv("data_19_20/WorkforceUtilizationSummaryReport20192020GenderTrade.csv", index=False)



# useful commands
# two_yrs_gen_craft_lvl = two_yrs_gen.groupby(['Gender','CRAFT_LEVEL']).agg({'Gender_Hours': 'sum'})
# gender = two_yrs_gen.groupby(['Gender']).agg({'Gender_Hours': 'sum'})
# gender_pct = two_yrs_gen_craft_lvl.groupby(level=0).apply(lambda x: 100 * x /float(x.sum()))
# example of sql with pandas
# q="""SELECT DISTINCT CONSTRUCTION_TRADE, CRAFT_LEVEL FROM data19;"""
# pysqldf = lambda q: sqldf(q, globals())
# a_df = pysqldf(q)

# Creates a dataframe for a year:
# df = pd.read_csv("data2020/WorkforceUtilizationSummaryReport202001.csv")
# df2 = pd.read_csv("data2020/WorkforceUtilizationSummaryReport202002.csv")
# df = df.append(df2)
# df2 = pd.read_csv("data2020/WorkforceUtilizationSummaryReport202003.csv")
# df = df.append(df2)
# df2 = pd.read_csv("data2020/WorkforceUtilizationSummaryReport202004.csv")
# df = df.append(df2)
# df2 = pd.read_csv("data2020/WorkforceUtilizationSummaryReport202005.csv")
# df = df.append(df2)
# df2 = pd.read_csv("data2020/WorkforceUtilizationSummaryReport202006.csv")
# df = df.append(df2)
# df2 = pd.read_csv("data2020/WorkforceUtilizationSummaryReport202007.csv")
# df = df.append(df2)
# df2 = pd.read_csv("data2020/WorkforceUtilizationSummaryReport202008.csv")
# df = df.append(df2)
# df2 = pd.read_csv("data2020/WorkforceUtilizationSummaryReport202009.csv")
# df = df.append(df2)
# df2 = pd.read_csv("data2020/WorkforceUtilizationSummaryReport202010.csv")
# df = df.append(df2)
# df2 = pd.read_csv("data2020/WorkforceUtilizationSummaryReport202011.csv")
# df = df.append(df2)
# df2 = pd.read_csv("data2020/WorkforceUtilizationSummaryReport202012.csv")
# df = df.append(df2)

