
import streamlit as st
import pandas as pd

# 👇 Importa funciones desde utilidad
from utilidad.limpieza import limpieza_general
from utilidad.graficos import (
    grafico_ordenes_por_hora,
    grafico_histograma_por_hora,
    grafico_ordenes_por_dia,
    grafico_histograma_por_dia,
    grafico_tiempo_entre_pedidos,
    grafico_comparativo_miercoles_sabado,
    grafico_ordenes_por_cliente,
    grafico_top_productos,
    grafico_top_reordenados,
    grafico_reorden_por_departamento
)

# 📂 Carga de datos
orders = pd.read_csv('instacart_orders.csv', sep=';')
order_products = pd.read_csv('order_products.csv', sep=';')
products = pd.read_csv('products.csv', sep=';')
departments = pd.read_csv('departments.csv', sep=';')
aisles = pd.read_csv('aisles.csv', sep=';')

# 🧼 Limpieza básica
orders = limpieza_general(orders)
order_products = limpieza_general(order_products)
products = limpieza_general(products)
departments = limpieza_general(departments)

# 🎨 Visualizaciones
with st.expander("📊 Órdenes por hora del día"):
    fig = grafico_ordenes_por_hora(orders)
    st.pyplot(fig)

with st.expander("📊 Histograma de órdenes por hora"):
    fig = grafico_histograma_por_hora(orders)
    st.pyplot(fig)

with st.expander("📊 Órdenes por día de la semana"):
    fig = grafico_ordenes_por_dia(orders)
    st.pyplot(fig)

with st.expander("📊 Histograma de compras por día"):
    fig = grafico_histograma_por_dia(orders)
    st.pyplot(fig)

with st.expander("📊 Tiempo entre pedidos"):
    fig = grafico_tiempo_entre_pedidos(orders)
    st.pyplot(fig)

with st.expander("📊 Pedidos por hora en miércoles vs sábado"):
    fig = grafico_comparativo_miercoles_sabado(orders)
    st.pyplot(fig)

with st.expander("📊 Órdenes por cliente"):
    fig = grafico_ordenes_por_cliente(orders)
    st.pyplot(fig)

with st.expander("📊 Top 20 productos más comprados"):
    fig = grafico_top_productos(order_products, products)
    st.pyplot(fig)

with st.expander("📊 Productos más reordenados"):
    fig = grafico_top_reordenados(order_products, products)
    st.pyplot(fig)

with st.expander("📊 Reorden por departamento"):
    fig = grafico_reorden_por_departamento(order_products, products, departments)
    st.pyplot(fig)
