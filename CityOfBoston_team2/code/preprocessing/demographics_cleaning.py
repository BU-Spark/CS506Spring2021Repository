import pandas as pd

demographics = pd.read_csv('../../dataset_ignore/census/Zip Codes Black Labels/GISDATA.ZIPCODES_POLY.csv')
demographics.drop(columns=['FID', 'objectid', 'state', 'pop10_sqmi', 'pop13_sqmi', 'hse_units', 'vacant', 'owner_occ', 'renter_occ', 'sqmi', 'shape_leng', 'gdb_geomattr_data', 'shape'], inplace=True)
demographics = demographics[demographics['po_name'] == 'Boston']

demographics.to_csv('../../datasets_clean/demographics.csv')
