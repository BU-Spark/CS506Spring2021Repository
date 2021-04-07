## raw datasets
The datasets named "food_retailers_2017_pt", "Final_merge", "(raw) boston-massachusetts_parcels" and "Open_space" are all raw datasets that are given at the beginning of this project. 
Note: "(raw) boston-massachusetts_parcels.csv" is bigger than 100 MB and cannot be pushed to github; we will provide a link later instead.

## DMA_refine.csv
The dataset "DMA_refine" is the most up-to-date dataset that contains our reserach results.
It contains the latitude, longitude and zip code of those combined parcels (13121 in total). 
The headings are very easy to understand: they contain the distance of that parcel to the closet essential amenity and the type of amenity is just as indicated (for example, "supermarket"). 
The distance is in meters, and the walking time is in seconds.

## CS506_parcels_service.json
This json file matches each parcel to its closest 2 essential amenities of each kind. The structure of this file is given below:
general:
{'supermarket': pairs, 'parks and open space': pairs, 'grocery': pairs, 'healthcare': pairs, 'hospital': pairs}
The structure of pairs (by example, dict['supermarket'][1]):
1:{'parcel': {'lat': 42.232159, 'lon': -71.12882909999998, 'addresses': ['meadow rd, hyde park, 02136']}, 'closest1': {'name': 'Save Mart Supermarket', 'address': '270 Reservation Rd', 'lat': 42.2541, 'lon': -71.13388}, 'closest2': {'name': 'Super Discount Store', 'address': '1232 River St Hyde Park', 'lat': 42.2558083, 'lon': -71.1228839}}

## final_parcels_coords.csv, Open_Space_fully_processed.csv, merged_processed5.csv
They are datasets that contain intermediate results. Their headings are in plain English and are very straightforward. "final_parcels_coords.csv" contains the infomation of all the small parcels; "Open_Space_fully_processed.csv" contains all the available valid addresses of open spaces; "merged_processed5.csv" is built upon "Open_Space_fully_processed.csv" and contains all the necessary infomation of found essential amenities.


## httplinks.npy
This is not a dataset by definition. It contains urls used to search in Google Distance Matrix API. Every 5 urls correspond to 1 parcel and 5 cloest essential service of each kind that belongs to it. The sequence is: 'supermarket', 'grocery', 'healthcare', 'hospital' and 'green space'.