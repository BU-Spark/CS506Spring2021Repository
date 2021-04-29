#%%
from logging import error
from math import nan
from matplotlib.pyplot import axis, title
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
##Datasets needed in order to execute all cells 
demographics_df = pd.read_csv('./demographics_blckgrp.csv')
df = pd.read_csv('./311census_updated_v2.1.csv')



# %%
#Take only blockgroups in Revere
demographics_df_blkgrp = demographics_df[43:-1]
# %%
#transforms dataframe into geopandas dataframe
from shapely import wkt
demographics_df['geometry'] = demographics_df['geometry'].apply(wkt.loads)
gdf = gpd.GeoDataFrame(demographics_df, crs='epsg:4326')

# %%
#hardcoded blockgroups to use in the analysis, taken from other teammates work
blkgrp_race = {'15000US250251707012': ['White', 0.3835051546391753],
 '15000US250251705021': ['White', 0.9887892376681614],
 '15000US250251708002': ['Hispanic or Latino', 0.5574007220216607],
 '15000US250251702004': ['White', 0.7345890410958904],
 '15000US250251706012': ['White', 0.5736079328756675],
 '15000US250251703003': ['White', 0.9659863945578231],
 '15000US250251705022': ['White', 0.7951885565669701],
 '15000US250251708001': ['Hispanic or Latino', 0.5525597269624574],
 '15000US250251707021': ['Hispanic or Latino', 0.6273504273504273],
 '15000US250251701004': ['White', 0.5850945494994438],
 '15000US250251701005': ['White', 0.523038605230386],
 '15000US250251703006': ['White', 0.5903755868544601],
 '15000US250251701003': ['White', 0.6847372810675563],
 '15000US250251706011': ['Hispanic or Latino', 0.46546546546546547],
 '15000US250251703004': ['White', 0.5900621118012422],
 '15000US250251706014': ['Hispanic or Latino', 0.6702194357366771],
 '15000US250251708003': ['White', 0.8193798449612403],
 '15000US250251703001': ['White', 0.5093896713615024],
 '15000US250251705012': ['White', 0.5730994152046783],
 '15000US250251704002': ['White', 0.5648148148148148],
 '15000US250251707022': ['Hispanic or Latino', 0.579033579033579],
 '15000US250251706013': ['White', 0.6246130030959752],
 '15000US250251703005': ['White', 0.8608981380065718],
 '15000US250251707025': ['White', 0.5195369030390738],
 '15000US250251701007': ['Hispanic or Latino', 0.49175824175824173],
 '15000US250251704001': ['White', 0.56625],
 '15000US250251701001': ['White', 0.5103857566765578],
 '15000US250251707024': ['Hispanic or Latino', 0.5144418423106948],
 '15000US250251704003': ['Hispanic or Latino', 0.4407652685798381],
 '15000US250251703007': ['White', 0.9188712522045855],
 '15000US250251701006': ['White', 0.4937428896473265],
 '15000US250251705011': ['White', 0.45107311749727175],
 '15000US250251702002': ['White', 0.564958283671037],
 '15000US250251704004': ['White', 0.4871159563924678],
 '15000US250251701002': ['White', 0.6368876080691642],
 '15000US250251707011': ['White', 0.6987577639751553],
 '15000US250251703002': ['White', 0.4228855721393035],
 '15000US250251708004': ['White', 0.5468036529680366],
 '15000US250251702001': ['White', 0.6933497536945813],
 '15000US250251707023': ['Hispanic or Latino', 0.5071482317531979],
 '15000US250251702003': ['White', 0.5927487352445194]}
 
#%%
#split data into pre-covid, in order to draw comparisons in visauls
covid_df = df[df['Request Type'] == 'COVID'].reset_index()
non_covid_df = df[df['Request Type'] != 'COVID'].reset_index()

# %%
#Counter allows to perform various statistics in the next cells
covid_groups = Counter(covid_df['Geoid_Blckgrp']).most_common()
novid_groups = Counter(non_covid_df['Geoid_Blckgrp']).most_common()

all_groups = list(blkgrp_race.keys())

#%%
#Ensures that all the block groups that will be used are from our dictionary of hard coded blockgroups
new_covid_groups = {}
test1 = list()
test2 = list()
new_novid_groups = {}

for i in range(len(covid_groups)):
    if covid_groups[i][0] in all_groups:
        new_covid_groups[covid_groups[i][0]] = covid_groups[i][1]
        test1.append(covid_groups[i][1])
    else:
        print(covid_groups[i][0])
print()
for j in range(len(novid_groups)):
    if novid_groups[j][0] in all_groups:
        new_novid_groups[novid_groups[j][0]] = novid_groups[j][1]
        test2.append(novid_groups[j][1])
    else:
       print(novid_groups[i][0]) 


#%%
#Get some statistics from Covd related data
percent_311_covid = list()
percent_hispanic_covid = list()

for i in range(len(new_covid_groups)):
    row = list(new_covid_groups.keys()) 
    total_lh = demographics_df[demographics_df['geoid'] == row[i]]['Hispanic or Latino:']
    total_tract = demographics_df[demographics_df['geoid'] == row[i]]['Total:']
    
    try:
        percent_311_covid.append(float(new_covid_groups[row[i]])/covid_df.shape[0])
        percent_hispanic_covid.append(float(total_lh/total_tract))
    except:
        percent_311_covid.append(0)
        print('Error')
