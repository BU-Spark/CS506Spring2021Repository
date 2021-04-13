# Author: Yash Jain
# Date: 2021/04/08

import pandas as pd
import re

def cluster_event_desc():
    data = pd.read_csv("../data/event_type_clusterings/SPECIAL_EVENTS")

    event_types = data.DESCRIPTION.unique()
        
    for event_type in event_types:
        df = data[data.DESCRIPTION == event_type]
        y = str(event_type)
        s = re.sub(r"[^a-zA-Z0-9]+", ' ', y)
        str_arr = s.split(' ')
        final_str = '_'.join(str_arr)
        # print(final_str)
        df.to_csv("../data/event_clus_desc/" + final_str, index=False)
    
    return event_types

if __name__ == '__main__':
    print(cluster_event_desc())