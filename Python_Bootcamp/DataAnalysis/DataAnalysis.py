import pandas as pd
import xlrd

df = pd.read_excel('salaries.xlsx', sheet_name='Sheet1')


df['Salary'].mean()
df['Salary'].max()
df['Salary'].min()
df['Salary'].count()
df['Salary'].std()
df['Country'].unique()
df['Country'].nunique()

df['Country'].value_counts()

df.sort_values('Salary', ascending=False)

c = df.groupby('Country')

c.max()
c.min()
c.sum()
c.mean()
c.std()
df1 = c.max()
df1.loc['UK']
df.groupby('Country').min().loc['USA']
df.groupby('Country').describe()
df.groupby('Country').describe().transpose()