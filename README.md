
# 🛒 Proyecto: Carro de Compras

### Análisis del comportamiento de pedidos en Instacart

Este proyecto explora un conjunto de datos modificado de Instacart, una plataforma de entrega de comestibles. El objetivo es entender qué productos se compran más, cuándo y con qué frecuencia los usuarios hacen pedidos. Utilizamos herramientas como **Python**, **Pandas**, **NumPy**, **Matplotlib**, **Seaborn** y **Streamlit** para visualizar estos insights en un dashboard interactivo.

---

## 🌐 Dashboard Interactivo

Desarrollado con **Streamlit**, este panel permite explorar el comportamiento de los clientes, incluyendo:

- Productos más solicitados 🛒
- Horarios y días de mayor actividad 📊
- Frecuencia de reordenación 🔄

👉 Ver aplicación desplegada en Render: 

Ideal para analistas, equipos de marketing o quienes buscan comprender los patrones de consumo en servicios de entrega.

---

## 🚀 Funcionalidades Clave

- 📌 Preprocesamiento de datos: manejo de nulos y duplicados.
- 📌 Análisis exploratorio (EDA): patrones por hora, día, reordenación.
- 📌 Visualización interactiva: dashboards claros y dinámicos.
- 📌 Despliegue en la nube: acceso fácil desde cualquier lugar.

---

## 📁 Estructura del Proyecto

- `notebooks/`: Jupyter Notebooks por fase.
- `data/`: Archivos CSV del dataset original.
- `main.py`: Script principal de Streamlit.
- `requirements.txt`: Dependencias del proyecto.
- `README.md`: Este archivo.

---

## 📊 Módulos de Análisis

### 📈 Patrones de Pedido

- Usuarios activos por hora del día (línea)
- Frecuencia de pedidos por hora (histograma)
- Actividad por día de la semana (línea e histograma)
- Intervalo entre pedidos consecutivos
- Comparativa miércoles vs sábado
- Distribución de pedidos por cliente

### 🛍️ Comportamiento del Producto

- Top 20 productos más comprados
- Productos más reordenados (con slider)
- Violin plots por producto y departamento

---

## 💻 Tecnologías Utilizadas

- Python · Pandas · NumPy  
- Matplotlib · Seaborn · Streamlit  
- Render (para el despliegue)  
- `calendar` (librería estándar)

---

## 📂 Datos

Datos modificados de Instacart:

- `instacart_orders.csv`
- `order_products.csv`
- `products.csv`
- `departments.csv`

Se simularon condiciones reales (valores nulos y duplicados) manteniendo la integridad de las distribuciones originales.

---

## ✒️ Autor

- [Román](https://github.com/Rom5262)
