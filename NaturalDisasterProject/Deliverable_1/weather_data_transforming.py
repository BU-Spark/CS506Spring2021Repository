#!/usr/bin/env python
# coding: utf-8

# In[25]:


import folium
from folium.plugins import HeatMap
import numpy as np
import pandas as pd
import os
current_directory = os.getcwd()


# In[26]:



location=[32.7003, -90.6783]
weather_data = pd.read_csv('/Users/abdullaahrobins/Documents/GitHub/CS506Spring2021Repository/NaturalDisasterProject/Datasets/Tornado_Data_2010-2020.csv')
folium.Map(location=location, zoom_start=3)
heat_df = weather_data[['BEGIN_LAT', 'BEGIN_LON']]
heat_df = heat_df.dropna(axis=0, subset=['BEGIN_LAT','BEGIN_LON'])
# HeatMap(data=weather_data.groupby(['BEGIN_LAT', 'BEGIN_LON']).mean().reset_index().values.tolist(), radius=8, max_zoom=4).add_to(base_map)
# base_map.save('tornado_heat_map.html')


# In[27]:


info = weather_data.info()
state_occ = weather_data['STATE_ABBR'].value_counts()
df = weather_data['STATE_ABBR'].value_counts().rename_axis('states').reset_index(name='counts')


# In[28]:


df.info()


# In[29]:


url = (
    "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
)
state_geo = f"{url}/us-states.json"

m = folium.Map(location=location, zoom_start=3)

folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=df,
    columns=["states", "counts"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Tornado Occurrances",
).add_to(m)

folium.LayerControl().add_to(m)


# In[30]:


m


# In[31]:


heat_df


# In[32]:


heat_data = [[row['BEGIN_LAT'],row['BEGIN_LON']] for index, row in heat_df.iterrows()]
HeatMap(heat_data).add_to(base_map)


# In[33]:


base_map


# In[34]:


base_map.save('heatmap_weather.html')
base_map.save('choropleth_weather.html')


# In[ ]:




