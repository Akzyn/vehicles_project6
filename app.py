# importar las librerias
import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Creando gráficos de venta de autos')

# leer los datos para histograma
car_data = pd.read_csv('vehicles_us.csv')
# crear un boton
hist_button = st.button('Construir un histograma')

# configurar el boto
if hist_button:
    st.write('Creación de un histograma para los datos de odómetro')

    # crear un histograma
    fig = px.histogram(car_data, x='odometer', labels={'x':'Odómetro', 'y':'millas'}, title='Histograma de odómetro', color_discrete_sequence=['indianred'])

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
    fig2 = px.scatter(car_data2, x='odometer', y='price', color={"paint_color":[nan: 'pink', 'white': 'white', 'red': 'red', 'black': 'black', 'blue': 'blue', 'grey':'grey', 'silver':'silver', 'custom':'custom', 'orange':'orange', 'yellow':'yellow', 'brown':'brown', 'green':'green', 'purple':'purple']}, 
                      labels={'x':'Odómetro', 'y':'Precio'}, title="Precio de autos clasificados por color basados por odómetro")

    #mostrar el grafico en plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)
    

ask_customer = st.checkbox('¿Te ha sido útil esta información?, Dar clic en la casilla para afirmar')

if ask_customer: # si la casilla de verificación está seleccionada
    st.write('Gracias por su tiempo :P')
