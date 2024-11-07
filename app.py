# importar las librerias
import streamlit as st
import pandas as pd
import plotly.express as px

# leer los datos para histograma
car_data = pd.read_csv('vehicles_us.csv')
# crear un boton
hist_button = st.button('Contruir un histograma')

# configurar el boto
if hist_button:
    st.write('Creacion de un histograma para los datos de odómetro')

    # crear un histograma
    fig = px.histogram(car_data, x='odometer')

    # mostrar un grafico plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


#Crear grafico de dispersion
#leer los datos para grafica de dispersion
car_data2 = pd.read_csv('vehicles_us.csv')

#crear un boton
scatter_button = st.button('Construir un gráfico de dispersión')

#configurar el boton
if scatter_button:
    st.write('Creación de un gráfico de dispersión para datos de odómetro')

    #creación del gráfico de dispersión
    fig2 = px.scatter_3d(car_data2, x='odometer')

    #mostrar el grafico en plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)
    

