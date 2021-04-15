import pandas as pd
import numpy as np
from os import getcwd
from campaign_info_bs4 import reformat_keyword_list


def main():
    raw_data = pd.read_csv(getcwd() + '/data/campaign_bs4_data.csv')  # change this when we finish Selenium scraper
    raw_data.All_Keywords = raw_data.All_Keywords.apply(reformat_keyword_list)

    # separate out each keyword in the 'All_Keywords' lists
    keywords = pd.DataFrame(raw_data.All_Keywords.tolist()).stack()

    # assign indices to all separated keywords to match the index of its url
    keywords.index = keywords.index.droplevel(-1)  

    # Split each row in original data into rows for each keyword it was found in by joining data to separated keyword dataframe
    keywords.name = "Keyword"
    joined_data = raw_data.join(keywords).sort_values(by='URL').reset_index().drop(columns=['index'])

    # place column with individual keywords in second position
    cols = joined_data.columns.tolist()
    cols[1], cols[-1] = cols[-1], cols[1]
    joined_data = joined_data[cols]

    # group by keyword and save campaigns in separate Excel sheets by keyword, then save a sheet with all campaigns
    keyword_groups = joined_data.groupby('Keyword')
    writer = pd.ExcelWriter("/Users/jaydenfont/Desktop/School/Classes/CS506/BU-Sociology-Opioid-Crisis/data/GFM_Data_Test.xlsx", engine='xlsxwriter')
    for keyword, group in keyword_groups:
        group.to_excel(writer, sheet_name=keyword)
    raw_data.to_excel(writer, sheet_name="all_campaigns")
    writer.save()   


if __name__ == '__main__':
    main()