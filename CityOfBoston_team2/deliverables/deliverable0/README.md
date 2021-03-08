# Deliverable 0: Revised Project Proposal

This proposal is also available as a pdf [here]('d0_revisedProposal.pdf').  The project is through Spark! BU and the City of Boston, and involves analyzing Boston's current status in a 15-minute city framework.

See <a href='#steps'>steps</a>, <a href='#questions'>questions</a>, and <a href='#limitations'>limitations</a> for notably updated aspects of the proposal.

## Contacts

**Nayeli Rodriguez**<br>
Technologist, Mayor’s Office of New Urban Mechanics<br>
City of Boston<br>
nayeli.rodriguez@boston.gov

Secondary Contact:<br>
Kat Eshel<br>
Carbon Neutrality Program Manager<br>
City of Boston<br>
katherine.eshel@boston.gov

Project Manager:<br>
Kamran Arif<br>
Spark! BU<br>
kamran55@bu.edu

## Organization

**City of Boston**<br>
The municipal government for the city of Boston, overseeing all public works and governance for Boston.

## Team Members

Katelyn Lee (ktllee@bu.edu)<br>
Darren Liu (darrenjl@bu.edu)<br>
Khaled Sulayman (khaledsh@bu.edu)<br>
Sandra Zhen (szhen@bu.edu)

## Meeting Times

**Bi-weekly with clients:**<br>
Thursday, 11-11:30am ET, beginning (02/25/21)

**Weekly with PM:**<br>
Friday, 4-4:30pm ET


## Project Description

Project type: Data Science

We would like to research the features that can make Boston a “15-minute city”, where essential services and resources are all within 15 minutes of each parcel in the city. Types of essential services within the city include:
<ul>
<li>Commercial</li>
<li>Education</li>
<li>Food access</li>
<li>Healthcare</li>
<li>Recreation</li>
<li>Social</li>
</ul>

We will target dense urban areas for the 15-minute city concept.  This will be done by identifying parcels of land in the city nearby or within areas with the highest concentration of essential services and then finding the shortest paths between them.  Then, the areas identified as 15-minute city sections will be displayed on a map to allow for identification of areas in need of more development of essential services.

Many cities such as [Melbourne](https://www.planning.vic.gov.au/__data/assets/pdf_file/0033/487509/Living-Locally-20MN-in-Greenfield-Growth-Areas.pdf) that have implemented the plan seem to heavily emphasize bike lanes and access to parks in the scheme, so a worthwhile extra addition to the project might be identifying locations that can easily be integrated into wide bike lanes and potential public lands to be marked out for green spaces/parks. Further, the [C40 mayor’s report](https://www.c40.org/other/agenda-for-a-green-and-just-recovery) emphasizes the use of bike lanes as a post-COVID economic recovery idea to build more closely knit cities and improve accessibility and reduce the reliance on public transit and cars that posed a COVID risk for many.

## Data Sets

### From previous Spark! projects or recommended in inital proposal
<ul>
	<li><a href='https://github.com/BU-Spark/BPDA-City-Business-Mapping/blob/master/data'>Boston Master businesses and establishments dataset</a></li>
	<li><a href='https://www.mapc.org/resource-library/food-systems-data/'>Grocers dataset from MAPC</a></li>
	<li><a href='http://maps.massgis.state.ma.us/map_ol/ej.php'>Environmental justice demographics</a></li>
</ul>

### Found or from client
<ul>
	<li><a href='https://data.boston.gov/dataset/open-space1'>Greenspace data</a></li>
	<li><a href='https://data.boston.gov/'>Map and parcel data (Analyze Boston)</a></li>
	<li>Census data</li>
</ul>

## <a name="steps">Steps</a>

<ol>
	<li>Combine the datasets and process them into clear categories of essential amenities.  Amenities should be categorized into the following categories: commercial, education, food access, healthcare, recreation, and social . Use the business_type fields within the Boston Master businesses and establishments dataset. Base geographic unit will be land parcels (parcel data from Analyze Boston).</li><br>
	<li>Identify the 15-minute city areas.  Which of Boston’s neighborhoods/zip codes contain parcels with essential amenities within a 15-minute commute? Note that commute refers to walking or biking.  Employ the CLARANS algorithm to cluster areas with dense essential amenities.</li><br>
	<li>Analyze the missing essential amenities within zip codes that do not meet the requirements for a 15-minute city.  Which areas are missing which amenities?</li><br>
	<li>Conduct demographic analysis on the parcels of land and compare the residents in 15-minute communities to non 15-minute communities. What are the demographic features of residents living within the 15-minute communities and those not living in them? Features to include: race, income, language spoken, housing density, etc.</li><br>
	<li>Create a map of the city displaying the 15-minute compliant areas, and also the areas which need more access to essential amenities and the amenities they require.  Final product should be at least usable by clients to display needs throughout Boston—.kml file should be considered to create a clickable map.</li>
</ol>

## <a name="questions">Questions</a>

<ol>
	<li>What amenities in Boston belong to each of the six categories of essential amenities necessary for a 15-minute city?</li>
	<li>What percentage of parcels are within 15 minutes of essential amenities?</li>
	<li>Which areas of the city are underserved in terms of a lack of essential amenities, and which amenities are they missing?</li>
	<li>What are the demographics of the underserved (non-15-minute) communities?</li>
</ol>


## <a name="limitations">Limitations</a>

<ul>
	<li>The businesses and amenities generally are not necessarily clearly in one category or another—some manual decision-making may be required to determine which amenities are in which categories.</li>
	<li>Walking and biking speeds can vary dramatically per person.  For biking time specifically, there may not be complete data for safe bike routes, which would impact the distances defined as “within 15-minutes” of any given parcel.</li>
	<li>Lack of specific and consistent location data in each dataset could prevent accurate geospatial analysis.</li>
</ul>

## Additional Information

### Tools and Methods
*Data processing:*
Pandas and NumPy will be used to clean and process the datasets into one master dataset.

*Clustering & Graph search:*
[CLARANS algorithm](https://pyclustering.github.io/docs/0.9.0/html/d6/d42/classpyclustering_1_1cluster_1_1clarans_1_1clarans.html) -  Works much better for high-dimension spatial clustering than DBScan that becomes inefficient and inaccurate when multiple attributes are added. We have multiple essential service types so it would be best to use CLARANS. 

[Kruskal’s algorithm implementation in Python](https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/) - To find the shortest distance between multiple sets of points, this will be done to find the parcels that are within a given short distance from all necessary amenities.

*Data Visualization:*
Matplotlib, Seaborn, Tableau, Folium for visualizing the geospatial data as needed.

*Final product:*
Note that clients have no data processing ability.  Maybe Simplekml to create an interactive map.  

### Optional Additional Steps with Extra Time
Examine the variance in type/density of amenities in each area.  For example, there may be a difference between 15-minute areas that include only one park or grocery store and areas that have a large variety of each type of amenity.

Analyze the paths between essential amenities to determine where additional bike lanes and other paths may be necessary.  This could be done by using Kruskal’s or Djikstra’s algorithm to find shortest routes between different areas, and analyzing junctions of paths to find which could be easily interconnected to most benefit.

### Further Background Information
An example of the type of final product desired can be found [here](https://app.developer.here.com/15-min-city-map/).

















