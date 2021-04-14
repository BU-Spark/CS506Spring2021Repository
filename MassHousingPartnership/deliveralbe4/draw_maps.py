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
                fill_color = "#FF0000" if w == -1 else "#0000FF"
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

def draw_debug_plot(points, polygons, weights_points=None, popup_polygons=None, weights_polygons=None):
    m = generateBaseMap()
    # add_points(points, m, weights_points)
    add_polygons(polygons, m, popup_polygons, weights_polygons)
    return m

def draw_debug_heatmap(points, weights, radius=15):
    m = generateBaseMap()
    HeatMap(
        data = [[p.y, p.x, w] for p, w in zip(points, weights)],
        radius = radius,
        max_zoom = 13).add_to(m)
    return m

def generate_distribution_map(l1, l2, labels, xlim=[-1,100], ylim=[-1,100], filename=None):
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
    # ax1.show()
    if filename:
        plt.savefig(filename)