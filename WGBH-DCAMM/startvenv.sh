#!/bin/bash

echo "Setup the python virtual environment"
python3 -m venv venv
echo "CREATED the virtual environment"
source venv/bin/activate
echo "ACTIVATED the virtual environment"
pip3 install -r requirements.txt
echo "INSTALLED Required Packages"

# Run the Tests
pip3 install .
tox --recreate

#python3 starter-code/initial-exploration.py
#python3 src/explore_product.py
#python3 src/explore_product.py
#sed 's/,,$//' stat_data/X_product_drop.csv > stat_data/X_prod.tmp; mv stat_data/X_prod.tmp stat_data/X_product_drop.csv
#sort -t',' -k 4n stat_data/X_product.csv > stat_data/X_product_srt.csv
#sort -t',' -k 2n stat_data/X_product_drop.csv > stat_data/X_product_drop_srt.csv
#sort -t',' -k 4n stat_data/X_product_keep.csv > stat_data/X_product_keep_srt.csv
#python3 src/explore_user.py
#sed 's/,,$//' stat_data/X_User_drop.csv > stat_data/X_User.tmp; mv stat_data/X_User.tmp stat_data/X_User_drop.csv
## use the following command to sort the output
#sort -t',' -k 4n stat_data/X_User.csv > stat_data/X_User_srt.csv
#sort -t',' -k 2n stat_data/X_User_drop.csv > stat_data/X_User_drop_srt.csv
#sort -t',' -k 4n stat_data/X_User_keep.csv > stat_data/X_User_keep_srt.csv
