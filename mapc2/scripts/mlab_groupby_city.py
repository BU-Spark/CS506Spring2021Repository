import pandas as pd
import numpy as np 

mapc = pd.read_csv('../data/tabular_datakeys_muni351.csv')

filepath = '../data/mlab_2020_with_provider_name.csv' # 'mapc2\data\mlab_2020_with_provider_name.csv'
mLab = pd.read_csv(filepath)

writepath = '../data/mlab_2020_by_city/'

def data_to_csv(data, city):
    print('Converting ' + city + ' data to csv')
    data.to_csv(writepath + city + '_mlab_2020.csv', index=False)

def group_data_by_field(df, fieldname, value):
    data = df[df[fieldname] == value]
    # print(city_data.columns)
    data_to_csv(data, value)

def _get_all_fieldValues(df, field):
    unique = df[field].unique()
    return unique

def groupby_field(df, field):
    unique = _get_all_fieldValues(df, field)
    # print(cities)
    for value in unique:
        if type(value) == str:
            group_data_by_field(df, city)
        else:
            print(city)

# mLab.set_index('Index')
group_data(mLab)
# print(mLab.columns)