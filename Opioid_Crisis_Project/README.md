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

-- Additional Attributes Generated for Data Analysis--

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
