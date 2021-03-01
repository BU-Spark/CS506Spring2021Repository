# Baystate Banner Research: LatinX Populations x Trump Voters
 
## Organization: Baystate Banner

## Contact
 
Senior Editor: Yawu Miller, yawu@bannerpub.com

Project Manager: Lingyan Jiang, lingyanj@bu.edu
Staff Lead:  Steve Backman, sbackma1@bu.edu

Team Representative: Ngozi Omatu, nomatu@bu.edu    
Member: Song Xie, sxie2@bu.edu                                  
Member: Matan Ziegel, mziegel@bu.edu                         
Member: Gil Lotzky, glotzky@bu.edu                               
Member: Anna Xie, annaxyw@bu.edu 

## Organization Description:

The Bay State Banner is an African American owned news weekly that reports on the political, economic, social, and cultural issues that are of interest to African American and English speaking Latinos in Boston and throughout New England

## Project Description:

The client would like to understand the components of support for Republicans over the time period of 2015-2020 including Presidential elections and the Governor’s races. The goal of the project is to find whether or not there is a significant difference in the voting pattern of the LatinX community from 2016 to 2020. We will be collecting data from cities with a majority LatinX population and non-LatinX populations. We will then compare the two populations to see whether there is a significant difference in voting patterns between the LatinX community and the control group(which has voted Republican consistently in the past). If there is a significant difference between the communities, we will analyze the various changes from 2016 to 2020 in those communities. The main goal is to conclude which LatinX voters changed their votes and which voters stayed consistent. 

## Data Sets:

