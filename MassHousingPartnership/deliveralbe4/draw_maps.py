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

def add_polygons(polygons, m, popup_text = None, weights=None):
    # if not weights: weights = [-1] * len(polygons)
    for polygon, p, w in zip(polygons, popup_text, weights):
        try:
            geojson = folium.Choropleth(
                geo_data = polygon,
                fill_color = "#FF0000" if w else "#0000FF"
            )
            if p != "-1":
                folium.Popup(p, max_width=1000).add_to(geojson)
            geojson.add_to(m)
        except Exception as e:
            print(e)
            print(type(polygon))
            continue

    
def add_points(points, m, weights=None):
    # TODO: Rewrite empty check
    if weights == None: weights = [0] * len(points)
    for point, w in zip(points, weights):
        folium.Marker(
            location = [point.y, point.x],
            popup=str(w)
        ).add_to(m)

def generate_popup_text(sjoin_df):
    popup_text = []
    for id_, s, ac, uc, ucus, asump, dsm in zip(
        sjoin_df['LOC_ID'], 
        sjoin_df['STYLE_DESC'], 
        sjoin_df['ADD_COUNT'], 
        sjoin_df['USE_CODE'], 
        sjoin_df['COUNT_USECODE'], 
        sjoin_df['ASSUMPTION'],
        sjoin_df['DENSITY_SQMETER']
    ):
        popup_text.append(
            id_ + 
            "<br>" + s + 
            "<br>USE CODE: " + str(uc) + 
            "<br>Address count:" + str(ac) + 
            "<br>Unit count - use code:" + str(ucus) + 
            "<br>Final assumption:" + str(asump) +
            "<br>Density Square meter: " + str(round(dsm, 2)))
    return popup_text

def draw_debug_plot(points, polygons, weights_points=None, popup_polygons=None, weights_polygons=None):
    m = generateBaseMap()
    # add_points(points, m, weights_points)
    add_polygons(polygons, m, popup_polygons, weights_polygons)
    return m

def draw_validation_map(df, city_name, filename=None):
    df_ = df[df['CITY'] == city_name]
    df_ = df_.to_crs("EPSG:4326")
    final_map = draw_debug_plot([], df_['geometry'], popup_polygons=generate_popup_text(df_), weights_polygons=df_['IS_ANOMALY'])
    if filename: 
        filename += city_name + ".html"
        final_map.save(filename)

def draw_debug_heatmap(points, weights, radius=15):
    m = generateBaseMap()
    HeatMap(
        data = [[p.y, p.x, w] for p, w in zip(points, weights)],
        radius = radius,
        max_zoom = 13).add_to(m)
    return m

# Draw anomalies distribution map
def generate_distribution_map(l1, l2, labels, xlim=[-1,100], ylim=[-1,100], filename=None, reg=None):
    plt.style.use('bmh')
    ax1 = plt.subplot()

    l1_, l2_ = [], []
    for x, y in zip(l1, l2):
        if x <=0 or y <=0: continue
        else:
            l1_.append(x)
            l2_.append(y)
    
    ax1.scatter(l1_, l2_, s=10, c='red')

    ax1.set_xlim(xlim)
    ax1.set_ylim(ylim)
    ax1.set_xlabel(labels[0])
    ax1.set_ylabel(labels[1])

    if reg:
        reg_x = [[i] for i in range(100)]
        reg_y = reg.predict(reg_x)
        ax1.plot([x[0] for x in reg_x], [y[0] for y in reg_y])
    # ax1.show()
    if filename:
        plt.savefig(filename)
    


