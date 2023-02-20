import plotly.offline as pyo
import plotly.graph_objs as go
import random

pyo.init_notebook_mode()
x_values = [random.randint(1, 100) for n in range(100)]

data = [go.Histogram(x=x_values)]
layout = go.Layout(title='Simple Histogram')
fig = go.Figure(data, layout)

pyo.iplot(fig)
import pandas as pd

df = pd.read_csv('monthly_salary.csv')
x_values = df['Monthly Salary']
data = [go.Histogram(x=x_values, xbins=dict(start=3000, end=5000, size=100))]

layout = go.Layout(title='Histogram of Monthly Salary')
fig = go.Figure(data, layout)
pyo.iplot(fig)