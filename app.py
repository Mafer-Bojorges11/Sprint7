import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('AUTOS')
hist_button = st.checkbox('Construir histograma')

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.checkbox('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfica de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig_2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_2, use_container_width=True)
