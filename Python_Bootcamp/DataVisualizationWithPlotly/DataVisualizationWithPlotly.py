import plotly.offline as pyo
import plotly.graph_objs as go

import random

pyo.init_notebook_mode()
x_values = [random.randrange(0, 20) for n in range(50)]
y_values = [random.randrange(-10, 10) for n in range(50)]

data = [go.Scatter(x=x_values, y=y_values, mode='markers')]


pyo.plot(data, filename='scatter_plot.html')


import pandas as pd

df = pd.read_csv('houses.csv')


x_values = df['GroundLivingArea']
y_values = df.SalePrice

data = [go.Scatter(x=x_values, y=y_values, mode='markers')]
pyo.iplot(data)