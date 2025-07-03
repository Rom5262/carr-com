import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo CSV
orders = pd.read_csv('instacart_orders.csv', sep=';')

# Variable numérica fija
variable_numerica = 'order_hour_of_day'


# Crear el histograma con curva de densidad
fig, ax = plt.subplots()
sns.histplot(data=orders, x=variable_numerica, kde=True, ax=ax)
ax.set_title(f'Histograma de {variable_numerica}')
ax.set_xlabel('Hora del Día')
ax.set_ylabel('Código Usuario')
st.pyplot(fig)
