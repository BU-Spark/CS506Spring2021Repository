# %%
from logging import error
from math import nan
from matplotlib.pyplot import axis
from numpy.core.shape_base import block
from numpy.lib.shape_base import tile
import pandas as pd
import numpy as np
from collections import Counter
#Imports needed for spatial merge of data
import shapely
from shapely.geometry import geo, shape, mapping
import geopandas as gpd
from geopandas.tools import sjoin
import json
import folium
from folium.plugins import HeatMap
#%%
demographics_df = gpd.read_file('./shapefiles/acs2019_5yr_B03002_15000US250251708004/acs2019_5yr_B03002_15000US250251708004.shp')
df = pd.read_csv('./311census_updated_v2.1.csv')

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

# %%
#give columns names based on json file
demographics_df.columns = cols2
#%%
#split data into pre-covid, in order to draw comparisons in visauls
covid_df = df[df['Request Type'] == 'COVID'].reset_index()
non_covid_df = df[df['Request Type'] != 'COVID'].reset_index()
#%%
#will use top ten Tracts to create maps/other tracts are not in Revere. 
covid_tracts = Counter(covid_df.Tract).most_common(10)
non_covid_tracts = Counter(non_covid_df.Tract).most_common(10)

# %%

total_pop = 0
for i in range(len(covid_tracts)):
    total = float(demographics_df[demographics_df['name'] == covid_tracts[i][0]]['Total:'])
    print(float(total))
    try:
        total_pop += total
    except:
        total_pop += 0
        #print("error")
#%%
#Get some statistics from our data
percent_311_covid = list()
percent_hispanic_covid = list()

for i in range(len(covid_tracts)):
    row = covid_tracts[i][1]
    total_lh = demographics_df[demographics_df['name'] == covid_tracts[i][0]]['Hispanic or Latino:']
    total_tract = demographics_df[demographics_df['name'] == covid_tracts[i][0]]['Total:']

    try:
        percent_311_covid.append(float(row)/covid_df.shape[0])
        percent_hispanic_covid.append(float(total_lh/total_tract))
    except:
        percent_311_covid.append(0)
        print('Error')
#%%
percent_311_nocovid = list()
percent_hispanic_nocovid = list()

for i in range(len(covid_tracts)):

    for j in range(len(non_covid_tracts)):
        if(non_covid_tracts[j][0] == covid_tracts[i][0]):
            row = non_covid_tracts[j][1]
    total_lh = demographics_df[demographics_df['name'] == covid_tracts[i][0]]['Hispanic or Latino:']
    total_tract = demographics_df[demographics_df['name'] == covid_tracts[i][0]]['Total:']

    try:
        percent_311_nocovid.append(float(row)/non_covid_df.shape[0])
        percent_hispanic_nocovid.append(float(total_lh/total_tract))     
    except:
        percent_311_nocovid.append(0)
        print('Error')






#%%
#%%
new_df = pd.DataFrame()
for i in range(len(covid_tracts)):
    row = demographics_df[demographics_df['name']==covid_tracts[i][0]]
    new_df = new_df.append(row)
#%%


#%%

#%%

def generateFoliumMap(location, df, pop_name, type,title_name,points):
    '''
    Takes as input location=lat,long of base map, Geopandas df with geometry columnm, the column name for popups,
    type=base~only shapes, heat~heatmap based on points, dots~map with geometries and points
    title_name = name of map title, points = lat, long] of points highlighted 
    '''
    base_map = folium.Map(location=location, zoom_start=13)
    if(type == 'blank'):
        for _, r in df.iterrows():
            sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
            geo_j = sim_geo.to_json()
            geo_j = folium.GeoJson(data=geo_j, style_function=lambda x: {'fillColor': 'orange', 'fillOpacity':'.2'})
            folium.Popup(r[str(pop_name)],parse_html=True,sticky=True).add_to(geo_j)
            geo_j.add_to(base_map)    
    elif(type== 'heat'):
        locations = points #add points on map
        HeatMap(data= locations.values.tolist(),radius=14).add_to(base_map)
    elif(type == 'dots'):
        locations = points
        locationlist = locations.values.tolist()
        for point in range(0, len(locationlist)):
            folium.CircleMarker(locationlist[point], color = 'red',opacity=.3, radius=.1).add_to(base_map)
        for _, r in df.iterrows():
            sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
            geo_j = sim_geo.to_json()
            geo_j = folium.GeoJson(data=geo_j, style_function=lambda x: {'fillColor': 'orange', 'fillOpacity':'.2'})
            folium.Popup(r[str(pop_name)],parse_html=True,sticky=True).add_to(geo_j)
            geo_j.add_to(base_map)  
    title_html = '''
             <h3 align="center" style="font-size:20px"><b>{}</b></h3>
             '''.format(title_name)
    base_map.get_root().html.add_child(folium.Element(title_html))

    return base_map
#%%

