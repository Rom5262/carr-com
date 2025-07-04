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


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
orders = pd.read_csv('instacart_orders.csv', sep=';')
order_client = orders['user_id'].value_counts()

# Crear gráfico
fig, ax = plt.subplots()

# Histograma en color rosa
sns.histplot(
    order_client,
    bins=24,
    ax=ax,
    color='#FF69B4'  # Rosa fuerte tipo HotPink
)

# Personalización
ax.set_title('Distribución de Número de Ordenes por Cliente')
ax.set_xlabel('Cantidad de Ordenes')
ax.set_ylabel('Número de Clientes')

# Mostrar en Streamlit
st.pyplot(fig)


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
orders = pd.read_csv('instacart_orders.csv', sep=';')
order_products = pd.read_csv('order_products.csv', sep=';')
products = pd.read_csv('products.csv', sep=';')


# Agrupar productos por cantidad de compras
count_products = order_products.groupby('product_id').size().reset_index(name='more_purchased')
popular_products = count_products.merge(products, on='product_id', how='left')
top_20_products = popular_products.sort_values(by='more_purchased', ascending=False).head(20)

# Crear gráfico
fig, ax = plt.subplots()

# Gráfico de barras horizontal en verde
sns.barplot(
    y=top_20_products['product_name'],
    x=top_20_products['more_purchased'],
    ax=ax,
    palette=['#32CD32'] * len(top_20_products)  # Verde tipo LimeGreen para cada barra
)

# Personalización
ax.set_title('Los 20 Productos Más Populares')
ax.set_xlabel('Cantidad de Compras')
ax.set_ylabel('Nombre del Producto')

# Mostrar en Streamlit
st.pyplot(fig)


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
order_products = pd.read_csv('order_products.csv', sep=';')

# Agrupar para contar artículos por pedido
articles = order_products.groupby('order_id').size()

# Crear gráfico
fig, ax = plt.subplots()

# Histograma en azul celeste
sns.histplot(
    articles,
    bins=30,
    ax=ax,
    color='#00BFFF'  # DeepSkyBlue
)

# Personalización
ax.set_title('Distribución de Artículos por Pedido')
ax.set_xlabel('Cantidad de Artículos')
ax.set_ylabel('Frecuencia')

# Mostrar en Streamlit
st.pyplot(fig)
