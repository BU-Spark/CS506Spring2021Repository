from datetime import datetime
import geopandas as gpd
import pandas as pd
import numpy as np
import re

import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap
from folium.plugins import MarkerCluster

def generateBaseMap(default_location = [42.3601, -71.0589]):
    base_map = folium.Map(location=default_location)
    return base_map

def add_polygons(polygons, m, weights=None):
    # if not weights: weights = [-1] * len(polygons)
    for polygon, w in zip(polygons, weights):
        try:
            geojson = folium.GeoJson(polygon)
            if w != "-1":
                folium.Popup(w, max_width=1000).add_to(geojson)
            geojson.add_to(m)
        except:
            print(type(polygon))
            continue
        # break
    
def add_points(points, m, weights=None):
    # TODO: Rewrite empty check
    if weights == None: weights = [0] * len(points)
    for point, w in zip(points, weights):
        folium.Marker(
            location = [point.y, point.x],
            popup=str(w)
        ).add_to(m)

def draw_debug_plot(points, polygons, weights_points=None, popup_polygons=None):
    m = generateBaseMap()
    add_points(points, m, weights_points)
    add_polygons(polygons, m, popup_polygons)
    return m

def draw_debug_heatmap(points, weights, radius=15):
    m = generateBaseMap()
    HeatMap(
        data = [[p.y, p.x, w] for p, w in zip(points, weights)],
        radius = radius,
        max_zoom = 13).add_to(m)
    return m

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

def join_two_dataset(df_add, df_parcel, keyword="LOC_ID"):
    # df_parcel = df_parcel.drop_duplicates([keyword])
    # start_time = datetime.now()
    df_joined = gpd.sjoin(df_add, df_parcel, how="right", op="within")
    # end_time = datetime.now()
    # print("Join Two Dataset Time cost: %.2fms" %((end_time - start_time).total_seconds() * 1000))

    return count_address(df_joined)

def count_address(df, keyword="LOC_ID"):
    address_count_list = []
    for _, d in df.groupby(keyword):
        address_count_list.append(len(d.index))
    df = df.groupby(keyword).nth(0)
    df["ADD_COUNT"] = address_count_list
    return df

def join_two_dataset_map(df_add, df_parcel, m, keyword="LOC_ID"):
    df_parcel = df_parcel.drop_duplicates([keyword])
    # start_time = datetime.now()
    df_joined = gpd.sjoin(df_add, df_parcel, how="inner", op="within")
    # end_time = datetime.now()
    # print("Join Two Dataset Time cost: %.2fms" %((end_time - start_time).total_seconds() * 1000))
    count_address_map(df_joined, m)

def count_address_map(df, m, keyword="LOC_ID"):
    for name, d in df.groupby(keyword):
        m.update({name: len(d.index)})

def calculate_coverage(df1, df2):
    return round((len(df1.index) / len(df2.index)) * 100, 2)

def check_tag(s1, s2):
    count = 0
    for v in s1:
        if v not in s2:
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