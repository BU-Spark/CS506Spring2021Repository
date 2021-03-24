#-*- coding=utf-8 -*- 
#@Time:2021/2/28 10:21 PM
#@Author:Yichen Mu
#@File:Visualization_6_subplot.py
#@Software:PyCharm

import numpy as np
import matplotlib.pyplot as plt
from calculate_data_by_year import calculate_all_sum_OT, calculate_sum_OT, extract_data

values_OTCODE = calculate_all_sum_OT("OTCODE")
code_list = []
value_list = []  # OT data every year by OTcode
values_list = []  # 6 lists of OT data by year
new_values_list=[] # store the top10 OT
new_code_list=[]   # store the top10 OTcode
years_list = [2015, 2016, 2017, 2018, 2019, 2020]
for key, value in values_OTCODE.items():
    code_list.append(key)
    value_list.append(value)
print(code_list)
# Initialize the lists
for i in range(6):
    values_list.append([])
for i in range(6):
    new_code_list.append([])
# Extract OT from the original data which is classified by OTCODE to store them according to the year.
for i in range(6):  # 6 years
    for j in range(len(value_list)):
        values_list[i].append(value_list[j][i])
# Sort the OT in every year to select the top 10 length of OT.
for i in range(len(values_list)):
    new_values_list.append(sorted(values_list[i],reverse=True)[:10])
# Select the OTCODE according to the sorted top10 OT array.
for i in range(len(new_values_list)):
    for j in range(len(new_values_list[i])):
        new_code_list[i].append(code_list[values_list[i].index(new_values_list[i][j])])
#print(new_values_list)
new_values_list=np.array(new_values_list)
#print(type(new_values_list),type(new_values_list[0]))
#print(new_code_list)
fig=plt.figure()
fig.suptitle('Top 10 event types in every year')
ax1=fig.add_subplot(2,3,1)
plt.bar(range(len(new_code_list[0])),new_values_list[0],width=0.9,label='OT',tick_label=new_code_list[0])
plt.title('2015')
plt.xticks(rotation=75)
plt.legend()
ax2=fig.add_subplot(2,3,2)
plt.bar(range(len(new_code_list[1])),new_values_list[1],width=0.9,label='OT',tick_label=new_code_list[1])
plt.title('2016')
plt.xticks(rotation=75)
plt.legend()
ax3=fig.add_subplot(2,3,3)
plt.bar(range(len(new_code_list[2])),new_values_list[2],width=0.9,label='OT',tick_label=new_code_list[2])
plt.title('2017')
plt.xticks(rotation=75)
plt.legend()
ax4=fig.add_subplot(2,3,4)
plt.bar(range(len(new_code_list[3])),new_values_list[3],width=0.9,label='OT',tick_label=new_code_list[3])
plt.title('2018')
plt.xticks(rotation=75)
plt.legend()
ax5=fig.add_subplot(2,3,5)
plt.bar(range(len(new_code_list[4])),new_values_list[4],width=0.9,label='OT',tick_label=new_code_list[4])
plt.title('2019')
plt.xticks(rotation=75)
plt.legend()
ax6=fig.add_subplot(2,3,6)
plt.bar(range(len(new_code_list[5])),new_values_list[5],width=0.9,label='OT',tick_label=new_code_list[5])
plt.title('2020')
plt.xticks(rotation=75)
fig.tight_layout(pad=1.9,w_pad=0.9,h_pad=0.4)
plt.legend()

plt.savefig('every_year_top10_subplots.png')
plt.show()