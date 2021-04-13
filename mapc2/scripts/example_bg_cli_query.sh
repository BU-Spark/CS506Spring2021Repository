#!/bin/bash
bq query --use_legacy_sql=false \
'SELECT
  a.TestTime AS TestTime,
  NET.SAFE_IP_FROM_STRING (client.IP) AS ip,
  a.MeanThroughputMbps AS MeanThroughputMbps,
  a.MinRTT AS MinRTT,
  client.Geo.city AS City,
  client.Geo.Latitude AS Latitude,
  client.Geo.Longitude AS Longitude,
  client.Network.ASNumber AS ProviderNumber,
  client.Network.ASName AS ProviderName
FROM
  `measurement-lab.ndt.unified_uploads`
WHERE
  client.geo.CountryCode = "US"
  AND client.Geo.region = "MA"
  AND date BETWEEN "2020-10-01"
  AND "2020-10-01"
  AND a.TestTime BETWEEN TIMESTAMP("2020-10-01 12:00:00.000", "UTC")
  AND TIMESTAMP("2020-10-01 12:30:00.000", "UTC")'