## Civera - MassCourtsPlus Project README

Given the Civera court database, to extract actor & action fields from case descriptions, use the <extraction_pipeline.ipynb> notebook.
  Open Google Colab.
  Upload <extraction_pipeline.ipynb> and open it.
  In the *Runtime* dropdown menu, select *Change Runtime Type*.
  In the popup window, select "GPU" from the Hardware Accelerator dropdown list, and *SAVE*.
  Now in the top right corner, be sure you are connected. (You should see RAM and DISK).
  Once connected, in the *Runtime* dropdown menu, select *Run all*, and the notebook will execute the rest.
  
When <extraction_pipeline.ipynb> is running, it completes code cells 1-12 in about a minute. These cells install/download the necessary libraries & files, create helper functions (with the regex code - see "Civera Project Final Report.pdf" section on Methodology for Normalizing the Database), create a Normalizer class (that uses previous cells' functions), initialize the normalizer class, and connect to the DB in MySQLWorkbench. 
After this, the notebook spends all of its time running the Normalize Data cell. The latency on this cell is explained in "Civera Project Final Report.pdf" section on Final Methodology, Performance Analysis.


Link to the Google Drive folder that contains all of our binary files:

https://drive.google.com/drive/folders/1MBxNEwgGCAONtKo8Y-U9XLLNbQXBMsps?usp=sharing

