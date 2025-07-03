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

# Cargar datos
orders = pd.read_csv('instacart_orders.csv', sep=';')

# Crear gráfico
fig, ax = plt.subplots()

# Histograma sin KDE
sns.histplot(
    data=orders,
    x='order_hour_of_day',
    bins=24,
    ax=ax,
    color='orange'
)


# Personalización
ax.set_title('Distribución de órdenes por hora del día')
ax.set_xlabel('Hora del Día')
ax.set_ylabel('Frecuencia')
st.pyplot(fig)


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
orders = pd.read_csv('instacart_orders.csv', sep=';')

# Agrupar por hora y contar usuarios
usuarios_por_dia = orders.groupby('order_dow')['user_id'].count()

# Crear gráfico
fig, ax = plt.subplots(figsize=(8, 4))
usuarios_por_dia.plot(
    ax=ax,
    marker='o',
    linestyle='-',
    color='b',
    grid=True
)

# Personalización
ax.set_title('Usuarios que hacen compras por dia')
ax.set_xlabel('Día de la Semana')
ax.set_ylabel('Usuarios por día')

# Mostrar en Streamlit
st.pyplot(fig)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar

# Cargar datos
orders = pd.read_csv('instacart_orders.csv', sep=';')

# Crear gráfico
fig, ax = plt.subplots()

# Histograma con 7 bins (uno por cada día)
sns.histplot(
    data=orders,
    x='order_dow',
    bins=7,  # Uno por cada día (0-6)
    ax=ax,
    color='orange'
)

# Personalización
ax.set_title('Compras por día de la Semana')
ax.set_xlabel('Día de la Semana')
ax.set_ylabel('Usuarios por Día')
ax.set_xticks(range(7))  # Posiciones de las etiquetas
ax.set_xticklabels(calendar.day_name[:7])  # Etiquetas con nombres de los días

# Mostrar gráfico en Streamlit
st.pyplot(fig)
