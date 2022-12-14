import pandas as pd

par1 = pd.read_parquet("data/green_tripdata_2021-01.parquet")
csv_output_1 = 'data/january.csv'
par1.to_csv(csv_output_1, index=False)

par2 = pd.read_parquet("data/green_tripdata_2021-02.parquet")
csv_output_2 = 'data/february.csv'
par1.to_csv(csv_output_2, index=False)

df1 = pd.read_csv("data/january.csv")
print(df1.head())


print(df1.columns)