import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('vehicles_us.csv')

# Preprocessing
df['model_year'] = df.groupby('model')['model_year'].transform(lambda x: x.fillna(x.median()))
df['cylinders'] = df.groupby('model')['cylinders'].transform(lambda x: x.fillna(x.median()))
df['odometer'] = df.groupby(['model', 'model_year'])['odometer'].transform(lambda x: x.fillna(x.mean()))

# Remove outliers
q_low = df['model_year'].quantile(0.01)
q_high = df['model_year'].quantile(0.99)
df = df[(df['model_year'] > q_low) & (df['model_year'] < q_high)]

q_low = df['price'].quantile(0.01)
q_high = df['price'].quantile(0.99)
df = df[(df['price'] > q_low) & (df['price'] < q_high)]

# Streamlit app
st.title('Car Sales Advertisements Dashboard')

st.header('Distribution of Car Prices')
fig = px.histogram(df, x='price', title='Distribution of Car Prices')
st.plotly_chart(fig)

st.header('Price vs. Odometer')
fig = px.scatter(df, x='odometer', y='price', title='Price vs. Odometer')
st.plotly_chart(fig)

st.header('Price vs. Model Year')
fig = px.scatter(df, x='model_year', y='price', title='Price vs. Model Year')
st.plotly_chart(fig)

if st.checkbox('Show Raw Data'):
    st.subheader('Raw Data')
    st.write(df)
