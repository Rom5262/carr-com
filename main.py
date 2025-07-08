
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
    grafico_reorden_por_departamento, # ¡IMPORTANTE: ESTA COMA ES NECESARIA!
)

# --- Configuración de la página de Streamlit ---
st.set_page_config(
    page_title="Análisis de Datos de Instacart",
    layout="wide", # Usa todo el ancho de la pantalla
    initial_sidebar_state="expanded"
)

st.title("🛒 Análisis de Datos de Instacart")
st.markdown("Explora patrones de compra y comportamiento de usuarios en Instacart.")

# --- Carga y Limpieza de Datos (Cacheada para eficiencia) ---
@st.cache_data(show_spinner="Cargando y limpiando datos... Esto puede tardar unos segundos.")
def load_and_clean_data():
    try:
        # 📂 Carga de datos
        # Asegúrate que la carpeta se llama 'datos' (todo en minúsculas) y los CSVs están dentro.
        # Volvemos a nrows=1000, si tienes problemas de rendimiento, puedes bajarlo a 500 o 100
        orders = pd.read_csv('datos/instacart_orders.csv', sep=';', nrows=1000) # Cargar solo 1,000 filas
        order_products = pd.read_csv('datos/order_products.csv', sep=';', nrows=1000) # Cargar solo 1,000 filas
        products = pd.read_csv('datos/products.csv', sep=';')
        departments = pd.read_csv('datos/departments.csv', sep=';')
        aisles = pd.read_csv('datos/aisles.csv', sep=';')
        
        # 🧼 Limpieza básica (usando la versión simplificada de limpieza.py)
        orders = limpieza_general(orders)
        order_products = limpieza_general(order_products)
        products = limpieza_general(products)
        departments = limpieza_general(departments)
        # aisles no se está usando actualmente en los gráficos, pero se puede limpiar si es necesario.
        
        return orders, order_products, products, departments, aisles
    
    except FileNotFoundError as e:
        st.error(f"Error: Uno de los archivos de datos no fue encontrado. Por favor, asegúrate de que todos los CSVs están en la carpeta 'datos/' dentro de tu repositorio de GitHub. Detalle: {e}")
        st.stop() # Detiene la ejecución de Streamlit si faltan archivos críticos
    except Exception as e:
        st.error(f"Ocurrió un error inesperado al cargar o limpiar los datos. Por favor, revise los logs del servidor para más detalles. Detalle: {e}")
        st.stop()

# Cargar y limpiar datos una sola vez gracias a @st.cache_data
orders, order_products, products, departments, aisles = load_and_clean_data()

# --- Función Auxiliar para Mostrar Gráficos de Forma Segura ---
def display_chart_section(chart_func, *args, title_text):
    """
    Muestra un gráfico en un expander de Streamlit, con manejo de errores.
    Cierra la figura de Matplotlib después de mostrarla para liberar memoria.
    """
    with st.expander(f"📊 {title_text}"):
        st.subheader(title_text)
        try:
            # Llama a la función de gráfico y obtiene la figura
            fig = chart_func(*args)
            
            if fig:
                st.pyplot(fig)
            else:
                st.warning(f"No se pudo generar el gráfico '{title_text}'. Esto podría deberse a datos faltantes o a un problema en la función del gráfico.")
        except Exception as e:
            st.error(f"Se produjo un error inesperado al generar el gráfico '{title_text}': {e}")
            st.info("Por favor, revise los logs del servidor en Render para obtener más detalles sobre este error específico.")
        finally:
            # Importante: Cerrar la figura de Matplotlib para liberar memoria
            # Esto es CRÍTICO en Streamlit para evitar advertencias y fugas de memoria
            plt.close('all')

# --- Secciones de Visualizaciones ---
st.header("Análisis de Órdenes y Comportamiento General")

display_chart_section(grafico_ordenes_por_hora, orders, title_text="Usuarios que hacen órdenes por hora del día")
display_chart_section(grafico_histograma_por_hora, orders, title_text="Distribución de órdenes por hora del día")
display_chart_section(grafico_ordenes_por_dia, orders, title_text="Usuarios que hacen compras por día de la semana")
display_chart_section(grafico_histograma_por_dia, orders, title_text="Distribución de compras por día de la semana")
display_chart_section(grafico_tiempo_entre_pedidos, orders, title_text="Tiempo transcurrido entre pedidos")
display_chart_section(grafico_comparativo_miercoles_sabado, orders, title_text="Comparativa de pedidos por hora: Miércoles vs Sábado")
display_chart_section(grafico_ordenes_por_cliente, orders, title_text="Distribución de órdenes por cliente")

st.header("Análisis de Productos")

display_chart_section(grafico_top_productos, order_products, products, title_text="Top 20 Productos Más Comprados")
display_chart_section(grafico_top_reordenados, order_products, products, 20, "horizontal", title_text="Top 20 Productos Más Reordenados")
display_chart_section(grafico_reorden_por_departamento, order_products, products, departments, title_text="Ratio de Reorden por Departamento")

st.markdown("---")
st.info("Análisis de datos de Instacart completado. Para cualquier consulta, revise las secciones anteriores.")
st.caption("Aplicación desarrollada con Streamlit.")
