import pandas as pd
import numpy as np 

mapc = pd.read_csv('../data/mapc_municipalities.csv')

filepath = '../data/mlab_2020_with_provider_name.csv' # 'mapc2\data\mlab_2020_with_provider_name.csv'
mLab = pd.read_csv(filepath)

writepath = '../data/mlab_2020_by_city/'

def data_to_csv(data, value):
    print('Converting ' + value + ' data to csv')
    data.to_csv(writepath + value + '_mlab_2020.csv', index=False)
    # data.to_csv('../data/mapc_municipalities.csv', index=False)

def group_data_by_value(df, fieldname, value):
    data = df[df[fieldname] == value]
    data_to_csv(data, value)

def _get_all_fieldValues(df, field):
    unique = df[field].unique()
    return unique

def group_data_by_field(df, field):
    unique = _get_all_fieldValues(df, field)
    for value in unique:
        if type(value) == str:
            group_data_by_value(df, field, value)
        else:
            print(value)

def match_data_by_field(df, field, match_df, match_field):
    match = _get_all_fieldValues(match_df, match_field)
    for value in match:
        if type(value) == str:
            group_data_by_value(df, field, value)
        else:
            print(value)

# group_data_by_field(mLab, 'City')
# group_data_by_value(mapc, 'region', 'MAPC')
match_data_by_field(mLab, 'City', mapc, 'municipal')


# print(mapc['muni_upper'].value_counts())
# print(mapc['municipal'].value_counts())