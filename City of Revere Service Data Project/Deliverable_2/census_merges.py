#%%
from matplotlib.pyplot import axis
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
# %%
#census data with demographics of Revere via block group and tract
demographics_df = gpd.read_file('./shapefiles/acs2019_5yr_B03002_15000US250251708004/acs2019_5yr_B03002_15000US250251708004.shp')
# %%

# %%
#json file with census demographics categories
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

# %%
demographics_df_tracts = demographics_df[:29]
demographics_df_blkgrp = demographics_df[43:-1]

# %%

# %%
df = pd.read_csv('./311census.csv',sep=',')

#%%
df_tracts = df['Tract']
df_blocks = df['Block']


#%%

df = df.drop(['Tract','Block'],axis=1)
# %%
#adds geometry column for all long/lat in 311 data
gdf = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
# %%
groups_merge_df = sjoin(gdf, demographics_df_blkgrp, how='left', op='within')
tracts_merge_df = sjoin(gdf, demographics_df_tracts, how='left', op='within')
# %%

# %%
to_drop = ['index_right', 'geoid','Total:', 'Total: error',
       'Not Hispanic or Latino:', 'Not Hispanic or Latino: error',
       'White alone', 'White alone error', 'Black or African American alone',
       'Black or African American alone error',
       'American Indian and Alaska Native alone',
       'American Indian and Alaska Native alone error', 'Asian alone',
       'Asian alone error', 'Native Hawaiian and Other Pacific Islander alone',
       'Native Hawaiian and Other Pacific Islander alone error',
       'Some other race alone', 'Some other race alone error',
       'Two or more races:', 'Two or more races: error',
       'Two races including Some other race',
       'Two races including Some other race error',
       'Two races excluding Some other race, and three or more races',
       'Two races excluding Some other race, and three or more races error',
       'Hispanic or Latino:', 'Hispanic or Latino: error', 'White alone',
       'White alone error', 'Black or African American alone',
       'Black or African American alone error',
       'American Indian and Alaska Native alone',
       'American Indian and Alaska Native alone error', 'Asian alone',
       'Asian alone error', 'Native Hawaiian and Other Pacific Islander alone',
       'Native Hawaiian and Other Pacific Islander alone error',
       'Some other race alone', 'Some other race alone error',
       'Two or more races:', 'Two or more races: error',
       'Two races including Some other race',
       'Two races including Some other race error',
       'Two races excluding Some other race, and three or more races',
       'Two races excluding Some other race, and three or more races error']


# %%
groups_merge_df = groups_merge_df.drop(columns = to_drop)
# %%
tracts_merge_df =tracts_merge_df.drop(columns = to_drop)
#%%
cols = tracts_merge_df.columns.tolist()
cols = cols[-1:] + cols[:-1]
tracts_merge_df  = tracts_merge_df[cols]


#%%

tract_block_merge_df = sjoin(tracts_merge_df, demographics_df_blkgrp , how='left', op='within')
#%%
to_drop = ['geoid','Total:', 'Total: error',
       'Not Hispanic or Latino:', 'Not Hispanic or Latino: error',
       'White alone', 'White alone error', 'Black or African American alone',
       'Black or African American alone error',
       'American Indian and Alaska Native alone',
       'American Indian and Alaska Native alone error', 'Asian alone',
       'Asian alone error', 'Native Hawaiian and Other Pacific Islander alone',
       'Native Hawaiian and Other Pacific Islander alone error',
       'Some other race alone', 'Some other race alone error',
       'Two or more races:', 'Two or more races: error',
       'Two races including Some other race',
       'Two races including Some other race error',
       'Two races excluding Some other race, and three or more races',
       'Two races excluding Some other race, and three or more races error',
       'Hispanic or Latino:', 'Hispanic or Latino: error', 'White alone',
       'White alone error', 'Black or African American alone',
       'Black or African American alone error',
       'American Indian and Alaska Native alone',
       'American Indian and Alaska Native alone error', 'Asian alone',
       'Asian alone error', 'Native Hawaiian and Other Pacific Islander alone',
       'Native Hawaiian and Other Pacific Islander alone error',
       'Some other race alone', 'Some other race alone error',
       'Two or more races:', 'Two or more races: error',
       'Two races including Some other race',
       'Two races including Some other race error',
       'Two races excluding Some other race, and three or more races',
       'Two races excluding Some other race, and three or more races error']

tract_block_merge_df = tract_block_merge_df.drop(columns = to_drop)

#%%%

cols = tract_block_merge_df.columns.tolist()
cols = cols[1:] + cols[:1]
cols
#%%%
tract_block_merge_df = tract_block_merge_df[cols]

# %%
# %%
tract_block_merge_df.columns = ['Unnamed: 0', 'Complete Address', 'Comments', 'Create Date',
       'Department', 'Department ID', 'District', 'Master Request',
       'Request ID', 'Request Type', 'Latitude', 'Longitude', 'geometry',
       'index_right', 'Block Group', 'Tract']


# %%
export_census_merge = tract_block_merge_df.to_csv('311census_updated.csv')
# %%