#%%
#More statistics from Non COvid related data
percent_311_nocovid = list()
percent_hispanic_nocovid = list()
for i in range(len(new_novid_groups)):
    row = list(new_covid_groups.keys()) 
    total_lh = demographics_df[demographics_df['geoid'] == row[i]]['Hispanic or Latino:']
    total_tract = demographics_df[demographics_df['geoid'] == row[i]]['Total:']
    
    try:
        percent_311_nocovid.append(float(new_novid_groups[row[i]])/non_covid_df.shape[0])
        percent_hispanic_nocovid.append(float(total_lh/total_tract))
    except:
        percent_311_nocovid.append(0)
        print('Error')
#%%
#Create new geopandas data frame in order to map and display statistics
new_df = pd.DataFrame()
for i in range(len(new_covid_groups)):
    temp = list(new_covid_groups.keys())
    row = demographics_df[demographics_df['geoid']==temp[i]]
    new_df = new_df.append(row)

gdf = gpd.GeoDataFrame(new_df, geometry='geometry')
percent_311_covid = np.array(percent_311_covid)
percent_311_nocovid = np.array(percent_311_nocovid)
gdf['311 Covid Percent'] = np.around(percent_311_covid,decimals=4)
gdf['311 Covid Percent'] = gdf['311 Covid Percent']
gdf['311 Nocovid Percent'] = np.around(percent_311_nocovid,decimals=4)
gdf['311 Nocovid Percent'] = gdf['311 Nocovid Percent']
gdf['Hispanic Covid Percent'] = np.around(percent_hispanic_covid,decimals=4)
gdf['Hispanic Covid Percent'] = gdf['Hispanic Covid Percent']
gdf['Hispanic Nocovid Percent'] = np.around(percent_hispanic_nocovid,decimals=4)
gdf['Hispanic Nocovid Percent'] = gdf['Hispanic Nocovid Percent']
# %%
# %%
gdf = gdf.reset_index()
# %%
dom_race = list()
for i in range(gdf.shape[0]):
    row = gdf['geoid'][i]
    dom_race.append(blkgrp_race[row][0])
# %%
gdf['Majority Race/Ethnicity'] = dom_race

# %%
#plotly is used for creating the Cholropleth maps
import plotly.express as px
#%%
gdf = gdf.set_index(gdf['geoid'])
fig = px.choropleth(gdf,
                   geojson=gdf.geometry,
                   locations=gdf.index,
                   color=gdf['311 Covid Percent'],
                   projection='mercator',
                   color_continuous_scale=px.colors.sequential.Redor,
                   title = 'Percent of Covid related 311 Calls by Census Block Group'
                   )
fig.update_geos(fitbounds="locations", visible=False)
#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


# %%

gdf = gdf.set_index(gdf['geoid'])
fig = px.choropleth(gdf,
                   geojson=gdf.geometry,
                   locations=gdf.index,
                   color=gdf['311 Nocovid Percent'],
                   projection='mercator',
                   color_continuous_scale=px.colors.sequential.Redor,
                   title='Percent of Non-Covid 311 Calls by Census Block Group'
                   )
fig.update_geos(fitbounds="locations", visible=False)
#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
# %%

gdf = gdf.set_index(gdf['geoid'])
fig = px.choropleth(gdf,
                   geojson=gdf.geometry,
                   locations=gdf.index,
                   color=gdf['Majority Race/Ethnicity'],
                   projection='mercator',
                   color_continuous_scale=px.colors.sequential.Purp,
                   color_discrete_sequence=px.colors.qualitative.T10
                   ,title='Majority Race/Ethnicity by Census Groups'
                   )
fig.update_geos(fitbounds="locations", visible=False)
#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

# %%
gdf = gdf.set_index(gdf['geoid'])
fig = px.choropleth(gdf,
                   geojson=gdf.geometry,
                   locations=gdf.index,
                   color=gdf['Hispanic Nocovid Percent'],
                   projection='mercator',
                   color_continuous_scale=px.colors.sequential.Purp
                   )
fig.update_geos(fitbounds="locations", visible=False)
#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
# %%

# %%
check_df = pd.read_csv('311census_updated_v2.1.csv')
# %%

# %%

# %%

# %%

# %%


x = ['Census Tract 1708, Block Group 1,0.0358,0.0427',
'Census Tract 1707.02, Block Group 4,0.0173,0.0427',
'Census Tract 1701, Block Group 7 ,0.0243,0.0354',
'Census Tract 1704, Block Group 3 ,0.014,0.0333',
'Census Tract 1708, Block Group 2 ,0.0284,0.0249',
'Census Tract 1707.02, Block Group 3 ,0.0241,0.0215',
'Census Tract 1707.02, Block Group 2 ,0.0316,0.0201',
'Census Tract 1706.01, Block Group 1 ,0.0373,0.0195',
'Census Tract 1707.02, Block Group 1  ,0.0155,0.0161',
'Census Tract 1706.01, Block Group 4  ,0.0278,0.0134 ']
for i in range(len(x)):
    x[i] = x[i].split(',')
x = np.array(x)
x
# %%
x = pd.DataFrame(x,columns=['Tract','Block Group','Percent Non Covid 311','Percent Covid 311'])
# %%