#%%
gdf = gpd.GeoDataFrame(new_df, geometry='geometry')
percent_311_covid = np.array(percent_311_covid)
percent_311_nocovid = np.array(percent_311_nocovid)
gdf['311 Covid Percent'] = np.around(percent_311_covid,decimals=4)
gdf['311 Covid Percent'] = gdf['311 Covid Percent'].astype(str)
gdf['311 Nocovid Percent'] = np.around(percent_311_nocovid,decimals=4)
gdf['311 Nocovid Percent'] = gdf['311 Nocovid Percent'].astype(str)
gdf['Hispanic Covid Percent'] = np.around(percent_hispanic_covid,decimals=4)
gdf['Hispanic Covid Percent'] = gdf['Hispanic Covid Percent'].astype(str)
gdf['Hispanic Nocovid Percent'] = np.around(percent_hispanic_nocovid,decimals=4)
gdf['Hispanic Nocovid Percent'] = gdf['Hispanic Nocovid Percent'].astype(str)
#%%
covid_dots = generateFoliumMap([42.408428, -71.011993], gdf,'311 Covid Percent','dots','City of Revere Percent 311 Calls by Tract, During COVID-19',covid_df[['Latitude','Longitude']])
covid_dots.save('covid_dots.html')
#%%
noncovid_dots = generateFoliumMap([42.408428, -71.011993], gdf,'311 Nocovid Percent','dots','City of Revere Percent 311 Calls by Tract, Before COVID-19',non_covid_df[['Latitude','Longitude']])
noncovid_dots.save('noncovid_dots.html')
#%%
base_map = folium.Map(location=[42.408428, -71.011993], zoom_start=13)
locations = covid_df[['Latitude','Longitude']]
locationlist = locations.values.tolist()
for point in range(0, len(locationlist)):
    folium.CircleMarker(locationlist[point], color = 'red',opacity=.3, radius=.1).add_to(base_map)
for _, r in gdf.iterrows():
    sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j, style_function=lambda x: {'fillColor': 'orange', 'fillOpacity':'.2'})
    folium.Popup("{}\nPercent of Pop His/Latino: {} % \n Percent of 311 Calls: {}%".format(r['name'],round(float(r['Hispanic Covid Percent'])*100,4),round(float(r['311 Covid Percent'])*100),4),parse_html=True,sticky=True).add_to(geo_j)
    geo_j.add_to(base_map)  
title_html = '''
        <h3 align="center" style="font-size:20px"><b>{}</b></h3>
        '''.format('City of Revere 311 and Hispanic/Latino by Tract Covid')
base_map.get_root().html.add_child(folium.Element(title_html))

base_map
base_map.save('Deliverable3_covid_dots.html')
# %%

base_map = folium.Map(location=[42.408428, -71.011993], zoom_start=13)
locations = non_covid_df[['Latitude','Longitude']]
locationlist = locations.values.tolist()
for point in range(0, len(locationlist)):
    folium.CircleMarker(locationlist[point], color = 'red',opacity=.3, radius=.1).add_to(base_map)
for _, r in gdf.iterrows():
    sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j, style_function=lambda x: {'fillColor': 'orange', 'fillOpacity':'.2'})
    folium.Popup("{}\nPercent of Pop His/Latino: {} % \n Percent of 311 Calls: {}%".format(r['name'],round(float(r['Hispanic Nocovid Percent'])*100,4),round(float(r['311 Nocovid Percent'])*100),4),parse_html=True,sticky=True).add_to(geo_j)
    geo_j.add_to(base_map)  
title_html = '''
        <h3 align="center" style="font-size:20px"><b>{}</b></h3>
        '''.format('City of Revere 311 and Hispanic/Latino by Tract Non Covid')
base_map.get_root().html.add_child(folium.Element(title_html))

base_map
base_map.save('Deliverable3_noncovid_dots.html')
#%%
#USEFUL CODE FOR EMBEDDING TEXTS INTO MAPS
from folium.features import DivIcon
m = folium.Map([34.0302, -118.2352], zoom_start=13)
folium.map.Marker(
    [34.0302, -118.2352],
    icon=DivIcon(
        icon_size=(150,36),
        icon_anchor=(0,0),
        html='<div style="font-size: 24pt">{}</div>'.format('Tract 0001'),
        )
    ).add_to(m)

# %%

# %% [markdown]



# tracts = np.array(tracts[:10])
# for i in range(len(tracts)):
#     tracts[i][1] = float(tracts[i][1])
#     tracts[i][0] = tracts[i][0][:-13]
# cv = pd.DataFrame(tracts, columns=['Tract', 'Number of 311 Calls'])
# cv['Number of 311 Calls'] = cv['Number of 311 Calls'].astype(float)
# %% [markdown]
# import seaborn as sns
# import matplotlib.pyplot as plt

# plt.figure(figsize = ( 22 , 15 )) 
# sns.set_theme(style="whitegrid")

# sns.barplot(x = 'Tract', y ='Number of 311 Calls' ,data=cv)

# plt.xlabel( "Tract" , size = 15 ) 
  
# Set label for y-axis 
# plt.ylabel( "Number of 311 Calls" , size = 15 ) 
  
# Set title for figure 
# plt.title( "Number of 311 Calls by Tract  (10 Most Common)" , size = 20 ) 
  
# Display figure 
# plt.show() 
# %%


# %%
import plotly.express as px
#%%
df = px.data.election()
geo_df = gpd.GeoDataFrame.from_features(
    px.data.election_geojson()["features"]
).merge(df, on="district").set_index("district")

fig = px.choropleth(geo_df,
                   geojson=geo_df.geometry,
                   locations=geo_df.index,
                   color="Joly",
                   
                   projection="mercator")
fig.update_geos(fitbounds="locations", visible=False)
fig.show()
# %%
gdf = gdf.set_index('name')
# %%

fig = px.choropleth(gdf,
                   geojson=gdf.geometry,
                   locations=gdf.index,
                   color="311 Nocovid Percent",
                   projection='mercator',
                   color_continuous_scale=px.colors.sequential.Redor
                   )
fig.update_geos(fitbounds="locations", visible=False)
#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()




# %%

fig = px.choropleth(gdf,
                   geojson=gdf.geometry,
                   locations=gdf.index,
                   color="311 Covid Percent",
                   projection='mercator',
                   color_continuous_scale=px.colors.sequential.Redor
                   )
fig.update_geos(fitbounds="locations", visible=False)
#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


# %%
