# Civera - MassCourtsPlus Project README

## How to run the Normalizer
Given the Civera court database, in order to extract actor & action fields from case descriptions, use the [extraction_pipeline.ipynb](./Code/extraction_pipeline.ipynb) notebook.
  1. Open Google Colab.
  2. Upload [extraction_pipeline.ipynb](./Code/extraction_pipeline.ipynb) and open it.
  3. In the *Runtime* dropdown menu, select *Change Runtime Type*.
  4. In the popup window, select "GPU" from the Hardware Accelerator dropdown list, and *SAVE*.
  5. In the top right corner, be sure you are connected. (You should see RAM and DISK).
  6. Once connected, in the *Runtime* dropdown menu, select *Run all*, and the notebook will execute the rest.
  
When [extraction_pipeline.ipynb](./Code/extraction_pipeline.ipynb) is running, it completes code cells 1-12 in about a minute. These cells install/download the necessary libraries & files, create helper functions (with the regex code - see [Civera Project Final Report.pdf](http:///C:/Civera Project Final Report.pdf) section on Methodology for Normalizing the Database), create a Normalizer class (that uses previous cells' functions), initialize the normalizer class, and connect to the DB in MySQLWorkbench. 
After this, the notebook spends all of its time running the Normalize Data cell. The latency on this cell is explained in [Civera Project Final Report.pdf](./Civera Project Final Report.pdf) section on Final Methodology, Performance Analysis.


## Drive folder containing all binary files

https://drive.google.com/drive/folders/1MBxNEwgGCAONtKo8Y-U9XLLNbQXBMsps?usp=sharing

