# %%
from matplotlib.pyplot import axis
from numpy.core.shape_base import block
import pandas as pd
import numpy as np
from collections import Counter
#Imports needed for spatial merge of data
import shapely
from shapely.geometry import shape, mapping
import geopandas as gpd
from geopandas.tools import sjoin
import json
import folium
from folium.plugins import HeatMap
#%%
demographics_df = gpd.read_file('./shapefiles/acs2019_5yr_B03002_15000US250251708004/acs2019_5yr_B03002_15000US250251708004.shp')
df = pd.read_csv('./311census_updated.csv')

with open('./shapefiles/metadata.json') as f:
    data = list(json.load(f).items())
data = data[1][1]['B03002']['columns']


cols = []
for i in data:
    cols += ([data[i]['name']])
cols
cols2 = ['geoid', 'name']
for i in cols:
    cols2 += [i]
    cols2 += [i + ' error']

cols2.append('geometry')
cols2
# %%
#give columns names based on json file
demographics_df.columns = cols2
#%%
#split data into pre-covid, in order to draw comparisons in visauls
covid_df = df[df['Request Type'] == 'COVID']
non_covid_df = df[df['Request Type'] != 'COVID']
#%%
#will use Tracts to map data from 311 to demographics
tracts = Counter(df.Tract).most_common()
tracts = tracts[:11]+tracts[12:]
tracts = tracts[:10]
tracts 
#%%

percent_311 = list()

for i in range(len(tracts)):
    row = demographics_df[demographics_df['name'] == tracts[i][0]]['Total:']

    try:
        percent_311.append(float(row))

    except:
        percent_311.append(0)

#%%
new_df = pd.DataFrame()
for i in range(len(tracts)):

    row = demographics_df[demographics_df['name'] == tracts[i][0]]
    new_df = new_df.append(row)

#%%
percent_311_hispanic = list()
for i in range(len(tracts)):
    total_lh = demographics_df[demographics_df['name'] == tracts[i][0]]['Hispanic or Latino:']
    total = demographics_df[demographics_df['name'] == tracts[i][0]]['Total:']
    try:
        percent_311_hispanic.append(float(total_lh))

    except:
        percent_311_hispanic.append(0)
#%%
gdf = gpd.GeoDataFrame(new_df, geometry='geometry')
percent_311 = np.array(percent_311)
gdf['311 Percent'] = np.around(percent_311,decimals=4)
gdf['311 Percent'] = gdf['311 Percent'].astype(str)
# %%
#################################################### Maps #############################################################
#Generates Base Map with Tracts Groups
def generateBaseMap(default_location=[42.408428, -71.011993]):
    base_map = folium.Map(location=default_location, zoom_start=13)
    return(base_map)
base_map=generateBaseMap()
#%%
for _, r in gdf.iterrows():

    sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j, style_function=lambda x: {'fillColor': 'orange', 'fillOpacity':'.2'})
    folium.Popup(r['HL Percent']).add_to(geo_j)
    geo_j.add_to(base_map)
# %%

base_map
# %%
###Function to generate maps
###what parameters do i want, shape_file, geometry column name, type of map, 

# %%
base_map.save('Revere_tract_base_percentages.html')

# %%
def generateBaseMap(default_location=[42.408428, -71.011993]):
    base_map = folium.Map(location=default_location, zoom_start=15)
    return(base_map)
base_map=generateBaseMap()
locations = df[['Latitude', 'Longitude']] #add points on map

HeatMap(data= df[['Latitude','Longitude']],radius=14).add_to(base_map)
# %%
for _, r in gdf.iterrows():

    sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j, style_function=lambda x: {'fillColor': 'orange', 'fillOpacity':'.2'})
    folium.Popup(r['311 Percent']).add_to(geo_j)
    geo_j.add_to(base_map)

# %%
base_map.save('Revere_tracts_heatmap_req_by_pop.html')
# %%

# %%

# %%

# %%
def generateBaseMap(default_location=[42.408428, -71.011993]):
    base_map = folium.Map(location=default_location, zoom_start=13)
    return(base_map)
base_map=generateBaseMap()
locations = df[['Latitude', 'Longitude']] #add points on map

