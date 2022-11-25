import streamlit as st
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from streamlit_plotly_events import plotly_events
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/jonmmease/plotly_ipywidget_notebooks/master/notebooks/data/cars/cars.csv')

xaxis = st.selectbox("x axis", options=df.select_dtypes('int64').columns)
yaxis = st.selectbox("y axis", options=df.select_dtypes('int64').columns)

fig = make_subplots(
    rows=2, cols=1,
    vertical_spacing=0.03,
    specs=[[{"type": "scatter"}],
           [{"type": "table"}]]
    )

fig.add_trace(
    go.Scatter(x=df[xaxis], y=df[yaxis], mode='markers'),
    row=1, col=1
    )

fig.add_trace(
    go.Table(
        header=dict(values=['ID','Classification','Driveline','Hybrid'],
                    fill = dict(color='#C2D4FF'),
                    align = ['left'] * 5),
        cells=dict(values=[df[col] for col in ['ID','Classification','Driveline','Hybrid']],
                fill = dict(color='#F5F8FF'),
                align = ['left'] * 5)),
    row=2, col=1
    )

fig.update_layout(height=800, title_text="Plot with table")
st.plotly_chart(fig)

selection = plotly_events(fig, override_height=800, select_event=True)
st.write(selection)
