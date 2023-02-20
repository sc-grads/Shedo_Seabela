import pandas as pd

df = pd.read_csv('countries_of_the_world.csv',
                 delimiter=',')

df.info()


pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)

df.head()
df.head(10)


df[df['Population'] > 100_000_000][['Country', 'Population', 'Area (sq. mi.)']]


df[df['Population'] > 100_000_000][['Country', 'Population', 'Area (sq. mi.)']].sort_values('Population',
                                                                                            ascending=False)

x = df['GDP ($ per capita)'].idxmax()
df.iloc[x]


region = df['Region'].str.strip().isin(['EASTERN EUROPE', 'WESTERN EUROPE'])  # this is a boolean series
df[region].sort_values('Population', ascending=False)

df.nlargest(3, 'Population')

df.nlargest(5, 'GDP ($ per capita)')

df.nlargest(n=2, columns='Birthrate')


df.nsmallest(5, 'Area (sq. mi.)')