import pandas as pd

data_url = "https://raw.githubusercontent.com/alstat/Analysis-with-Programming/master/2014/Python/Numerical-Descriptions-of-the-Data/data.csv"
df = pd.read_csv(data_url)

print(df.head())  # print first 5 rows
# print(df.tail())  # print last 5 rows
# print(df.tail(n=10))  # set num of rows
print(df.columns)  # colnames  , df.index = rownames
print(df.T)  # transpose
