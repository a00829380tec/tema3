import pandas as pd
import streamlit as st

url = "https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv"

df = pd.read_csv(url)

st.title("Tema 2")
st.header("Interacción con otros componentes")
st.caption("En los retos de los módulos previos, trabajaste con los datos provistos en el Hackathon HackerEarth 2020, tomando como hipótesis que esta información resultará explicativa del fenómeno de deserción laboral que tanto afecta en la actualidad a las empresas y organizaciones.")
st.slider("Ejemplo de slider")
st.radio("Ejemplo de radio", ["Ejemplo de radio 1","Ejemplo de radio 2"])
st.selectbox("Ejemplo de selectbox", ["Ejemplo de selectbox 1","Ejemplo de selectbox 2"])