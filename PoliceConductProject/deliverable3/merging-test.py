import pandas as pd
import numpy as np 


final = pd.read_csv("filtered.csv")
lead = pd.read_csv("LEAD BPD cleaned.csv")

lead.rename()

import datacompy
compare = datacompy.Compare(
final,
lead,
join_columns=['names','NAME'],  #You can also specify a list of columns eg ['policyID','statecode']
)
