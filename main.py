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


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
orders = pd.read_csv('instacart_orders.csv', sep=';')


Tiempo_espera = orders['days_since_prior_order'].value_counts().sort_index()

# Crear gráfico
fig, ax = plt.subplots(figsize=(8, 4))
Tiempo_espera.plot(
    ax=ax,
    marker='o',
    linestyle='-',
    color='b',
    grid=True
)

# Personalización
ax.set_title('Tiempo de Solicitud')
ax.set_xlabel('Día del Mes')
ax.set_ylabel('Codigo Usuario')

# Mostrar en Streamlit
st.pyplot(fig)


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
orders = pd.read_csv('instacart_orders.csv', sep=';')

# Filtrar datos por miércoles (3) y sábado (6)
dif_wed = orders[orders['order_dow'] == 3]
dif_sat = orders[orders['order_dow'] == 6]

# Conteo por hora
graphic_wed = dif_wed['order_hour_of_day'].value_counts().sort_index()
graphic_sat = dif_sat['order_hour_of_day'].value_counts().sort_index()

# Unir los conteos en un solo DataFrame
graphic_dif_w_s = pd.concat([graphic_wed, graphic_sat], axis=1)
graphic_dif_w_s.columns = ['wednesday', 'saturday']

# Crear gráfico de barras
fig, ax = plt.subplots(figsize=(10, 5))
graphic_dif_w_s.plot(kind='bar', ax=ax, color=['skyblue', 'orange'])

# Personalización
ax.set_title('Diferencia de Pedidos por Hora del Día')
ax.set_xlabel('Hora del Día')
ax.set_ylabel('Cantidad de Órdenes')
ax.legend(title='Día')

# Mostrar en Streamlit
st.pyplot(fig)

