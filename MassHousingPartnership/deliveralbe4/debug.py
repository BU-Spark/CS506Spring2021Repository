import re
import pandas as pd

import numpy as np

from texttable import Texttable

# count polygons with same MAP_PAR_ID
def count_polygons(polygons):
    p = None
    count = 1
    for polygon in polygons:
        if not p:
            p = polygon
            continue
        if p != polygon:
            p = polygon
            count += 1
    return count

def check_geometry(df, keyword="MAP_PAR_ID"):
    count = 0
    for i, d in df.groupby(keyword):
        # print(i)
        n = count_polygons(d.geometry)
        if n > 1:
            count += 1
    return count

def filter_usecode(s, pattern="^[1]"):
    if re.search(pattern, s):
        return True
    else:
        return False

def check_tag(s1, s2):
    count = 0
    for v in s1:
        if v not in s2:
            count += 1
    return count

def calculate_coverage(df1, df2):
    return round((len(df1.index) / len(df2.index)) * 100, 2)

def process_duplicate_parcel_data(df, keyword="MAP_PAR_ID"):
    room_count_list = []
    geometry_list = []
    id_list = []

    for _, d in df.groupby(keyword):
        room_num_list = d["NUM_ROOMS"]
        geometry = d["geometry"].iloc[0]
        map_par_id = d[keyword][0]
        room_count = 0
        for rn in room_num_list:
            room_count += rn

        room_num_list.append(room_count)
        geometry_list.append(geometry)
        id_list.append(map_par_id)
    
    df_empty = pd.DataFrame({'A' : []})

# Count occurancy of a usecode in dataframe
def count_by_usecode(df, usecode):
    return np.sum(df["USE_CODE"] == usecode)

def check_mix_usecode(df, mix_usecode_set):
    for uc in mix_usecode_set:
        df_1 = df[df['USE_CODE'] == uc]
        for _, df_2 in df_1.groupby('LOC_ID'):
            count_ = len(df_2)
            if count_ > 1:
                print("{}, {}".format(uc, count_))

# Print out usecode classes
def print_use_code_classes(usecode_df):
    index_to_keep = usecode_df.index[[len(v) == 3 for v in usecode_df['USE_CODE']]]
    df_ = usecode_df.loc[index_to_keep]
    print_by_usecode(df_)

def print_usecode_subclass(df, usecode, is_class=True, print_all_desc=True):
    print_by_usecode(get_record_by_usecode(df, usecode, is_class), print_all_desc=print_all_desc)

def print_by_usecode(df, headers=["USE_CODE", "USE_DESC", "COUNT", "INDEX"], print_all_desc = False):
    count = 1
    t = Texttable()
    t.set_cols_dtype(['t'] * len(headers))
    if headers:
        t.add_row(headers)
    for code_, df_ in df.groupby("USE_CODE"):
        # print(type(code_))
        if not print_all_desc:
            t.add_row([code_, df_['USE_DESC'].iloc[0], len(df_), count])
            count += 1
        else:
            for desc in df_['USE_DESC']:
                t.add_row([code_, desc, len(df_), count])
                count += 1
    print(t.draw())

def get_record_by_usecode(df, usecode, is_class=True):
    end = 3
    if not is_class: end = 4
    return df[[v[:end] == usecode if v else False for v in df['USE_CODE']]]

def check_use_code_in_df(df_use_code_set, use_code_set):
    res = set()
    for uc in use_code_set:
        if uc not in df_use_code_set:
            res.add(uc)
    coverage_rate = (len(use_code_set) - len(res))/len(use_code_set)
    print("Coverage rate: {}%".format(round(coverage_rate * 100, 2)))
    return res

def find_use_value_by_keyword(df, style, keyword="STYLE", target="USE_CODE"):
    df_ = df[df[keyword] == style]
    t = Texttable()
    t.set_cols_dtype(['t'] * 2)
    t.add_row([target, 'COUNT'])
    for uc, dff_ in df_.groupby(target):
        t.add_row([uc, len(dff_)])
    print(t.draw())