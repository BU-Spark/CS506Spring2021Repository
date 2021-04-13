import pandas as pd 
import numpy as np 
import random 
import matplotlib.pyplot as plt
import statistics

data = pd.read_csv('filtered_final_dataset.csv')

# Initial Exploration -- See Look at Race, Rank, and Misconducts of Officers

# Plot of Race of Officers Under Investigation
data['Race'].value_counts().plot(kind='pie')
plt.title("Demographic of Officers Under Investigation")
plt.show()

# Plot of Officer Rank 
data['Rank'].value_counts().plot(kind='pie')
plt.title(" Ranking of Officers Under Investigation")
plt.show()

print(data['TypeOfMisconduct'].value_counts())

"""
There are two types of misconduct - citizen complaint, and internal investigation. Now, we want to see 
whether or not race, ranking, and type  of misconduct have an effect on the amount of contributions 
an officer makes.
"""

# Sum of the total amounts for each officer WITHOUT duplicate dates
sum = {}
total_sum = 0
for n in data['Name'].unique():
    dates = []
    sum[n] = 0
    for d in data.loc[data['Name'] == n, 'Date']:
        if d not in dates:
            dates.append(d)
            s = ((data.loc[(data['Date'] == d )& (data['Name'] == n), 'Amount'].values)[0])
            sum[n] += s
    total_sum += sum[n]
# print(sum)

# Adding correct total contributions to dataset 
data = data.drop_duplicates(subset = ["Name"])
data['Total Amount']= data['Name'].map(sum)
df = data[['Name', 'Race','TypeOfMisconduct','Allegation', 'Date', 'Rank', 'Total Amount']]
# print(df)

# Plot to see Demographic of Officers and the Average Contributions
race1 = []
for race in df.Race:
    for amount in df.loc[data['Race'] == race, 'Total Amount']:
        if race == 'White':
            race1.append(amount)
# print(race1)

race2 = []
for race in df.Race:
    for amount in df.loc[data['Race'] == race, 'Total Amount']:
        if race == 'Hispanic':
            race2.append(amount)

race3 = []
for race in df.Race[0:20]:
    for amount in df.loc[data['Race'] == race, 'Total Amount']:
        if race == 'Black':
            race3.append(amount)

avg1 = np.mean(race1)
avg2 = np.mean(race2)
avg3 = np.mean(race3)

print("Average Amount of Contribution For Officers who are White: ", avg1)
print("Average Amount of Contribution For Officers that are Hispanic: ", avg2)
print("Average Amount of Contribution For Officers that are Black: ", avg3)

fig = plt.figure()
race = ['white', 'Hispanic', 'Black']
amount = [avg1, avg2, avg3]
plt.bar(race, amount)
plt.title("Average Contribution of Each Race of Officer Under Investigation")
plt.show()

"""
From the three races represented on the graph, white officers made the most contributions. Now, we want to see if
the ranking and the type of misconduct are related to race, and contribution amount. 
"""

# Plot of Misconduct and Contribution
# citizen complaint, and internal investigation
"""
0. python notebook tutorial by shelli :)
2. types of misconducts and see if they relate to the amount donated
3. types of misconducts and the ranking 
"""