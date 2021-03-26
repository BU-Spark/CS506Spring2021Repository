import pandas as pd
from pandas import DataFrame
import difflib
import re
import shapefile
import math

#https://geospatialtraining.com/tutorial-creating-a-pandas-dataframe-from-a-shapefile/
def read_shapefile(shp_file):
    sf_shape = shapefile.Reader(shp_file)
    fields = [x[0] for x in sf_shape.fields][1:]
    records = [y[:] for y in sf_shape.records()]
    #records = sf_shape.records()
    shps = [s.points for s in sf_shape.shapes()]
    df = pd.DataFrame(columns=fields, data=records)
    df = df.assign(coords=shps)
    return df

# def import_data(filename):
#     data = pd.read_csv(filename, sep=',', usecols = ['SITE_NAME','OWNERSHIP','DISTRICT','ZonAgg','TypeLong','ACRES','ADDRESS','ShapeSTArea','ShapeSTLength'])
#     return data

#https://stackoverflow.com/questions/61858903/remove-duplicate-approximate-word-matching-using-fuzzy-python
def similarity_replace(series):

    reverse_map = {}
    diz_map = {}
    for i,s in series.iteritems():
        diz_map[s] = re.sub(r'[^a-z]', '', s.lower())
        reverse_map[re.sub(r'[^a-z]', '', s.lower())] = s

    best_match = {}
    uni = list(set(diz_map.values()))
    for w in uni:
        best_match[w] = sorted(difflib.get_close_matches(w, uni, n=3, cutoff=0.5), key=len)[0]

    return series.map(diz_map).map(best_match).map(reverse_map)

def columnValues(dataframe, columnName):    
    """
    lists all possible values in a particular column
    """
    return list(set(dataframe[columnName].tolist())) 

def output_data(dataframe,path):
    dataframe.to_csv(path, index = False)
    return

# https://stackoverflow.com/questions/37885798/how-to-calculate-the-midpoint-of-several-geolocations-in-python
def avg_coord(coords):

    x = 0.0
    y = 0.0
    z = 0.0

    for coord in coords:
        latitude = math.radians(coord[0])
        longitude = math.radians(coord[1])

        x += math.cos(latitude) * math.cos(longitude)
        y += math.cos(latitude) * math.sin(longitude)
        z += math.sin(latitude)

    total = len(coords)

    x = x / total
    y = y / total
    z = z / total

    central_longitude = math.atan2(y, x)
    central_square_root = math.sqrt(x * x + y * y)
    central_latitude = math.atan2(z, central_square_root)

    mean_lat = math.degrees(central_latitude)
    mean_long = math.degrees(central_longitude)
    return mean_lat,mean_long
def splitCoords(coords):
    lat = []
    lon = []
    for coord in coords:
        lat.append(coord[0])
        lon.append(coord[1])
    return lat,lon

# df = import_data("../../dataset_ignore/Open_Space.csv")

df = read_shapefile("../../dataset_ignore/Open_Space/Open_Space.shp")
# print(df.columns)
print(df[['coords']].head())
df = df[['SITE_NAME','ADDRESS','coords','TypeLong','ACRES']]
# print("df is \n",df.head())
df['TypeLong'] = similarity_replace(df.TypeLong)
df=df.sort_values(by=['ACRES'], ascending=False)

#creating average coordinates
# df['avg_coord'] = df['coords'].apply(lambda coords: avg_coord(coords))
# df[['lat', 'lon']] = pd.DataFrame(df['avg_coord'].tolist(), index=df.index)

#split coords
df['latlon'] = df['coords'].apply(lambda coords: splitCoords(coords))
df[['lat', 'lon']] = pd.DataFrame(df['latlon'].tolist(), index=df.index)
df.drop(['latlon'], axis=1)
# print('-----')
print(df[['lat','lon']].head())
output_data(df,"../../datasets_clean/open_space_latlon.csv")