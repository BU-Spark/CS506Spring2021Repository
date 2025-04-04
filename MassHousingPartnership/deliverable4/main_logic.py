import pandas as pd
import geopandas as gpd

from helper import *
from datetime import datetime

# If there are multiple addresses for one centroid id, remove those data with none unit number
# Could be slow
# Verify the code
def get_addresss_list_to_remove(add_df, keyword='CENTROID_ID'):
    index_res = []
    gp = add_df.groupby(keyword)
    for i, (_, df_) in enumerate(gp):
        progress = int(len(gp) / 100)
        if i % (10 * progress) == 0 and i != 0:
            print("Finished {}%".format(i/progress))
        if len(df_) <= 1: continue
        else:
            index_to_drop = df_.index[[v_ is None for v_ in df_['UNIT']]]
            index_res += index_to_drop.tolist()
    return index_res

def clean_addresses(add_df, keyword='CENTROID_ID'):
    indices_to_remove = benchmark(get_addresss_list_to_remove, (add_df, keyword))
    return add_df.drop(indices_to_remove)

def filter_out_residential_parcels(df, res_usecode_set):
    return df[[v[:3] in res_usecode_set if v else False for v in df['USE_CODE']]]

# Count value in dataframes
def count_value_in_df(df, dict_):
    count = 0
    for val in df:
        if val in dict_.keys():
            count += dict_[val]
    return count

## TODO: groupby.apply function may be better here. Need to read and understand API.
def count_parcels(parcel_df, usecode_dict):
    id_ = []
    count_by_usecode = []
    usecode_str = []
    style_desc = []
    geometry_ = []
    area = []
    city_name = []

    gp = parcel_df.groupby("LOC_ID")

    for i, (loc_id_, df_) in enumerate(gp):
        progress = int(len(gp) / 100)
        if i % (10 * progress) == 0 and i != 0:
            print("Finished {}%".format(i/progress))
        # count_temp_style = 0
        style_set = set()
        for style_ in df_["STYLE"]:
            style_set.add(str(style_))
            # if style_ in usecode_dict.keys():
            #     count_temp += usecode_dict[style_]
        
        count_temp_usecode = 0
        usecode_set = set()
        for uc in df_["USE_CODE"]:
            usecode_set.add(str(uc))
            if uc:
                if uc[:3] in usecode_dict.keys():
                    count_temp_usecode += usecode_dict[uc[:3]]
                    continue
                if uc in usecode_dict.keys():
                    count_temp_usecode += usecode_dict[uc]
                    continue
            else:
                count_temp_usecode = -1

        id_.append(loc_id_)
        count_by_usecode.append(count_temp_usecode)
        style_desc.append(compose_string(style_set))
        usecode_str.append(compose_string(usecode_set))
        city_name.append(df_["CITY"].iloc[0])
        area.append(df_["SHAPE_AREA"].iloc[0])
        geometry_.append(df_['geometry'].iloc[0])

    return [id_, city_name, style_desc, count_by_usecode, usecode_str, area, geometry_]

# TODO: Duplicated function. Need to be merged
def count_parcels_by_usecode(parcel_df, usecode_dict):
    count_usecode = []

    for loc_id_, df_ in parcel_df.groupby("LOC_ID"):
        count_temp = 0
        for us in df_["USE_CODE"]:
            if us and us[:-1] in usecode_dict.keys():
                count_temp += usecode_dict[us[:-1]]

        count_usecode.append(count_temp)

    return count_usecode

# Generate new dataframe
# TODO: Need to add verification function. Make sure that geometry value is valid.
def generate_gpd_dataframe(feature_list, feature_names=[]):
    if len(feature_names) < len(feature_list) - 1:
        feature_names = [str(i) for i in range(len(feature_list) - 1)]
    df = pd.DataFrame(list(zip(*feature_list[:-1])), columns=feature_names)
    df['geometry'] = feature_list[-1]

    gdf = gpd.GeoDataFrame(df)
    return gdf

