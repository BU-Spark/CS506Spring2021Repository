# Author: Joey_Cheng
# Date: 2021/4/14

import pandas as pd
from datetime import datetime


def transfer_time_format(time):
    try:
        return datetime.strptime(time, "%d-%b-%y").strftime("%m/%d/%y")
    except ValueError:
        return time


# court_OT = pd.read_csv("../data/court OT data/Court Overtime 2014 - 2019 - 2014.csv")
# court_OT["OTDATE"] = court_OT["OTDATE"].apply(lambda x: transfer_time_format(str(x)))
# print(court_OT["OTDATE"])

def check_collision(court_data, special_event_data):
    count, hours = 0, 0
    for index, row in special_events_data.iterrows():
        # records that on the same day for the same person
        sameday = court_data.loc[(court_data["OTDATE"] == row.OTDATE) & (court_data["NAME"] == row.NAME)]

        if len(sameday) > 0:
            for court_index, court_record in sameday.iterrows():
                # over night
                if int(row.ENDTIME) < int(row.STARTTIME):
                    row.ENDTIME += 2400

                # overlap
                if (int(row.STARTTIME) < int(court_record.STARTTIME) < int(row.ENDTIME)) \
                        or (int(row.STARTTIME) < int(court_record.ENDTIME) < int(row.ENDTIME)):
                    print("OT record:\n", row, "\n")
                    print("Court record:\n", court_record, "\n")
                    print("-" * 60, "\n")
                    count += 1
                    time = [int(row.STARTTIME), int(court_record.STARTTIME), int(row.ENDTIME), int(court_record.ENDTIME)]
                    time.sort()
                    hours += int((time[2] - time[1]) / 100) + float((time[2] - time[1]) % 100) / 60

    return count, hours



if __name__ == '__main__':

    count, hours = 0, 0
    for i in range(2015, 2020):
        print("checking", i, "...\n")
        court_OT_data = pd.read_csv("../data/court OT data/Court Overtime 2014 - 2019 - " + str(i) + ".csv")
        court_OT_data["OTDATE"] = court_OT_data["OTDATE"].apply(lambda x: transfer_time_format(str(x)))

        special_events_data = pd.read_csv("../data/Special-Events-" + str(i) + ".csv")

        new_count, new_hours = check_collision(court_OT_data, special_events_data)
        count += new_count
        hours += new_hours

    print("total counts: ", count)
    print("total hours: ", hours, "\n")

