"""
count_event_clus_desc_records.py

Counts/plots number of records in each file in /event_clus_desc
"""

import pandas as pd
import matplotlib.pyplot as plt

def plot_records():

    # List of cluster descriptions
    desc = ['BAA_BOSTON_MARATHON',
    'BFS_EVENT_ACTIVITY',
    'BRIGHTON_DAY_PARADE',
    'CARIBBEAN_CARNIVAL',
    'CHINESE_NEW_YEAR',
    'DYKE_MARCH',
    'EVACUATION_DAY_PARAD',
    'FIRST_NIGHT',
    'GREEK_INDEP_DAY_PARA',
    'HAITIAN_AMER_UNITY_P',
    'HALLOWEEN_COVERAGE',
    'INDEPENDENCE_DAY',
    'MASS_MELNEA',
    'NUISANCE_PATROL',
    'STATE_OF_THE_CITY_AD',
    'TD_GARDEN_EVENTS']

    # List counting number of records in each cluster
    rec = []
    rec.append(pd.read_csv('../data/event_clus_desc/BAA_BOSTON_MARATHON').shape[0])
    rec.append(pd.read_csv('../data/event_clus_desc/BFS_EVENT_ACTIVITY').shape[0])
    rec.append(pd.read_csv('../data/event_clus_desc/BRIGHTON_DAY_PARADE').shape[0])
    rec.append(pd.read_csv('../data/event_clus_desc/CARIBBEAN_CARNIVAL').shape[0])
    rec.append(pd.read_csv('../data/event_clus_desc/CHINESE_NEW_YEAR').shape[0])
    rec.append(pd.read_csv('../data/event_clus_desc/DYKE_MARCH').shape[0])
    rec.append(pd.read_csv('../data/event_clus_desc/EVACUATION_DAY_PARAD').shape[0])
    rec.append(pd.read_csv('../data/event_clus_desc/FIRST_NIGHT').shape[0])
    rec.append(pd.read_csv('../data/event_clus_desc/GREEK_INDEP_DAY_PARA').shape[0])
    rec.append(pd.read_csv('../data/event_clus_desc/HAITIAN_AMER_UNITY_P').shape[0])
    rec.append(pd.read_csv('../data/event_clus_desc/HALLOWEEN_COVERAGE').shape[0])
    rec.append(pd.read_csv('../data/event_clus_desc/INDEPENDENCE_DAY').shape[0])
    rec.append(pd.read_csv('../data/event_clus_desc/MASS_MELNEA').shape[0])
    rec.append(pd.read_csv('../data/event_clus_desc/NUISANCE_PATROL').shape[0])
    rec.append(pd.read_csv('../data/event_clus_desc/STATE_OF_THE_CITY_AD').shape[0])
    rec.append(pd.read_csv('../data/event_clus_desc/TD_GARDEN_EVENTS').shape[0])

    # Store lists in dictionary, sort
    d = dict(zip(desc, rec))
    d_sort = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}

    fig, axes = plt.subplots(figsize=(17, 10))

    # Plot results, save to file
    plt.barh(list(d_sort.keys()), list(d_sort.values()))

    for index, value in enumerate(d_sort.values()):
        plt.text(value, index, str(value))

    plt.title('Number of Records in Each \'event_clus_desc\' Cluster')
    plt.ylabel('Cluster Name')
    plt.xlabel('# of Records')
    plt.savefig("../img/count_event_clus_desc_records.png", bbox_inches='tight')
    plt.show()
    

plot_records()