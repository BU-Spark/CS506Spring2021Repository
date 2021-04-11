#%%
from numpy.core.fromnumeric import size
import pandas as pd
import numpy as np
from collections import Counter

import matplotlib.pyplot as plt
# %%
df = pd.read_csv('40U Tickets 2015-2020.csv',sep=',')
# %%
common_violation = Counter(df['Violation Type']).most_common(6)
# %%
common_violation = np.array(common_violation)
cv = pd.DataFrame(common_violation, columns=['violation', 'violation_count'])

# %%

cv['violation_count'] = cv['violation_count'].astype(int)

# %%

# %%

# %%
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize = ( 22 , 15 )) 
sns.set_theme(style="whitegrid")

sns.barplot(x = 'violation', y ='violation_count' ,data=cv)

plt.xlabel( "Violation" , size = 25 ) 
  
# Set label for y-axis 
plt.ylabel( "Number of Violations" , size = 25 ) 
plt.xticks(rotation=30, horizontalalignment="right",size=20)
# Set title for figure 
plt.title( "Number of Housing Violations by Violation Type" , size = 20 ) 
plt.legend( loc='upper left')
# Display figure 
plt.show() 
# %%

common_locations = Counter(df['Address']).most_common(30)
common_locations
# %%
import folium
import requests 
import json
from math import nan 
# %%
Locations=  list()
Errors = list()
# %%

for i in range(len(common_locations)):
    try:
        street_address = common_locations[i][0]
        city = 'Revere'
        Google_query = "https://maps.googleapis.com/maps/api/geocode/json?address="+street_address+", "+city+" MA&key=AIzaSyD5UAYQMmsDdkUFfjq38Ved2GNt5c2Jy0o"
        Google_request = requests.get(Google_query)
        Google_JSON = Google_request.json()

        Google_coordinates = Google_JSON['results'][0]['geometry']['location']
        lat = Google_coordinates['lat']
        lon = Google_coordinates['lng']
        Locations.append([lat,lon])
    except:
        Locations.append([nan,nan])
        Errors.append(i)
        print('Error')

# %%
base_map = folium.Map(location=[42.408428, -71.011993], zoom_start=13)
#%%



for i in range(0, len(Locations)):
    folium.Marker((Locations[i][0],Locations[i][1]), popup=str(common_locations[i][1]),color = 'red',opacity=1, sticky=True,radius=.1).add_to(base_map)

title_html = '''
            <h3 align="center" style="font-size:20px"><b>{}</b></h3>
            '''.format('Locations of Top 30 Violations')
base_map.get_root().html.add_child(folium.Element(title_html))
base_map

# %%
base_map.save('violations_data.html')
# %%
