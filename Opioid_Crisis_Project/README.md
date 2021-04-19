# BU-Sociology-Opioid-Crisis

We currently have a scraper that extracts all of the URLs of the pages containing words from a list of search words we specified.

We created a scraper to extract the following basic info from a particular campaign:
- title
- organizer
- beneficiary
- date created
- location
- description
- campaign tags
- number of followers
- number of donors
- number of shares
- amount raised compared to total goal (as a percentage)
- number of campaign updates 
- number of campaign comments
- script tag information: charity name (if provided), currency code, donation count, country code, campaign photo URL
- script tag information: beneficiary is charity (T/F), comments enabled (T/F), donations enabled (T/F), campaign is team (T/F), campaign is business (T/F)

ChromeDriver is included, so the user does not have to change to their local path.

# Additional Attributes Generated for Data Analysis

Sentiment Analysis Performed using VADER

VADER (Valence Aware Dictionary for Sentiment Reasoning) is a sentiment analysis model that produces a score pertaining to how neutral, positive, or negative text is and the “intensity” of that sentiment. VADER scores on a scale of -4 to 4 with -4 being text that is extremely negative and 4 being text that is extremely positive. 
- description_positive (score of how positive campaign description is - higher scores = more positive sentiment)
- description_negative (score of how negative campaign description is - lower scores = more negative sentiment)
- description_neutral (score of how neutral campaign description is - scores closer to 0 = more neutral sentiment)
- description_compound (score of overall campaign description sentiment - normalized across neutral, negative, and positive scores)
- title_positive (score of how positive campaign title is - higher scores = more positive sentiment)
- title_negative (score of how negative campaign title is - lower scores = more negative sentiment)
- title_neutral (score of how neutral campaign title is - scores closer to 0 = more neutral sentiment)
- title_compound (score of overall campaign title sentiment - normalized across neutral, negative, and positive scores)


# Data Collection Workflow

Files used to scrape data<br />
gofundme_scrape.py:
- Used to scrape campaigns associated with a key search term from the list of terms provided by our client.<br />

campaign_info_bs4.py:
- Used to scrape specific information for each campaign in urls.csv using both Selenium and BeautifulSoup<br />

data_formatting.py:
- Used to organize our final list of campaigns into the format specified by our client (an Excel file with multiple sheets corresponding to campaigns associated with each keyword and a master Excel sheet with a list of all campaigns)

1) First, collect the appropriate urls that contain any of the specified keywords in gofundme_scrape.py. This file is in the web_scraper folder. If you would like to change the list of keywords, you can change the keywords on line 116. After running the script, you can find the urls in data/urls.csv.

2) Next, collect the list of attributes for each campaign by running campaign_info_bs4.py. This file is also in the web_scraper folder. You can also specify which sections of urls you would like to scrape by specifying the urls indices on line 547. After running the scraper, you should find the list of attributes in /data/campaign_bs4_data.csv. (This is unprocessed data, so we did not upload it to GitHub)

3) If you run campaign_info_bs4.py on different sections of urls, you can merge the results by running merge_filter_csvs.py. This file is in the preprocessing folder. Start by creating a folder containing all of the unmerged data. (The rest of the directions are commented in the file itself)

4) Finally, reformat the data in campaign_bs4_data by running data_formatting.py. This file is in the preprocessing folder. After running the script, you should see an Excel file titled GFM_Data_Final.xlsx, which contains subsheets of campaign data for each keyword and a subsheet of campaign data for all keywords.

5) To generate graphs and visualize results from a logistic regression model predicting campaign success, see the analysis folder-- includes all code used to generate figures for data analysis




