# Deliverable 1: Initial Preprocessing and Analysis

The revised proposal is available as a pdf [here]('d1_revisedProposal.pdf').  For this deliverable, three data sources were examined and preprocessed, and data from one source was fully analyzed to answer the first key question.

## Key Question Answered with Preliminary Analysis

<ol>
	<li>What amenities in Boston belong to each of the six categories of essential amenities necessary for a 15-minute city?</li>
</ol>

Of the datasets that were preprocessed, three allowed clean categorization of amenities into one of the six categories described below.  The datasets can be found below, as part of the data sourced form MAPC.  As a next step, this categorization will be expanded into the other datasets and data sources.

## Processing Methods and Goal

Since the ultimate goal for the project is to analyze which parcels are within 15 minutes of all categories of essential amenities, the datasets needed to be processed such that they retained information relevant to location and amenity type.  Then, the pertinent information from each dataset is:
<ul>
	<li>Name</li>
	<li>Location
		<ul>
			<li>latitude and longitude</li>
			<li>street address</li>
		</ul></li>
	<li>Amenity Type (one of six categories given)
		<ul>
			<li>Commercial</li>
			<li>Education</li>
			<li>Food access</li>
			<li>Healthcare</li>
			<li>Recreation</li>
			<li>Social</li>
		</ul></li>
</ul>

To acheive this goal, each dataset that was processed was imported as a pandas dataframe, cleaned, and then exported as a sanitized csv file.  Only one of the sources of data contained datasets that could simply be categorized into appropriate amenity categories, so two of the clean datasets contain only name, location, and type as suggested by the dataset.

## Datasets Processed

<ul>
	<li><a href='https://github.com/BU-Spark/BPDA-City-Business-Mapping/blob/master/data'>Boston Master businesses and establishments dataset</a>
	<ul>
		<li>A single dataset.  Clean file saved as <a href='../../datasets_clean/businesses_sanitized.csv'>businesses_sanitized.csv</a>.</li>
	</ul></li>
	<li><a href='https://www.mapc.org/resource-library/food-systems-data/'>Grocers dataset from MAPC</a>
		<ul>
			<li>Dataset for farmers.  Clean file saved as <a href='../../datasets_clean/farmers_sanitized.csv'>farmers_sanitized.csv</a>.</li>
			<li>Dataset for food retailers.  Clean file saved as <a href='../../datasets_clean/food_retailers_sanitized.csv'>food_retailers_sanitized.csv</a>.</li>
			<li>Dataset for schools.  Clean file saved as <a href='../../datasets_clean/schools_sanitized.csv'>schools_sanitized.csv</a>.</li>
		</ul></li>
	<li><a href='https://data.boston.gov/dataset/open-space1'>Greenspace data</a>
		<ul>
			<li>A single dataset.  Clean file saved as <a href='../../datasets_clean/open_space_sanitized.csv'>open_space_sanitized.csv</a>.</li>
		</ul></li>
</ul>

## Refined Limitations

### General Limitations Related to Preprocessing and Initial Analysis
<ul>
	<li>The businesses and amenities generally are not necessarily clearly in one category or another—some manual decision-making may be required to determine which amenities are in which categories.  Some datasets have clearly defined amenity types while others require a categorization algorithm to determine amenity type.</li>
	<li>Lack of specific and consistent location data in each dataset could prevent accurate geospatial analysis.</li>
</ul>

### Data-specific Limitations

<ul>
	<li><a href='https://github.com/BU-Spark/BPDA-City-Business-Mapping/blob/master/data'>Boston Master businesses and establishments dataset</a>
		<ul>
			<li>A single dataset.  Clean file saved as <a href='../../datasets_clean/businesses_sanitized.csv'>businesses_sanitized.csv</a>.</li>
			<li>Limitations: This dataset lacks street address and has major inconsistencies in business type.  It may not be necessary to include street address, but the inconsistencies in the business type classification must be resolved.
		</ul></li>
	<li><a href='https://www.mapc.org/resource-library/food-systems-data/'>Grocers dataset from MAPC</a>
		<ul>
			<li>Dataset for farmers.  Clean file saved as <a href='../../datasets_clean/farmers_sanitized.csv'>farmers_sanitized.csv</a>.</li>
			<li>Dataset for food retailers.  Clean file saved as <a href='../../datasets_clean/food_retailers_sanitized.csv'>food_retailers_sanitized.csv</a>.</li>
			<li>Dataset for schools.  Clean file saved as <a href='../../datasets_clean/schools_sanitized.csv'>schools_sanitized.csv</a>.</li>
			<li>Limitations:  MAPC contains a large number of datasets, which must be sorted through to determine usefulness.  Not all datasets contain necessary data.
		</ul></li>
	<li><a href='https://data.boston.gov/dataset/open-space1'>Greenspace data</a>
		<ul>
			<li>A single dataset.  Clean file saved as <a href='../../datasets_clean/open_space_sanitized.csv'>open_space_sanitized.csv</a>.</li>
			<li>Limitations: The greenspace data lacks longitude and latitude.  This may be a significant problem, because clustering and distance analysis cannot be carried out with street addresses alone.  Units/parcels and amenity type in this data are also unclear.</li>
		</ul></li>
</ul>

## Changes to Project Scope

Given that not all the datasets contain data points that are all within the limits of the City of Boston, the project scope may be expanded (or reduced in specificity) to the general Boston area. 

## Next Steps

### General Next Steps

Since only some of the data was processed and analyzed for this preliminary step, the next step is first to clean and categorize all of the data.  Then, definite limitations for the data as a whole can be analyzed and scraping can be done to make up for missing data in each dataset.  Finally, as the last initial processing step, the datasets can be merged to create a master dataset with which the next key question can be answered.

### Data-specific Next Steps

<a href='https://github.com/BU-Spark/BPDA-City-Business-Mapping/blob/master/data'>Boston Master businesses and establishments dataset</a>:

 Though street addresses may not be necessary, the lack of clear categorization is a major issue with this dataset.  In order to properly categorize the data points and answer key question 1, some categorization algorithm must be carried out on the set of categories given in the original data.

<a href='https://www.mapc.org/resource-library/food-systems-data/'>Grocers dataset from MAPC</a>:

Because there is a large number of MAPC datasets available, it must be determined which MAPC datasets are important enough to include.  Then, harder-to-obtain data can be scraped. Further work should be done to consolidate the datasets from this data source.

<a href='https://data.boston.gov/dataset/open-space1'>Greenspace data</a>:

Since this dataset has only street addresses, longitude and latitude (as well as land area) may need to be scraped from another dataset.  As with the businesses master dataset, a categorization algorithm is necessary to clearly determine amenity type.

