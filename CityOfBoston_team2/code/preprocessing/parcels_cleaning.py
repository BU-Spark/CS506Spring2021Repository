"""
last modified: 04/07/2021

cleaning for parcels dataset
keeping only residential parcels
"""

#%% packages

from pyproj import Transformer
import pandas as pd


#%% import

print('acquiring data...')
raw_parcel = pd.read_csv('../../dataset_ignore/Parcels_2020.csv',
                         warn_bad_lines=False)
raw_codes = pd.read_csv('../../dataset_ignore/property-assessment.csv')


#%% join and filter

print('joining and filtering data...')
raw = raw_parcel.set_index("PID_LONG").join(raw_codes.set_index("PID"))
residential = raw[raw['PTYPE'].apply(lambda x: x in range(101, 129))]


#%% cleaning up columns

print('cleaning dataframe...')

# saving only id and longitude/latitude
parcels = residential[['OBJECTID','XCOOR','YCOOR', 'ZIPCODE']]
parcels.columns = ['id', 'eastings', 'northings', 'zip']

# removing na values
parcels = parcels.dropna().reset_index(drop = True)


#%% transforming to latitude and longitude wgs84

print('converting coordinates...')

# note epsg is massachusetts crs code
transformer = Transformer.from_crs(crs_from = 'epsg:2249',
                                   crs_to = 'epsg:4326')

# lists of east/north and initial for lat/lon
east = list(parcels.eastings)
north = list(parcels.northings)
latitudes = []
longitudes = []

# saving a couple entries for testing
test = parcels.loc[0:2,:].copy(deep = True)

# transforming
for i in range(len(east)):
    new = transformer.transform(east[i],north[i])
    latitudes.append(new[0])
    longitudes.append(new[1])

# updating dataframe
parcels.eastings = latitudes
parcels.northings = longitudes

# checking first couple entries
test1 = transformer.transform(test.eastings[0],test.northings[0])
test2 = transformer.transform(test.eastings[1],test.northings[1])
test3 = transformer.transform(test.eastings[2],test.northings[2])

if test1 == (parcels.eastings[0],parcels.northings[0]) and \
    test2 == (parcels.eastings[1],parcels.northings[1]) and \
    test3 == (parcels.eastings[2],parcels.northings[2]):
        parcels.columns = ['id', 'lat', 'lon', 'zip']
        print('converted.')
        
else:
    print('improper conversion.')
    

#%% exporting

print('outputting...')

output_path = '../../datasets_clean/parcels_latlon.csv'

# output cleaned and converted data as csv
parcels.to_csv(output_path)
print('done')

#%% visualizing

import folium

print('generating map of parcels...')
base_path = '../maps/parcel_map.html'

# function to generate base map
def generate_base(default_location = [42.3150,-71.0700]):
    base_map = folium.Map(location = default_location,
                          zoom_start = 12,
                          tiles = 'CartoDB positron')
    return base_map

# latitudes and longitudes as lists
latitudes = list(parcels.lat)
longitudes = list(parcels.lon)

# generating map with schools
base = generate_base()

for lat, lon in zip(latitudes, longitudes):
    folium.Circle(
        location = [lat,lon],
        radius = 20,
        color = 'blue',
        fill = True
        ).add_to(base)
    
base.save(base_path)