# Join two dataset
def join_two_dataset(df_add, df_parcel, keyword="LOC_ID"):
    # df_parcel = df_parcel.drop_duplicates([keyword])
    # start_time = datetime.now()
    df_joined = gpd.sjoin(df_add, df_parcel, how="right", op="within")
    # end_time = datetime.now()
    # print("Join Two Dataset Time cost: %.2fms" %((end_time - start_time).total_seconds() * 1000))

    return count_address(df_joined)

# Used to count address
# Pretty slow need to update
# Correctness need to be verified
def count_address(df, keyword="LOC_ID"):
    df_ = df.drop_duplicates(subset=[keyword]).copy()
    df_['ADD_COUNT'] = list(df.groupby(['LOC_ID']).size())
    return df_

# Poor implement
def count_address_map(df, m, keyword="LOC_ID"):
    for name, d in df.groupby(keyword):
        m.update({name: len(d.index)})
# Refactor needed.
def join_two_dataset_map(df_add, df_parcel, m, keyword="LOC_ID"):
    df_parcel = df_parcel.drop_duplicates([keyword])
    # start_time = datetime.now()
    df_joined = gpd.sjoin(df_add, df_parcel, how="inner", op="within")
    # end_time = datetime.now()
    # print("Join Two Dataset Time cost: %.2fms" %((end_time - start_time).total_seconds() * 1000))
    count_address_map(df_joined, m)

def join_two_dataset_state_map(parcel_df, address_df_map, keyword="CITY"):
    start_time = datetime.now()
    
    m = {}
    for name, p_df in parcel_df.groupby(keyword):
        start_time_2 = datetime.now()

        a_df = address_df_map[address_df_map["COMMUNITY_NAME"] == name]
        join_two_dataset_map(a_df, p_df, m, "LOC_ID")
        print("%s, cost: %.2dms" %(name, (datetime.now() - start_time_2).total_seconds() * 1000))
        print("res length: %d" %(len(m)))

    end_time = datetime.now()
    print("Time cost: %.2fms" %((end_time - start_time).total_seconds() * 1000))
    return m

# No style yet
def do_assumption(df, parcel_confidence_set, countable_usecode_set):
    count_by_usecode = df['COUNT_USECODE']
    count_by_add = df['ADD_COUNT']
    usecode = df['USE_CODE']

    assumption = []
    anomalies = []

    for i, u in enumerate(usecode):
        uu = u[:3]
        if uu in parcel_confidence_set or u in parcel_confidence_set:
            assumption.append(count_by_usecode[i])
            continue
        if uu not in countable_usecode_set and u not in countable_usecode_set:
            assumption.append(count_by_add[i])
            continue
        if count_by_usecode[i] == count_by_add[i]:
            assumption.append(count_by_usecode[i])
            continue
        # TODO： possibile?
        # Two people live in a two family house?
        # if count_by_add[i] < count_by_usecode[i]:
        #     assumption.append(count_by_add[i])
        #     continue

        assumption.append(-1)
        anomalies.append((count_by_usecode[i], count_by_add[i]))
    return assumption, anomalies

# Update anomaliy values
def update_anomaly(df, anomalies, reg):
    anomalies_list = list(zip(*anomalies))
    predict_value = reg.predict([[x] for x in anomalies_list[0]])
    
    assumption_list = list(df["ASSUMPTION"])
    usecode_count = list(df["COUNT_USECODE"])
    is_anomaly_list = df["IS_ANOMALY"]

    anomaly_count = 0
    for i, (asump, is_anomal, ucc) in enumerate(zip(assumption_list, is_anomaly_list, usecode_count)):
        if is_anomal: 
            temp_res = int(predict_value[anomaly_count][0])
            assumption_list[i] = max(ucc, temp_res)
            anomaly_count += 1
    df['ASSUMPTION'] = assumption_list
