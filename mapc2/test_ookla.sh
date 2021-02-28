#!/bin/bash
export FORMAT='parquet' # (shapefiles|parquet)
export TYPE='fixed'        # (fixed|mobile)
export YYYY='2020'         # 2020
export Q='1'               # 1,2,3 (to date)

aws s3 cp s3://ookla-open-data/${FORMAT}/performance/type=${TYPE}/year=${YYYY}/quarter=${Q}/ ./data \
--recursive \
--no-sign-request