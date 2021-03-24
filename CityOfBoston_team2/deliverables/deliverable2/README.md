# Deliverable 2: Further Data Analysis

The revised proposal is available as a pdf [here]('d2_revisedProposal.pdf').  For this deliverable, we explored a single category, attempting to answer the following question in depth.

## Key Question Answered with Preliminary Analysis

<ol>
	<li>Which areas of the city are underserved in terms of a lack of essential amenities, and which amenities are missing?</li>
</ol>

Using the schools_sanitized dataset, we were able to identify and visually represent underserved areas using a basemap, pictured below. Areas within 15 minutes are pictured in blue, while underserved areas are shown in red.

![Areas underserved with schools](https://github.com/Zayta/CS506Spring2021Repository/blob/master/CityOfBoston_team2/deliverables/deliverable2/figs/underserved_schools.png?raw=true)

## Refined Limitations

### General Limitations Related to Preprocessing and Initial Analysis
<ul>
	<li>As previously mentioned, the bulk of the business and amenities data makes it difficut to be able to categorize manualy. We are looking into algorithms and heuristics that my help simplify this process.</li>
	<li>There is an inconsistency in the longitude and latitude standards used in the datasets. On some, coordinates are reltive to Boston, while others follow the WGS84 standard. This requires some transformation of these attributes, which we have achieved in code/preprocessing/parcels_cleaning.py</li>
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
	<li><a href="https://data.boston.gov/">Analyze Boston - Map and Parcel Data></a>
		<ul>
			<li>A single dataset.  Clean file saved as <a href='../../datasets_clean/parcels_sanitized.csv'>parcels_sanitized.csv</a>.</li>
			<li>This dataset lacks the proper longitude and latitude format.</li>
		</ul>
	</li>
	
</ul>


## Next Steps

### General Next Steps

Our next steps will revolve around completing the merging of data into a master dataset, which will drastically simplify future analysis. In order to do this, we need to deal with the uncategorized amenity types in some datasets, and standardize the latitude and longitude data among all data. Once this is completed, the remaining key questions will follow naturally as simple analysis of the data, which we will then focus on visually representing in an information-efficient way.

### Data-specific Next Steps

<a href='https://github.com/BU-Spark/BPDA-City-Business-Mapping/blob/master/data'>Boston Master businesses and establishments dataset</a>:

 Though street addresses may not be necessary, the lack of clear categorization is a major issue with this dataset.  In order to properly categorize the data points and answer key question 1, some categorization algorithm must be carried out on the set of categories given in the original data.

<a href='https://www.mapc.org/resource-library/food-systems-data/'>Grocers dataset from MAPC</a>:

Because there is a large number of MAPC datasets available, it must be determined which MAPC datasets are important enough to include.  Then, harder-to-obtain data can be scraped. Further work should be done to consolidate the datasets from this data source.

<a href='https://data.boston.gov/dataset/open-space1'>Greenspace data</a>:

Since this dataset has only street addresses, longitude and latitude (as well as land area) may need to be scraped from another dataset.  As with the businesses master dataset, a categorization algorithm is necessary to clearly determine amenity type.

<a href="https://data.boston.gov/">Analyze Boston - Map and Parcel Data></a>:

The latitude and longitude format must be transformed to the WGS84 standard.
