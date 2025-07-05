
🛒 PROYECTO: CARRO DE COMPRAS.

 Análisis del Comportamiento de Pedidos en Instacart
________________________________________
Análisis de una plataforma que entrega productos comestibles, en donde la clientela puede registrar un pedido y hacer que se lo entreguen.
________________________________________
En este proyecto, exploramos y analizamos un conjunto de datos modificado de Instacart, una plataforma de entrega de comestibles. Nuestro objetivo principal es entender el comportamiento de los usuarios: qué productos adquieren más, en qué días y a qué horas realizan sus compras, y cómo la plataforma maneja sus datos. Este análisis se realiza utilizando Python y bibliotecas clave como Pandas, NumPy, Matplotlib, Seaborn y Streamlit para la creación de un dashboard interactivo.
________________________________________
🌐 Dashboard Interactivo de Análisis de Pedidos
Este proyecto presenta un dashboard interactivo desarrollado con Streamlit, diseñado para ofrecer una exploración profunda del comportamiento de los usuarios al realizar sus pedidos en Instacart.
 A través de este dashboard, los usuarios pueden conocer los productos más solicitados, cuándo y a qué hora realizan sus pedidos, la frecuencia de reordenación y mucho más.
👉 Ver aplicación desplegada en Render ()
Ideal para analistas de datos, equipos de marketing o cualquier persona interesada en comprender la dinámica de los servicios de entrega de comestibles, el dashboard transforma datos complejos en insights accionables y fácilmente digeribles.
________________________________________
🚀 Funcionalidades Clave del Proyecto
________________________________________
Este proyecto se centra en:
📌 Preprocesamiento de Datos: Identificación y tratamiento de valores ausentes y duplicados para garantizar la calidad y fiabilidad del conjunto de datos.
📌 Análisis Exploratorio de Datos (EDA): Obtención de insights sobre el comportamiento de compra del cliente (productos populares, patrones de pedidos por día/hora, frecuencia de reordenación).
📌 Visualización de Datos Dinámica: Creación de gráficos claros y efectivos para comunicar los hallazgos clave a través de un dashboard interactivo.
📌 Despliegue Profesional: Implementación de un dashboard interactivo utilizando Streamlit y Render para un acceso sencillo y global.
________________________________________
📁 Estructura del Proyecto
•	notebooks/: Contiene el  Jupyter Notebook con el código para cada fase.
•	data/: Almacena el conjunto de datos de entrada (instacart_orders.csv, order_products.csv, products.csv, departments.csv).
•	main.py: El script principal de Streamlit que integra todas las visualizaciones.
•	requirements.txt: Archivo con las dependencias del proyecto.
•	README.md: Este archivo.
________________________________________
📊 Vistazo Rápido a los Análisis y Gráficos Clave
El dashboard interactivo y los scripts de análisis ofrecen diferentes perspectivas sobre los datos de pedidos de Instacart. A continuación, se destacan algunos de los análisis visuales más relevantes que puedes explorar:
📈 Módulo "Patrones de Pedido"
•	Usuarios que hacen órdenes por hora del día: Un gráfico de línea que muestra el volumen de usuarios activos por cada hora del día, identificando las horas pico de actividad.
•	Distribución de órdenes por hora del día: Un histograma que visualiza la frecuencia de pedidos a lo largo de las 24 horas del día.
•	Usuarios que hacen compras por día: Un gráfico de línea que muestra el conteo de usuarios que realizan compras en cada día de la semana.
•	Compras por Día de la Semana: Un histograma que ilustra la distribución de la actividad de compra a lo largo de los siete días de la semana, con etiquetas claras para cada día.
•	Tiempo de Solicitud (Días Desde el Pedido Anterior): Un gráfico de línea que muestra la distribución de los intervalos de tiempo entre pedidos consecutivos, revelando la frecuencia con la que los usuarios reordenan.
•	Diferencia de Pedidos por Hora del Día (Miércoles vs. Sábado): Un gráfico de barras agrupadas que compara el volumen de pedidos por hora en días específicos (miércoles y sábado), destacando diferencias en el comportamiento semanal.
•	Distribución del Número de Órdenes por Cliente: Un histograma que muestra cuántos pedidos ha realizado cada cliente, permitiendo identificar la fidelidad o frecuencia de compra.
🛒 Módulo "Comportamiento del Producto"
•	Los 20 Productos Más Populares: Un gráfico de barras horizontal que identifica los veinte productos más frecuentemente comprados en la plataforma.
•	Top N Productos Reordenados: Un gráfico de barras interactivo (horizontal o vertical) con un slider que permite al usuario ajustar el número de productos más reordenados a visualizar, mostrando la cantidad total de veces que cada producto ha sido recomprado.
•	La  Reordenación por Producto: Un violin plot que muestra la distribución del ratio de reordenación para los productos más reordenados, ofreciendo una visión de la consistencia con la que los productos son recomprados.
•	Reordenado de Productos por Departamento: Un violin plot que compara el ratio de reordenación promedio de los productos agrupados por su departamento, revelando qué categorías de productos son más propensas a ser reordenadas.
________________________________________
💻 Tecnologías Clave Utilizadas
________________________________________
•	Python: El lenguaje de programación principal.
•	Pandas: Para la manipulación y análisis eficiente de grandes volúmenes de datos.
•	NumPy: Para operaciones numéricas fundamentales.
•	Matplotlib: Para la creación de visualizaciones de datos estáticas.
•	Seaborn: Para la creación de visualizaciones de datos estadísticas y estéticamente agradables.
•	Streamlit: Framework utilizado para construir la interfaz de usuario interactiva del dashboard.
•	Render: Plataforma para el despliegue de la aplicación web.
•	calendar: (Biblioteca estándar de Python) Para la manipulación de nombres de días.
________________________________________
📊 Datos
________________________________________
Este dashboard se alimenta de un conjunto de datos modificado de Instacart, que incluye información detallada sobre pedidos (instacart_orders.csv), productos en los pedidos (order_products.csv), detalles de productos (products.csv) y nombres de departamentos (departments.csv). El dataset ha sido preprocesado para incluir valores ausentes y duplicados, simulando un escenario de datos del mundo real, manteniendo las distribuciones originales para un análisis más realista.
________________________________________
✒️ Autor
•	[Román/Rom5262] 

