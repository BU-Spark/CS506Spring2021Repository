Deliverable 3: Report First Draft
================
Urban Mechanics Team 2

At this point in our analysis, the number parcels with 15-minute access
to each type of amenity have been determined. Some analysis has also
been completed regarding relationship between areas with amenity access
and demographics of those same areas.

## Final dataset

The final merged dataset has been created; it is called
`final_merge.csv` in this directory. The features on it are `name`,
`zip`, `lat`, `lon`, `category`, and `address`. Most of these are
self-explanatory. `lat` and `lon` correspond to latitude and longitude
respectively, `address` refers to street address, and `category` is
amenity category. Each of the amenity datasets was standardized and
concatenated to create this dataset.

## General insights

Overall, there seems to be a broad distribution of all amenity types.
The map below displays all amenities. Though it is somewhat difficult to
differentiate color; commercial corresponds to red, education to blue,
food access to green, health to purple, recreation to orange, and social
to dark red.

![‘Map of access for commercial amenities.’](figures/base.png)

Discerning specific amenities from this figure is difficult, however it
is obvious that each color is fairly well distributed throughout Boston.
Some of the amenities are outside Boston; this may need to be controlled
in a future analysis. Overall, there were 0 parcels that lacked all
amenities, mostly because every parcel was within 15 minutes of a
commercial amenity, and there were 16,033 out of 62,190 parcels (25.8%)
that lacked at least one amenity.

Most of the missing amenities were concentrated in the zip codes 02136
and 02132, which did not have noticeably different demographic
properties in out initial analysis—it is very likely that more in-depth
analysis will be required to understand this observed trend.

It should also be noted that the analyses were carried out for only
residential parcels. That is, only distances from residential parcels to
amenities were considered in order to cut down on calculation time (of
course, amenities did not have to be on residential parcels).

## Commercial

![‘Map of access for commercial amenities.’](figures/commercial.png)

There were no parcels without access to commercial amenities. This is
equal across zip codes and demographics.

## Education

![‘Map of access for education amenities.’](figures/education.png)

1.4% of parcels do not have access to education amenities. The majority
of the underserved parcels are in the zipcodes 02132 and 02136.

## Food Access

![‘Map of access for food access amenities.’](figures/food.png)

1.8% of parcels do not have access to food access amenities. Though no
zip codes had a very large number of parcels missing amenities, the zip
codes 02130, 02132, and 02467 have the largest number of underserved
parcels.

## Healthcare

![‘Map of access for healthcare amenities.’](figures/health.png)

2.9% of parcels do not have access to healthcare amenities. Most of
these parcels are found in the zipcode 02136.

## Recreation

![‘Map of access for recreation amenities.’](figures/recreation.png)

2.3% of parcels do not have access to recreation amenities. Most of the
under-served parcels seem to be concentrated in zip codes 02126, 02131,
02132, and 02136.

## Social

![‘Map of access for social amenities.’](figures/social.png)

24.1% of parcels do not have access to social amenities. The large
majority of the under-served parcels were in the zip codes 02136 and
02132, though there were some others missing a signficant number.

## Next Steps

As we move further towards completion of the project, there is still
some cleaning and analysis to be done. All the above analysis was
completed using a simple distance algorithm—a more complex algorithm
that better accounts for the network of traffic and streets in Boston
should be developed. Additionally, the analysis has so far been carried
out based on walking times; biking times should be added in the next
iteration of this report.

There were also some problems with classification and calculation time
that came up with this analysis; some of the datasets may need to be
reclassified, and others may need to be filtered to cut down on
calculation time.

Lastly, closer analysis should be done with other demographic factors
and regarding specific combinations of amenity access or lack thereof.
