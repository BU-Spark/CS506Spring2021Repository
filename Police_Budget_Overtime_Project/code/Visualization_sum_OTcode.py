#-*- coding=utf-8 -*- 
#@Time:2021/2/28 9:36 PM
#@Author:Yichen Mu
#@File:visualization_sum_OTcode.py
#@Software:PyCharm
import matplotlib.pyplot as plt
from calculate_data_by_year import calculate_all_sum_OT, calculate_sum_OT, extract_data

values_OTCODE = calculate_all_sum_OT("OTCODE")
code_list = []
value_list = []  # OT data every year by OTcode
#values_list = []  # 6 lists of OT data by year
years_list = [2015, 2016, 2017, 2018, 2019, 2020]
for key, value in values_OTCODE.items():
    code_list.append(key)
    value_list.append(value)

for i in range(len(value_list)):
    sum=0
    for j in range(len(value_list[i])):
        sum+=value_list[i][j]
    value_list[i]=sum
print(len(value_list),value_list)
plt.bar(range(len(value_list)),value_list,width=0.9,label='OT',tick_label=code_list)
plt.title('2015-2020 total OT sorted by OTCODE')
plt.xticks(rotation=90)
plt.tick_params(axis='x',which='major',labelsize=6)
plt.legend()
plt.savefig('sum_year_OT.png')
plt.show()