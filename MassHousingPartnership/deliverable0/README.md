# Deliverable 0

## MHP Project Team Meeting

- [ ] Time: Wed 2:00-2:30PM (weekly with PM and biweekly with clients)

- [ ] People:
- Rishab Nayak(PM)
- Greta Bruce(Spark)
- Tom Hopper(Client)
- Asif Rahman
- Belamarich, Camilla
- Benjamin Lague
- Shuzhe Luan
- Lingxiao Yuan

## Project Description

This project is an extension of an existing research project, called TODEX: A Transit-Oriented Development Explorer for Massachusetts, for which our team developed a methodology to estimate residential density near every MBTA rail station in Massachusetts.

We are embarking on a project that uses the same data sources (statewide assessors parcels and statewide emergency 911 addresses) and a similar methodology to create a database of residential density across the entire state.

We would like to be able to keep this database updated easily and eventually share the dataset and associated analytical work with the public via an interactive website.

The project would focus on back end data science processes including data aggregation, cleaning, imputation, and automation of these processes for when new data becomes available.

The project could potentially choose one or several municipalities as a test case for the methodology and automation that could be later used by client's staff to analyze the entire state.

We have an existing methodology that has served us well but is time consuming to replicate and difficult to scale.

We seek to understand ways to streamline the analytical process and overcome some of the issues we have had with computation time.


## Datasets

https://www.mass.gov/doc/standard-for-digital-parcels-and-related-data-sets-version-21/download

https://docs.digital.mass.gov/dataset/massgis-data-standardized-assessors-parcels

https://docs.digital.mass.gov/dataset/massgis-data-master-address-data

### Data information and limitation
- Statewide assessor parcel data
  - Geo-database format
  - Available by request (send email for download) Mass GIS
-	Statewide address data
  - Geo-database format
- USPS dataset
  - Might have duplicates of addresses.
- Datasets do not have a common key. Need to connect the two datasets by location.

# Suggested Steps
1. Automate collection of source data (including spatial data)
2. Standardize and join source data
3. Calculate or impute residential density for each location in the data set through decision rules and other imputation techniques.
4. Create an automated process through which new parcel and address information can be processed quickly to keep the residential density database updated.

### Core Values and challenges:
- Updatability - need to be run the program on the newest data-sets
- Needs to be friendly with R code (can run on python within R) Tom should be kept up to date on the tools we are using. Annotations and documentation for our code is essential.
- Modifiable and able to set rules within the program (at least access to the code and an understanding of how it works)
- Datasets do not have a common key. Need to connect the two datasets by location. Geopandas and Shapely.

## Question to be answered in Analysis
1. What is the most efficient way to deploy and automate a data processing task when the source data updates frequently.
2. How to scale methodology to the entire state data set and overcome computationally expensive analytical process

### Required Features:
- [ ] Paring datasets - getting a location ID for both parcel data and addresses
- [ ] Tagging parcels as housing/forest/business, etc.
- [ ] Tagging parcels with more granular data: how dwelling units are on the parcel?
- [ ] Residential density (Residential housing units) on a parcel
- [ ] Utilize a map and draw a shape on it to see the density of that location.

## Additional Information
### Tools and Methods
- For scraping - Scrapy, Selenium webdriver, and/or Beautiful soup.

- For cleaning and preprocessing use Pandas to organize the dataset into dataframes for faster computation.

- Data visualization libraries such as Matplotlib, Seaborn, and Bokeh (interactive web-integratable visualizations).

## Time challenges:
The constraint of time, as we have only two full months left.

We need to familiarize ourself with the existing project’s codebase/environment and maybe use it in our current project
