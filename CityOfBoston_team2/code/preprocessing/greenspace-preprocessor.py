import pandas as pd
from pandas import DataFrame
import difflib
import re
import shapefile
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
    dataframe.to_csv(path)
    return

# df = import_data("../../dataset_ignore/Open_Space.csv")

df = read_shapefile("../../dataset_ignore/Open_Space/Open_Space.shp")
print(df.columns)
df = df[['SITE_NAME','ADDRESS','coords','TypeLong','ACRES']]
print("df is \n",df.head())
df['TypeLong'] = similarity_replace(df.TypeLong)
df=df.sort_values(by=['ACRES'], ascending=False)
print('Types are: ', columnValues(df,'TypeLong'))

output_data(df,"../../datasets_clean/open_space_sanitized.csv")