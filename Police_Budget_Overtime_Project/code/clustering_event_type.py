# Author: Yash Jain
# Date: 2021/3/22

import pandas as pd
import re

def cluster_event_types():
    for y in range(15, 21):
        event_types = []
        data = pd.read_csv("../data/Special-Events-20" + str(y) + ".csv")

        event_types = data.CHARGED.unique()
        
        for event_type in event_types:
            df = data[data.CHARGED == event_type]
            y = str(event_type)
            s = re.sub(r"[^a-zA-Z0-9]+", ' ', y)
            str_arr = s.split(' ')
            final_str = '_'.join(str_arr)
            # print(final_str)
            df.to_csv("../data/event_type_clusterings/" + final_str, index=False)
    
    return event_types

if __name__ == '__main__':
    print(cluster_event_types())