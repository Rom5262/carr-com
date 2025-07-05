import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

# Configuración visual
sns.set_style("whitegrid")

# Cargar datos
order_products = pd.read_csv('order_products.csv', sep=';')
products = pd.read_csv('products.csv', sep=';')

# Agrupar y preparar top N productos
most_reordered = order_products.groupby('product_id')['reordered'].sum().reset_index()
most_reordered = most_reordered.sort_values(by='reordered', ascending=False)
most_reordered = most_reordered.merge(products[['product_id', 'product_name']], on='product_id', how='left')

# 🎚️ Interactividad
top_n = st.slider("Cantidad de productos a mostrar", min_value=5, max_value=50, value=20, step=5)
tipo = st.radio("Tipo de gráfico", ["Horizontal", "Vertical"])

# Subset de datos
top_products = most_reordered.head(top_n)

# 🎨 Crear degradado de color
palette = sns.color_palette('Blues_r', len(top_products))

# 📊 Crear gráfico
fig, ax = plt.subplots(figsize=(10, 6))

if tipo == "Horizontal":
    sns.barplot(data=top_products, x='reordered', y='product_name', ax=ax, palette=palette)
    for bar in ax.patches:
        ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
                str(int(bar.get_width())), va='center', fontsize=9)
    ax.set_xlabel("Cantidad de Reordenes")
    ax.set_ylabel("Nombre del Producto")
else:
    sns.barplot(data=top_products, x='product_name', y='reordered', ax=ax, palette=palette)
    for bar in ax.patches:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                str(int(bar.get_height())), ha='center', fontsize=9)
    ax.set_ylabel("Cantidad de Reordenes")
    ax.set_xlabel("Nombre del Producto")
    plt.xticks(rotation=45)

# 🏷️ Título
ax.set_title(f"Top {top_n} Productos Reordenados")

# 🖼️ Mostrar en Streamlit
st.pyplot(fig)


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
order_products = pd.read_csv('order_products.csv', sep=';')
products = pd.read_csv('products.csv', sep=';')

# Calcular reorder ratio por producto
reorder_ratio = order_products.groupby('product_id')['reordered'].mean().reset_index()
reorder_ratio.columns = ['product_id', 'reorder_ratio']

# Unir con productos
merged = reorder_ratio.merge(products[['product_id', 'product_name']], on='product_id', how='left')

# Seleccionar los top N productos
top_n = st.slider("Ver top productos más reordenados", min_value=5, max_value=50, value=20)
top_products = merged.sort_values(by='reorder_ratio', ascending=False).head(top_n)

# Crear gráfico violinplot por producto
fig, ax = plt.subplots(figsize=(14, 6))
sns.violinplot(data=top_products, x='product_name', y='reorder_ratio', palette='coolwarm', ax=ax)


# Personalización
ax.set_title('Producto Reordenado')
ax.set_xlabel('Producto')
ax.set_ylabel('Reorden')
plt.xticks(rotation=45)
fig.tight_layout()

# Mostrar en Streamlit
st.pyplot(fig)



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
order_products = pd.read_csv('order_products.csv', sep=';')
products = pd.read_csv('products.csv', sep=';')
departments = pd.read_csv('departments.csv', sep=';')

# Calcular reorder ratio por producto
reorder_ratio = order_products.groupby('product_id')['reordered'].mean().reset_index()
reorder_ratio.columns = ['product_id', 'reorder_ratio']

# Unir con productos y departamentos
merged = reorder_ratio.merge(products[['product_id', 'department_id']], on='product_id', how='left')
merged = merged.merge(departments, on='department_id', how='left')  # Junta con los nombres reales

# Crear gráfico violinplot
fig, ax = plt.subplots(figsize=(14, 6))
sns.violinplot(data=merged, x='department', y='reorder_ratio', palette='coolwarm', ax=ax)

# Personalización
ax.set_title('Reordenado de Productos por Departamento')
ax.set_xlabel('Departamento')
ax.set_ylabel('Reordenes')
plt.xticks(rotation=45)
fig.tight_layout()

# Mostrar en Streamlit
st.pyplot(fig)


