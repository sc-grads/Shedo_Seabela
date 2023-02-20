import plotly.offline as pyo
import plotly.graph_objs as go
import random

pyo.init_notebook_mode()

x_values = list(range(50))
y_values = [random.randrange(20, 25) for x in range(50)]
trace1 = go.Scatter(x=x_values, y=y_values, mode='lines', name='Just Lines')

y_values = [random.randrange(15, 20) for x in range(50)]
trace2 = go.Scatter(x=x_values, y=y_values, mode='markers', name='Just Markers')

y_values = [random.randrange(10, 15) for x in range(50)]
trace3 = go.Scatter(x=x_values, y=y_values, mode='lines+markers', name='Markers and Lines')

data = [trace1, trace2, trace3]
layout = go.Layout(title='Simple Line Chart',
                   xaxis={'title': 'This is the X Axis'},
                   yaxis=dict(title='This is the Y Asis')
                   )

fig = go.Figure(data=data, layout=layout)

pyo.iplot(fig)

import pandas as pd

df = pd.read_csv('gold_annual_price.csv')

trace = go.Scatter(x=df.Date, y=df.Price, mode='lines', name='Gold Price')

data = [trace]
layout = go.Layout(title='Gold Monthly Price (1950-2019)')
fig = go.Figure(data=data, layout=layout)

pyo.iplot(fig)