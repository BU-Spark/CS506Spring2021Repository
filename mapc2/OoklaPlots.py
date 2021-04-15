#!/usr/bin/env python
# coding: utf-8

# In[30]:


import geopandas as gp
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import descartes
import geoplot as gplt
import geoplot.crs as gcrs


# In[38]:


# read shape files
q1 = gp.read_file('./Ookla shape data/2020q1')
q2 = gp.read_file('./Ookla shape data/2020q2')
q3 = gp.read_file('./Ookla shape data/2020q3')
q4 = gp.read_file('./Ookla shape data/2020q4')
ma = gp.read_file('./data/export-gisdata.mapc.ma_municipalities').to_crs(epsg=4326)


# In[57]:


data_2020 = pd.concat([q1,q2,q3,q4])


# In[59]:


ax = gplt.webmap(data_2020, projection=gcrs.WebMercator())
gplt.choropleth(
    data_2020, hue='avg_d_kbps', projection=gcrs.AlbersEqualArea(),
    cmap='Greens', legend=True, ax=ax
)
plt.show()

# In[43]:


# use the location of the centroid of each polygon
data_2020['geometry'] = data_2020['geometry'].centroid


# In[56]:


ax = gplt.webmap(data_2020, projection=gcrs.WebMercator())
gplt.pointplot(data_2020, ax=ax, hue='avg_d_kbps', legend=True)
plt.show()

# In[53]:


ax = gplt.webmap(data_2020, projection=gcrs.WebMercator())
gplt.kdeplot(data_2020[['avg_d_kbps', 'geometry']], n_levels=50, cmap='Reds', thresh=0.05 ,shade=True, ax=ax)
plt.show()

# In[32]:


gplt.choropleth(q1, hue='avg_d_kbps')

