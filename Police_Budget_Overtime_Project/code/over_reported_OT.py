"""
Author: Joey Cheng
Date: 02-26-2021
"""

# Calculate the difference between reported OT and real work time in minute format

import pandas as pd

def read_special_events_data(filePath):
    data = pd.read_csv(filePath, converters={
        'STARTTIME': lambda x: str(x),
        'ENDTIME': lambda x: str(x)
    })

    transform_time_data(data)

    return data


# Transform STARTTIME and ENDTIME to timedelta
def transform_time_data(data):
    data["STARTTIME"] = pd.to_datetime(data["STARTTIME"], format='%H%M')
    data["ENDTIME"] = pd.to_datetime(data["ENDTIME"], format='%H%M')

    return


# Return the OT based on STARTTIME and ENDTIME
# Return type: pd.Series with result in minutes format
def calculate_OT(data):
    OT = (data.ENDTIME - data.STARTTIME).astype('timedelta64[m]')
    return OT.apply(lambda x: x + 1440 if x < 0 else x)


# Return the sum of over reported OT (reported OT - real OT)
def calculate_over_reported(filePath):
    data = read_special_events_data(filePath)
    OT = calculate_OT(data)
    reported_OT = data.OTHOURS.apply(lambda x: x * 60)

    return (reported_OT - OT).sum()


if __name__ == '__main__':
    diff_2015 = calculate_over_reported("../data/Special-Events-2015.csv")
    diff_2016 = calculate_over_reported("../data/Special Events 2015 - present - 2016.csv")
    diff_2017 = calculate_over_reported("../data/Special Events 2015 - present - 2017.csv")
    diff_2018 = calculate_over_reported("../data/Special Events 2015 - present - 2018.csv")
    diff_2019 = calculate_over_reported("../data/Special Events 2015 - present - 2019.csv")
    diff_2020 = calculate_over_reported("../data/Special Events 2015 - present - 2020.csv")
    print(diff_2015, diff_2016, diff_2017, diff_2018, diff_2019, diff_2020)



