import pandas as pd
from pandas import DataFrame

def import_data(filename):
    data = pd.read_csv(filename, sep=',', usecols = ['DISTRICT','ZonAgg','TypeLong','ACRES','ADDRESS'])
    return data

print(import_data("../../datasets/open_space.csv"))
