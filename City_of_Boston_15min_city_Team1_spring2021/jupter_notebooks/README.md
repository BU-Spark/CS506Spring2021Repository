# Instructions On How to Run Our Codes

To reproduce our results, you need to first run the notebooks in "preprocess" folder.

The sequence is: CS506_open_space_annotated.ipynb -> CSDATA_combine_datasets_V2_annotated.ipynb -> CS506_combineParcels_V2_annotated.ipynb.

All 3 notebooks involve datasets in the "datasets" folder. You do not need to run CS506_raw_parcels.ipynb and parcel_to_coord.ipynb because the dataset they use is too big to upload to Github and their final output file (final_parcels_coords.csv) is already in "datasets". If you really want to run those codes, the link for dataset they require is:
https://koordinates.com/layer/96130-boston-massachusetts-parcels/

After that, you need to run the codes in "distance_matrix". You can run parcel_service_distance_v2.ipynb, DMA_process.ipynb and DMA_process_2.ipynb (follow this order) to get all the distances (between parcels and essential services), and run CS506DATA_View_DMA_annotated.ipynb to visualize the data.

# Note that for all codes above, if it uses a PATH (e.g. in pad.read_csv or with open(PATH, ...) as f), you will need to change the PATH value depending on how you put the files on your local machine. Also, in DMA section you need a Google Map API key; Please apply for a key yourself. We won't provide such a key because it is linked to our billing account (e.g. credit cards) and will charge fees.
