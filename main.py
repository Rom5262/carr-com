import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---                                    ---
st.set_page_config(
    page_title="Análisis de Órdenes ",
    page_icon="🛒",
    layout="wide"
)

st.title("Análisis de Usuarios por Hora del Día")
st.write("Esta aplicación visualiza el número de usuarios que realizan pedidos en diferentes horas del día.")

# ¡IMPORTANTE! Se usa sep=';' para leer el archivo CSV
try:
    orders = pd.read_csv('instacart_orders.csv', sep=';')
    st.success("Archivo 'instacart_orders.csv' cargado exitosamente con separador ';'.")
except FileNotFoundError:
    st.error("Error: El archivo 'instacart_orders.csv' no se encontró.")
    st.error("Por favor, asegúrate de que esté en la misma carpeta que 'main.py'.")
    st.stop() # Detiene la ejecución si el archivo no se encuentra
except Exception as e:
    st.error(f"Error al leer 'instacart_orders.csv': {e}")
    st.error("Verifica el formato del archivo y el separador (debe ser ';').")
    st.stop()


st.write("---")
st.subheader("Gráfico de Usuarios por Hora del Día")


# Crea una figura y un eje para el gráfico de Matplotlib.
fig, ax = plt.subplots(figsize=(8, 4))

# Aplica tu código de gráfico al eje 'ax'
orders.groupby('order_hour_of_day')['user_id'].count().plot(
    ax=ax, # ¡Importante! Dibuja en el eje 'ax'
    marker='o',
    linestyle='-',
    color='b',
    title='Usuarios por Hora del Día',
    xlabel='Hora del Día',
    ylabel='Código Usuario',
    grid=True
)

# Muestra el gráfico de Matplotlib en Streamlit
st.pyplot(fig)

st.write("---")
st.info("¡Análisis de órdenes completado!")
