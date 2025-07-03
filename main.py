import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Análisis de Órdenes", page_icon="🛒", layout="wide")
st.title("Usuarios por Hora del Día")
st.write("Visualización de pedidos según la hora.")


try:
    orders = pd.read_csv('instacart_orders.csv', sep=';')
    st.success("Archivo cargado con éxito.")
except FileNotFoundError:
    st.error("Archivo 'instacart_orders.csv' no encontrado.")
    st.stop()
except Exception as e:
    st.error(f"Error al leer el archivo: {e}")
    st.stop()

# Gráfico
fig, ax = plt.subplots(figsize=(8, 4))
orders['order_hour_of_day'].value_counts().sort_index().plot(
    ax=ax, marker='o', linestyle='-', color='b'
)
ax.set(title='Usuarios por Hora del Día', xlabel='Hora', ylabel='Cantidad de Usuarios', grid=True)
st.pyplot(fig)

st.info("¡Análisis completado!")
