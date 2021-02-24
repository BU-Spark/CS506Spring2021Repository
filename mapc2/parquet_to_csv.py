import pandas as pd
df = pd.read_parquet('/Users/adamstreich/Desktop/data506')
df.to_csv('/Users/adamstreich/Desktop/data506MOD.csv')