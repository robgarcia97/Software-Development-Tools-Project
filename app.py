import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Car Sales Dashboard')
df = pd.read_csv('vehicles_us.csv')

st.header('Price Distribution')
fig_hist = px.histogram(df, x='price')
st.plotly_chart(fig_hist)

st.header('Odometer vs Price')
fig_scatter = px.scatter(df, x='odometer', y='price')
st.plotly_chart(fig_scatter)

if st.checkbox('Show Raw Data'):
    st.write(df)
