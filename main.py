
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt # Importar explícitamente por si alguna función de grafico no lo hace
import seaborn as sns # Importar explícitamente por si alguna función de grafico no lo hace

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
        # Nota: Asegúrate de que estos CSVs están en el mismo directorio que main.py en GitHub
        orders = pd.read_csv('instacart_orders.csv', sep=';')
        order_products = pd.read_csv('order_products.csv', sep=';')
        products = pd.read_csv('products.csv', sep=';')
        departments = pd.read_csv('departments.csv', sep=';')
        aisles = pd.read_csv('aisles.csv', sep=';')

        # 🧼 Limpieza básica
        # st.info("Aplicando limpieza básica a los DataFrames...") # Puedes comentar esta línea si no quieres que aparezca en la UI
        orders = limpieza_general(orders)
        order_products = limpieza_general(order_products)
        products = limpieza_general(products)
        departments = limpieza_general(departments)
        # aisles no se está usando actualmente en los gráficos proporcionados, pero se puede limpiar si es necesario.
        
        # Opcional: Optimización de tipos de datos para reducir uso de memoria
        # Solo si los archivos son muy grandes y experimentas problemas de memoria
        # orders['order_dow'] = orders['order_dow'].astype('int8')
        # orders['order_hour_of_day'] = orders['order_hour_of_day'].astype('int8')
        # orders['days_since_prior_order'] = orders['days_since_prior_order'].astype('float16')
        # orders['user_id'] = orders['user_id'].astype('int32')
        # order_products['reordered'] = order_products['reordered'].astype('bool')

        return orders, order_products, products, departments, aisles # Incluimos aisles por si lo usas más tarde
    
    except FileNotFoundError as e:
        st.error(f"Error: Uno de los archivos de datos no fue encontrado. Por favor, asegúrate de que todos los CSVs están en el mismo directorio que main.py en tu repositorio de GitHub. Detalle: {e}")
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
            st.info("""Por favor, revise los logs del servidor para más detalles.
         Este mensaje puede aparecer si el gráfico no se generó correctamente.""")
            
