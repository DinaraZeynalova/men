import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='week8_streamlit')
st.header('Welcome to week 8')

df=pd.read_csv('water_potability.csv')
df=df.dropna()
st.dataframe(df)

chart =px.scatter(df,
                       
                   x='Chloramines',
                   y='Hardness',
                   color='Potability',
                   title='Scatter Plot')

st.plotly_chart(chart)
