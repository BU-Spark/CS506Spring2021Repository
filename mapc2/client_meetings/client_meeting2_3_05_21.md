# Second Meeting (3.05.21)

Second meeting with the client.

Date: 03/05/21

Team 1: Heatmap Visualization!

--------------------------------------

Team 2: Aggregated the data from 2020

Oookla data from programmatic access with AWS
    - 4 quarters of data from 2020 to csv (each file is abt 10MB - Manageable)
    - Everydata point is not 1 test -> Aggregation of data - TILE

Columns & Example data:
- quadkey: 0302332121321131
    - a key that identifies the tile
- avg_d_kbps: 141598
    - the average download speed in kilobits per second within the tile
- avg_u_kbps: 56138
    - the average upload speed in kilobits per second within the tile
- avg_lat_ms: 11
    - the average latency of the tests in this tile
- tests: 55
    - the number of tests that contributed to the other values in this tile
- devices: 27
    - the number of unique devices that contributed to the data in this tile
- geometry: 
    - "POLYGON ((-71.1090087890625 42.3504251224346, -71.103515625 42.3504251224346, -71.103515625 42.3463653316019, -71.1090087890625 42.3463653316019, -71.1090087890625 42.3504251224346))"
    - list of latitude/longitude pairs, that collectively form the polygonal shape of this tile
- STATEFP: 25
    - state FIPS code
    - MA: 25
- COUNTYFP: 021
    - county FIPS code
- COUNTYNS: 00606937
    - Another unique county identifier
- GEOID: 25021
    - unique ID for the geographic location of the county
- NAMELSAD: Norfolk County
    - full name of the county


MLAB: (437,000 Rows of data)
    - Trickier because size of the data was so large
    - Pulled 4 example times throughout the day (8-8:30 12-12:30 3-3:30 8-8:30) - Representative set of times
    - Figured that internet broadband speeds do not vary too much throughout the day.
    - Scripts to pull data into csv files of reasonable size
    - Each data point is an individual test, NOT aggregation like Ookla data

Columns & Example data:
- TestTime: 2020-10-01 12:01:22.316165 UTC
    - the time at which the test took place, includes both a date and a time
- IP: TBPhGA==
    - the IP address of the device being tested
- MeanThroughputMbps: 5.924981493972454
    - average broadband throughput in megabits per second. Note that this is different than the download and upload speeds of Ookla, since they are measuring slightly different things.
- MinRTT: 21.283
    - Minimum round trip time, the time it takes to send a signal or data packet and receive back the corresponding acknowledgment
- City: Wellfleet
    - the city in which the test occured
- Latitude: 41.9289
    - latitude location of the test
- Longitude: -70.0186
    - longitude location of the test
- ProviderNumber: 7922
    - the autonomous system number of the nearest server system for the test



Questions Client has:
- How many total tests? Who goes to Ookla vs Google?
- Cambridge vs Quincy asked about broadband access. How representatibe are these tests of the larger area?
Ookla:
- How low of a count are there for a Polygon? (Roughly sized/Couple per size)
- Geography piece: aggregate Polygon
- Municipalities (group-by) could be helpful to compare against MLAB (See what we don't have in MLAB)
- See if Ookla can provide provider number

MLAB: 
- Matching geography to IP is NOT Straightforward
- Times: Windows of 7-7 and then nighttime. (FCC?) Average usage has variation throughout the day.
    Fascinating 
    - Comcast has never exceeded 80/85% even with everyone on Zoom
- Everett: In 2020 compared to prior years: T-Mobile - explosion of wireless MyFi devices - avg speeds (lower & never get to broadband levels)


Links:
https://datacommon.mapc.org/browser/datasets/415 - 


Questions we have:
Ookla:
1. What kind of featurese would you like to have?
    Nice to have grids & coordinates, but MUNICIPAL AGGREGATION
    Need to compare to FCC dataset -> Provider(?)
    Devices? Broader picture of acceess: What is the internet? Device to access internet. How it accesses
        How many devices? What types of devices? What are people using to access the data?
    Ookla only provides speed 
    #Symmetical Speeds - Now we rely on uploads in addition to downloads -> That speed is being requested more and it is NOT symmetrical 25/3
https://my.dish.com/support/general-speed-size
    - Average upload is real low
    - FCC Map of a lot of coverage (pop density: 2 per household)

2. Format of the file storing the data: Is CSV okay? Yup! Can move between datacommon and other 
    - Aggregate by peak times within Municipalities (Everett, Quincy, etc..)

MLAB: 
1. How do you feel about our approach?
Options: Time, Aggregation similar to Ookla

Client's first aggregations by provider, by year & by municipalities:
    - List of all providers & comparing between municipalities
https://airtable.com/shrjWSiyF82WLrFny

Next step: getting a sense of how providers/broadband speed/municipalities
Visualization

One other grouping Client is interested in: What are these providers? What group? Wireless, DSL, Fiber (FCC)

2. Should we look at 2019?
Historical is always fascinating. Work on 2020 & work backwards on historical.


What is of interest to the municipalities: 
For the density of the household: How much money do they need to spend to get a bare minimum? - Connection to income (Comparison to census)


Resources:
Datakey set (all the blocks in all the tracks in all the municipalities in the state)