"""
last modified: 03/23/2021

a test version of 15-minute area finding code.
uses school data; simulated branches for streets
"""

#%% packages

import pandas as pd
import numpy as np
import os
import folium


#%% importing data

# path to data (osp_recreation_amenities.csv)
osp_recreation_amenities_path = '../../datasets_clean/osp_recreation_amenities.csv'
parcels_path = '../../datasets_clean/parcels_latlon.csv'

# pulling data from csv file(osp_recreation_amenities)
if os.path.exists(osp_recreation_amenities_path):
    print('acquiring data (osp_recreation_amenities)...')
    osp_recreation_amenities = pd.read_csv(osp_recreation_amenities_path, usecols = ['SITE_NAME','lat','lon'])    

# rejects if path has been changed
else:
    raise FileNotFoundError('invalid path to osp_recreation_amenities')
    
# pulling data from csv file (parcels)
if os.path.exists(parcels_path):
    print('acquiring data (parcels)...')
    parcels = pd.read_csv(parcels_path, usecols = [1,2,3])

# rejects if path has been changed
else:
    raise FileNotFoundError('invalid path to parcels')
    

#%% base map

print('generating map of osp_recreation_amenities...')
base_path = 'maps/base_map_os.html'

# function to generate base map
def generate_base(default_location = [42.3150,-71.0700]):
    base_map = folium.Map(location = default_location,
                          zoom_start = 12,
                          tiles = 'CartoDB positron')
    return base_map

# latitudes and longitudes as lists
latitudes = list(osp_recreation_amenities.lat)
longitudes = list(osp_recreation_amenities.lon)

# generating map with osp_recreation_amenities
base = generate_base()

for lat, lon in zip(latitudes, longitudes):
    folium.Circle(
        location = [lat,lon],
        radius = 100,
        color = 'red',
        fill = True,
        weight = 1.5
        ).add_to(base)
    
base.save(base_path)


#%% using l2 distance to approximate 15-minutes

print('finding close-by parcels...')

# 15-minute walking distance in latitude/longitude
limit = 0.007

# initialize column for closenesses
parcels['osp_recreation_amenities'] = np.zeros(parcels.shape[0], dtype=int)
cols = ['lat','lon']

# for each school, find parcels within distance
for lat, lon in zip(latitudes, longitudes):
    # top = lat + limit
    # bottom = lat - limit
    # left = lon + limit
    # right = lon - limit
    
    # # parcels in square limit
    # close = (parcels['lat'] < top) & \
    #         (parcels['lat'] > bottom) & \
    #         (parcels['lon'] < left) & \
    #         (parcels['lon'] > right)
    
    # dataframe with same lat and lon
    amenity = pd.DataFrame(np.zeros((parcels.shape[0],2),
                                    dtype=int),
                           columns = cols)
    amenity.lat = lat
    amenity.lon = lon
    
    # l2 distances
    closeness = np.linalg.norm(amenity[cols].values - parcels[cols].values,
                               axis = 1)
    closeness = pd.Series(closeness)
    
    parcels.osp_recreation_amenities = parcels.osp_recreation_amenities + closeness.apply(lambda x: 1 if x < limit else 0)
    
underserved = parcels[parcels.osp_recreation_amenities == 0]
served = parcels[parcels.osp_recreation_amenities != 0]

none = generate_base()    

for lat, lon in zip(underserved.lat.tolist(), underserved.lon.tolist()):
    folium.Circle(
        location = [lat,lon],
        radius = 50,
        color = 'red',
        fill = True,
        weight = 0,
        fill_opacity = 0.7
        ).add_to(none)
    
for lat, lon in zip(served.lat.tolist(), served.lon.tolist()):
    folium.Circle(
        location = [lat,lon],
        radius = 50,
        color = 'blue',
        fill = True,
        weight = 0,
        fill_opacity = 0.7
        ).add_to(none)
    
none.save('maps/underserved_map_os.html')


#%% example nodes (intersections) - unused for now

# print('generating nodes...')
# nodes_path = 'maps/node_map.html'
# with_nodes = generate_base()

# small = 1

# # amount of extra space around
# if small == 0:
#     print('creating full map...')
#     edge = 0.005
#     split = 5000
# else:
#     print('creating semi-map...')
#     edge = -0.05
#     split = 2000

# # bounds for nodes
# north_bound = round(max(latitudes),2) + edge
# south_bound = round(min(latitudes),2) - edge
# west_bound = round(max(longitudes),2) + edge
# east_bound = round(min(longitudes),2) - edge

# # generating proto-nodes
# # first a grid of possible nodes
# grid = []

# for lat in list(np.linspace(south_bound,north_bound,(split/20))):
#     for lon in list(np.linspace(east_bound,west_bound,(split/20))):
#         grid.append([lat,lon])

# grid = np.array(grid)

# # choosing random nodes to act as intersections
# node_index = np.random.choice(grid.shape[0],
#                               size = split,
#                               replace = False)

# nodes = grid[node_index].tolist()

# for node in nodes:
#     folium.Circle(
#         location = node,
#         radius = 25,
#         color = 'blue',
#         fill = True,
#         fill_opacity = 1
#         ).add_to(with_nodes)
    
# # adding osp_recreation_amenities in range to map and list of nodes
# in_range_lat = filter(lambda x: (x < max(grid[node_index][:,0].tolist())) and \
#                              (x > min(grid[node_index][:,0].tolist())),
#                    latitudes)
# in_range_lon = filter(lambda x: (x < max(grid[node_index][:,1].tolist())) and \
#                              (x > min(grid[node_index][:,1].tolist())),
#                    longitudes)
    
# for lat, lon in zip(in_range_lat, in_range_lon):
#     folium.Circle(
#         location = [lat,lon],
#         radius = 100,
#         color = 'red',
#         fill = True,
#         weight = 1.5,
#         fill_opacity = 0.6
#         ).add_to(with_nodes)
    
#     nodes.append([lat,lon])

# with_nodes.save(nodes_path)


#%% connection matrix for proto nodes - in progress

# connections = pd.DataFrame(np.zeros(shape=(len(nodes),len(nodes))))
























