#!/bin/bash
# 
# This script iterates through each quarter of the passed in year, and pulls 
# Ookla parquet files from aws s3. These files are intended to then be converted
# to csv format elsewhere. 
# 
# Note: the parquet format is an Apache open-source data format, and we find it
# easier to work with than GIS data.
# 
# Author: Nathan Lauer
# Email: lauern@bu.edu
# Please feel free to ask me any questions, I hope you're having a nice day!

script_name=$0
year=$1

# Defines usage for this script, executes if user requests help or upon error
function usage() {
  echo "usage: ${script_name} <year>"
  exit 
}

# Helper function to provide consistent logging format
function logit() {
  text_to_log=$1
  echo "[${script_name}][`date`] - ${text_to_log}" 
}

################## Main execution flow
# Check correct number of arguments
if [ "$#" -ne 1 ]; then
  usage
fi

# Mark start time
start=`date +%s`

# Define types
format='parquet' # (shapefiles|parquet)
type='fixed'     # (fixed|mobile)
yyyy="${year}"   # 2020
Q='1'     # 1,2,3 (to date)

logit "Starting data pull for year ${year}. This may take some time."

# Iterate through each quarter in the year
for i in {1..4}; do 
  logit "Pulling data for quarter ${i}"
  quarter=$i
  aws s3 cp s3://ookla-open-data/${format}/performance/type=${type}/year=${yyyy}/quarter=${quarter}/ ./data \
  --recursive \
  --no-sign-request
done

# Compute execution time
end=`date +%s`
runtime=$((end-start))

logit "Data pull complete. Execution Time: ${runtime} seconds"
logit "Resulting parquet files can be found in the ./data folder"
