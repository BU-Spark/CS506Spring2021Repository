# Instructions On How to Run Our Codes

To reproduce our results, you need to first run the notebooks in "preprocess" folder.

The sequence is: CS506_open_space.ipynb -> CSDATA_combine_datasets_V2.ipynb -> CS506_combineParcels_V2.ipynb.

All 3 notebooks involve datasets in the "datasets" folder. You do not need to run CS506_raw_parcels.ipynb because the dataset it uses is too big to upload to Github and its output file is already in "datasets". If you really want to run it, the link for dataset it requires is:

After that, you need to run the codes in "distance_matrix". You can run parcel_service_distance_v2.ipynb, DMA_process.ipynb and DMA_process_2.ipynb (follow this order) to get all the distances (between parcels and essential services), and run CS506DATA_View_DMA.ipynb to visualize the data.

# Note that for all codes above, if it uses a PATH (e.g. in pad.read_csv or with open(PATH, ...) as f), you will need to change the PATH value depending on how you put the files on your local machine. Also, in DMA section you need a Google Map API key; Please apply for a key yourself. We won't provide such a key because it is linked to our billing account (e.g. credit cards) and will charge fees.
