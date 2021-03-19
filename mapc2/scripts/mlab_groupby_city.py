import pandas as pd
import numpy as np 

filepath = '../data/mlab_2020_with_provider_name.csv' # 'mapc2\data\mlab_2020_with_provider_name.csv'
mLab = pd.read_csv(filepath)

writepath = '../data/mlab_2020_by_city/'

def city_to_csv(city_data, city):
    print('Converting ' + city + ' data to csv')
    city_data.to_csv(writepath + city + '_mlab_2020.csv', index=False)

def group_data_by_city(df, city):
    city_data = df[df['City'] == city]
    # print(city_data.columns)
    city_to_csv(city_data, city)

def _get_all_cities(df):
    cities = df.City.unique()
    return cities

def group_data(df):
    cities = _get_all_cities(df)
    # print(cities)
    for city in cities:
        if type(city) == str:
            group_data_by_city(df, city)
        else:
            print(city)

# mLab.set_index('Index')
group_data(mLab)
# print(mLab.columns)