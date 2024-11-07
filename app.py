# importar las librerias
import streamlit as st
import pandas as pd
import plotly.express as px

# leer los datos
car_data = pd.read_csv(
    'E:/Tripleten/Sprint 6/Proyecto6/vehicles_project6/vehicles_us.csv')
# crear un boton
hist_button = st.button('Contruir un histograma')

# configurar el boto
if hist_button:
    st.write(
        'Creacion de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x='odometer')

    # mostrar un grafico plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