locationlist = locations.values.tolist()
for point in range(0, len(locationlist)):
    folium.CircleMarker(locationlist[point], color = 'red',opacity=.3, radius=.1).add_to(base_map)
# %%
for _, r in gdf.iterrows():

    sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j, style_function=lambda x: {'fillColor': 'orange', 'fillOpacity':'.2'})
    folium.Popup(r['HL Percent']).add_to(geo_j)
    geo_j.add_to(base_map)
base_map
# %%
base_map.save('Revere_tracts_dots_percent_hl.html')

# %%
#Covid Comparison Maps
def generateBaseMap(default_location=[42.408428, -71.011993]):
    base_map = folium.Map(location=default_location, zoom_start=15)
    return(base_map)
base_map=generateBaseMap()
locations = covid_df[['Latitude', 'Longitude']] #add points on map

HeatMap(data= covid_df[['Latitude','Longitude']],radius=14).add_to(base_map)

for _, r in blocks_demographics_df.iterrows():

    sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j, style_function=lambda x: {'fillColor': 'orange', 'fillOpacity':'.2'})
    folium.Popup(r['name']).add_to(geo_j)
    geo_j.add_to(base_map)
base_map.save('Revere_covid_heatmap.html')


def generateBaseMap(default_location=[42.408428, -71.011993]):
    base_map = folium.Map(location=default_location, zoom_start=15)
    return(base_map)
base_map=generateBaseMap()
locations = non_covid_df[['Latitude', 'Longitude']] #add points on map

HeatMap(data= non_covid_df[['Latitude','Longitude']],radius=14).add_to(base_map)

for _, r in blocks_demographics_df.iterrows():

    sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j, style_function=lambda x: {'fillColor': 'orange', 'fillOpacity':'.2'})
    folium.Popup(r['name']).add_to(geo_j)
    geo_j.add_to(base_map)
base_map.save('Revere_before_covid_heatmap.html')

# %%
#Generates Base Map with Block Groups
def generateBaseMap(default_location=[42.408428, -71.011993]):
    base_map = folium.Map(location=default_location, zoom_start=13)
    return(base_map)
base_map=generateBaseMap()
for _, r in tracts_demographics_df.iterrows():

    sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j, style_function=lambda x: {'fillColor': 'orange', 'fillOpacity':'.2'})
    folium.Popup(r['name']).add_to(geo_j)
    geo_j.add_to(base_map)

# %%
base_map.save('Revere_tracts_base.html')
# %%
def generateBaseMap(default_location=[42.408428, -71.011993]):
    base_map = folium.Map(location=default_location, zoom_start=13)
    return(base_map)
base_map=generateBaseMap()
locations = df[['Latitude', 'Longitude']] #add points on map

locationlist = locations.values.tolist()
for point in range(0, len(locationlist)):
    folium.CircleMarker(locationlist[point], color = 'red',opacity=.3, radius=.1).add_to(base_map)
# %%
for _, r in gdf.iterrows():

    sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j, style_function=lambda x: {'fillColor': 'orange', 'fillOpacity':'.2'})
    folium.Popup(r['name']).add_to(geo_j)
    geo_j.add_to(base_map)
base_map
# %%
base_map.save('Revere_tracts_dots_name.html')
#%%



tracts = np.array(tracts[:10])
for i in range(len(tracts)):
    tracts[i][1] = float(tracts[i][1])
    tracts[i][0] = tracts[i][0][:-13]
cv = pd.DataFrame(tracts, columns=['Tract', 'Number of 311 Calls'])
cv['Number of 311 Calls'] = cv['Number of 311 Calls'].astype(float)
#%%
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize = ( 22 , 15 )) 
sns.set_theme(style="whitegrid")

sns.barplot(x = 'Tract', y ='Number of 311 Calls' ,data=cv)

plt.xlabel( "Tract" , size = 15 ) 
  
# Set label for y-axis 
plt.ylabel( "Number of 311 Calls" , size = 15 ) 
  
# Set title for figure 
plt.title( "Number of 311 Calls by Tract  (10 Most Common)" , size = 20 ) 
  
# Display figure 
plt.show() 
# %%

# %%

# %%

# %%

# %%
