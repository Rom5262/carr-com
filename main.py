import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
orders = pd.read_csv('instacart_orders.csv', sep=';')

# Agrupar por hora y contar usuarios
usuarios_por_hora = orders.groupby('order_hour_of_day')['user_id'].count()

# Crear gráfico
fig, ax = plt.subplots(figsize=(8, 4))
usuarios_por_hora.plot(
    ax=ax,
    marker='o',
    linestyle='-',
    color='b',
    grid=True
)

# Personalización
ax.set_title('Usuarios que hacen órdenes por hora del día')
ax.set_xlabel('Hora del Día')
ax.set_ylabel('Cantidad de Usuarios')

# Mostrar en Streamlit
st.pyplot(fig)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
orders = pd.read_csv('instacart_orders.csv', sep=';')

# Crear histograma con KDE
fig, ax = plt.subplots()
sns.histplot(data=orders, x='order_hour_of_day', kde=True, bins=24, ax=ax)

# Personalización
ax.set_title('Distribución de órdenes por hora del día')
ax.set_xlabel('Hora del Día')
ax.set_ylabel('Cantidad de Órdenes (Frecuencia)')
st.pyplot(fig)

