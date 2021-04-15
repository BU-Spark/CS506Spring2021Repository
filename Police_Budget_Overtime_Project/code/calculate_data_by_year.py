"""
Author: Joey Cheng
Date: 02-26-2021
"""
import pandas as pd
from over_reported_OT import read_special_events_data

# Extract the data entries that entry[column_name] = code
def extract_data(column_name, code):
    """
    :param column_name: the name of the column, type: string
    :param code: the key looking for
    :return: a length 6 list, each element is a dataframe containing that year's data
    """
    filePaths = ["../data/Special-Events-2015.csv",
                 "../data/Special Events 2015 - present - 2016.csv",
                 "../data/Special Events 2015 - present - 2017.csv",
                 "../data/Special Events 2015 - present - 2018.csv",
                 "../data/Special Events 2015 - present - 2019.csv",
                 "../data/Special Events 2015 - present - 2020.csv"]

    output_data = []

    for path in filePaths:
        data = read_special_events_data(path)
        target_data = data[data[column_name] == code]
        output_data.append(target_data)

    return output_data


def calculate_average_OT(data):
    """
    :param data: list of data in dataframe by year
    :return: length 6 list, each element represents the result of that year
    """
    res = []
    for d in data:
        res.append(d.OTHOURS.mean())
    return res


def calculate_sum_OT(data):
    res = []
    for d in data:
        res.append(d.OTHOURS.sum())
    return res


def calculate_all_average_OT(column_name):
    """
    :param column_name: Name of the column
    :return: type dictionary, key is every key in the column and value is the average OT time in list by year
    """
    # Use 2015 data as key
    original_data = read_special_events_data("../data/Special-Events-2015.csv")
    keys = pd.unique(original_data[column_name])
    res = {}

    for k in keys:
        data = extract_data(column_name, k)
        res[k] = calculate_average_OT(data)

    return res


def calculate_all_sum_OT(column_name):
    """
    :param column_name: Name of the column
    :return: type dictionary, key is every key in the column and value is the sum OT time in list by year
    """
    # Use 2015 data as key
    original_data = read_special_events_data("../data/Special-Events-2015.csv")
    keys = pd.unique(original_data[column_name])
    res = {}

    for k in keys:
        data = extract_data(column_name, k)
        res[k] = calculate_sum_OT(data)

    return res

if __name__ == '__main__':
    # Example of getting one key value
    data = extract_data("NAME", "O'Connor,Paul B")
    #print(calculate_sum_OT(data))

    # Example of getting all the key values for an attribute
    print(calculate_all_sum_OT("OTCODE"))