* PD43 MA state portal: https://electionstats.state.ma.us/
	*2016:(https://electionstats.state.ma.us/elections/view/130243/)and 2020:(https://electionstats.state.ma.us/elections/view/140751/) Presidential races 
	*2014:(https://electionstats.state.ma.us/elections/view/126084/) and 2018:(https://electionstats.state.ma.us/elections/view/131501/) MA Governor (General Elections)
*Census data: https://data.census.gov/cedsci/ (Demographics)
	*6 cities Census data 2019: https://www.census.gov/quickfacts/fact/table/douglastownworcestercountymassachusetts,southwicktownhampdencountymassachusetts,acushnettownbristolcountymassachusetts,lynncitymassachusetts,springfieldcitymassachusetts,lawrencecitymassachusetts/PST045219
	*Lawrence: 2016(https://data.census.gov/cedsci/table?g=8600000US01840,01841,01843&tid=ACSDP5Y2016.DP05&hidePreview=true) and 2019(https://data.census.gov/cedsci/table?g=8600000US01840,01841,01843&tid=ACSDP5Y2019.DP05&hidePreview=true)
	*Lynn: 2016(https://data.census.gov/cedsci/table?g=8600000US01901,01902,01904,01905&tid=ACSDP5Y2016.DP05&hidePreview=true) and 2019(https://data.census.gov/cedsci/table?g=8600000US01901,01902,01904,01905&tid=ACSDP5Y2019.DP05&hidePreview=true)
	*Springfield: 2016(https://drive.google.com/file/d/1ClJgIagU0SPYzgKfoWBZ483_jaPDCk3O/view?usp=sharing) and 2019(https://drive.google.com/file/d/1sAx6LqFNTRZY-yACggIea3Bu5jiACAjB/view?usp=sharing)
	*Southwick: 2016(https://drive.google.com/file/d/1IoutMwAnHnFSPdNOyFN1IJaBRjjq58RL/view?usp=sharing) and 2019(https://drive.google.com/file/d/1JJ-2rkBeTGxsELkjnU2zqaUSRFir_x6d/view?usp=sharing)
	*Acushnet: 2016(https://data.census.gov/cedsci/table?g=8600000US02743&tid=ACSDP5Y2016.DP05&hidePreview=true) and 2019(https://data.census.gov/cedsci/table?g=8600000US02743&tid=ACSDP5Y2019.DP05&hidePreview=true)
	*Douglas: 2016(https://data.census.gov/cedsci/table?g=8600000US01516&tid=ACSDP5Y2016.DP05&hidePreview=true) and 2019(https://data.census.gov/cedsci/table?g=8600000US01516&tid=ACSDP5Y2019.DP05&hidePreview=true)
		Optional Support data:http://archive.boston.com/news/local/massachusetts/graphics/03_22_11_2010_census_town_population/
*LatinX Origin Demographics:https://www.pewresearch.org/hispanic/fact-sheet/latinos-in-the-2016-election-massachusetts/#:~:text=The%20Hispanic%20population%20in%20Massachusetts,Hispanic%20statewide%20population%20share%20nationally (2014)

## Suggested Steps:

#### Step 1: 
Collect city voter & demographic data of majority LatinX towns (~80%) 
	* Lawrence 
	* Lynn 
	* Springfield
and compare with representative mostly white towns very likely to vote Republican as control groups
	*Southwick
	*Acushnet
	*Douglas
About the data:
	*Voter data includes total ballots cast, registered voters, eligible voters, and demographics for that city.
	*Election races will include 2016 and 2020 Presidential races as well as 2014 and 2018 MA Governor-general elections.



#### Step 2:
Use pandas to read through csv files and convert to data frames. Only keep key attributes for demographic data (zip code, estimated total pop, LatinX sub-group pop, and voting age pop (18+)) and election data (city zip codes, city names, total votes per candidate, total votes)

#### Step three: 
Relate city election data to city demographic data (either via each city’s zip codes or precincts). Analyze different kinds of LatinX voters supporting Trump - Mexican, Dominican, Cuban American. Where is their support concentrated? How did their support change from 2016 to 2020

#### Step three: 
Examine the difference between LatinX people registered as Democrat, Republican, Independent in these different geographic and elections.

#### Step four: 
Complete analysis on correlations between how these towns to vote, do they move with each other in different elections>

#### Step five: 
Complete data visualizations based to present which neighborhoods, cities, and districts have higher levels of support for Donald Trump.

## Strategic Questions:

1.How has support for Trump shifted across LatinX sub-groups from 2016 to 2020? Was there a significant shift?

2.What is the breakdown of LatinX sub-groups in their support for Democratic vs. Republican candidates?

3.Which LatinX groups exhibited changed their votes and which groups remained the same?


## Additional Information:
#### Tools & Methods
Data pre-processing: Pandas to convert csv files into data frames, NumPy for processing and organizing the pre-processed data

Data Visualization: Matplotlib, Seaborn, Tableau for all kinds of interactive visualizations

#### Weekly Meeting Schedule:
#### Wednesdays 11am-12:30pm EST


## Potential Ricks & Limitations:

1. Lack of connection between city election results and city demographic data, i.e. unable to break down city election results by demographics as we are only given each city’s aggregate election results

2. Difficult to apply clustering methods as we are only given aggregate data for demographics and election results for each city (lack of large dataset)

3. The conclusion on voting pattern changes may not be concrete due to the other factors such as changes in voter turnout or each demographic’s population which is not indicative of a change in preference for a political candidate.


## General Questions:

1.How can we combine the election data with the demographic data?

	a. It will be difficult to combine data frames because we cannot correspond the zip codes from the demographic data to the precincts in the election data 
	b.Can't correlate changes in demographics to changes in election results
	c.Worst case scenario, should we combine data frames based on the city?
2.Should we organize election data based on Republicans vs Non Republicans rather than Republicans vs Democrats vs Independents?

3.We can’t directly answer any of the key questions until we are able to relate election data to demographic data

                             
## Key Questions Answers:

1.In our non-control group cities (Springfield, Lawrence, Lynn), Springfield saw a 1.79 percentage point increase in LatinX population (relative to the city’s total population) and a 5.13 percentage point increase in Trump votes(across all races). For Lawrence, there was a 3.44 percentage point increase in LatinX population(relative to the city’s total population) and a 10.85 percentage point increase in Trump votes(across all races). For Lynn, there was a 4.79 percentage point increase in LatinX population(relative to the city’s total population) and 2.96 percentage point increase in Trump votes(across all races).

Listed below are the screenshots of the code for the preprocessed data:


![Screenshots:](https://github.com/nomatu/CS506Spring2021Repository/blob/master/tvbiw-ehokw.png)
![](https://github.com/nomatu/CS506Spring2021Repository/blob/master/example2.png)
![](https://github.com/nomatu/CS506Spring2021Repository/blob/master/example3.png)
![](https://github.com/nomatu/CS506Spring2021Repository/blob/master/example4.png)


