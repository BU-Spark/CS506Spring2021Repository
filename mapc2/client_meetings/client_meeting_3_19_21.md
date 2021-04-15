# Third Meeting (3.19.21)

Third meeting with the client.

Date: 03/19/21


Team 1: Not much progress in terms of code this week

Ryan:
Everrett Community Meeting:
    - Talk about coverage: Looked at actual providers for a few specific addresses

Comprehensive (visualization) of what the FCC says per provider per package: https://public.tableau.com/profile/ryan.kelly4867#!/vizhome/ProviderCosts/Dashboard1

Helpful to have as many data points as possible (though average would be fair)


--------------------------------------

Team 2: 

MLAB: ProviderName: mlab_2020_with_provider_name.csv, split by city.csv: mlab_2020_by_city.csv mlab_avg_groupings_2020

Ookla: labelled by county, but haven't beenable to find that same information for municipalities
    - Polygon shape data:
        https://datacommon.mapc.org/browser/datasets/390

Comcast's concern for MLab vs Ookla: they believe msot of the tests are running on lower tier providers -> pipes they're using after comcast are slower
    - In-house network & pipe after is messing up their speeds
        - vs Ookla (between you and Comcast)
    - MLab : openning one prowser and TCP connection : Is that an accurate test of speed? How representative is this "speed"? Or is it more capacity/other metric?
        - Ryan thinks it a metric of application of speed
    - Timing (shady)

Deliverables for the future: 
    - csv files & interactive maps:
        - median download, upload speed map: by provider (they have for 2020 but could be interesting)
        - monopoly/duapoly: In the last 5 years how many providers have provided speeds over a certain threshold (100 by 100: how many providers are available per municipality for that)
            - 100 by 100: difficult for comcast to reach (upload speeds on copper lines are poor)
    - analysis on:
        - Are there certain places where multiple providers exist but there is a clear disparity?

Identifiable outcomes:
    - Mean speed for mean income *POINT OF INTEREST - Analysis
        - Trying to understand the relationship between the mean upload speed as it correlates with mean income per municipality
        - Income Matching PRIORITY
            - map/scatterplot**
            - What income measurement?? Census avg income
            - Collaborate with Team 1!

Notes from Ryan: 
    - ACS data:
        - Ask by municipality, by <30, 30-70, >70, by income: Do you have internet subscription?
        https://airtable.com/shrEFbGQ2vputfhUM : Look at 'Per capita income table from the Census (ACS)'
            - 8% make over 75k per year but do not have an internet subscription
            - Chart this out; by scatter-plot where we join census data, measures of income on the provider -> avg speeds for that

    - Amount of providers that are listed -> Break down by package & be a little more subjective (More for Team 1)


    - Median Household Income by Tenure (Municipal): https://datacommon.mapc.org/browser/datasets/194
    - Census Data API: Variables in /data/2017/acs/acs5/groups/B25119 - 2019 data: https://api.census.gov/data/2017/acs/acs5/groups/B25119.html
        - May have 2020 data by April

    - Slide deck used to walk through community members about topic : https://slides.com/mapc/everett
        - DSL (~$80/month) - Very bad .. Why do people have it?
        - Hidden click charts (Slide )
        - Everret: 15% No Internet; 8% >75k; <20k (~800 households)


Deliverables Organization:
    - INCOME MATCHING !!


Questions from us:
    - Time History: FCC data (count change from provider over time); uptick in wireless providers for MLab data (2017 T-Mobile hotspots)
        - Categorical by Year

    - Relevance of Everett, Chelsea, Revere, Quincy, Malden
        - Gateway Cities (economic distress) - by race, income, etc - areas of economic potential/growth

Question from Ryan: N/A