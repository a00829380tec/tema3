import pandas as pd
import streamlit as st
import plotly.express as px

url = "https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv"

df = pd.read_csv(url)
df = df.sort_values('Order Date')

st.title("Tema 3")
st.header("Gráficas en Streamlit")
st.caption("En los retos de los módulos previos, trabajaste con los datos provistos en el Hackathon HackerEarth 2020, tomando como hipótesis que esta información resultará explicativa del fenómeno de deserción laboral que tanto afecta en la actualidad a las empresas y organizaciones.")

fig = px.line(df, x='Order Date', y="Profit", title='Profit vs. Order Date')
st.write(fig)