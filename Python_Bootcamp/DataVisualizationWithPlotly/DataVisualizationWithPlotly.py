import plotly.offline as pyo
import plotly.graph_objs as go

pyo.init_notebook_mode()

labels = ['Nitrogen', 'Oxygen', 'Other']
values = [78.09, 20.95, 0.96]
my_colors = ['#0066cc', '#ffd700', '#dc0000']

data = [go.Pie(labels=labels, values=values, marker=dict(colors=my_colors))]

layout = go.Layout(title='Air Composition')
fig = go.Figure(data, layout)

pyo.iplot(fig)
import pandas as pd

df = pd.read_html('https://en.wikipedia.org/wiki/List_of_continents_by_population')
type(df[0])
t1 = df[0]
labels = t1.loc[1:, 'Continent']
values = t1.loc[1:, '% of world pop.']
values[7] = values[7].lstrip('<')

data = [go.Pie(labels=labels, values=values)]

layout = go.Layout(title='World Population By Continent, 2016')
fig = go.Figure(data, layout)

pyo.iplot(fig)

