import pandas as pd
import xlrd
dfs = pd.read_html('https://en.wikipedia.org/wiki/List_of_European_cities_by_population_within_city_limits')

df = dfs[0]
dfs = pd.read_html('https://www.nasdaq.com/symbol/amzn/historical')
df = dfs[2]

i = df.iloc[:, 1].idxmax()
df.iloc[i]