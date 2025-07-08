

import matplotlib.pyplot as plt
import seaborn as sns
import calendar
import pandas as pd 

sns.set_style("whitegrid") 

# 1️⃣ Órdenes por hora del día
def grafico_ordenes_por_hora(df: pd.DataFrame) -> plt.Figure | None:
    """Crea un gráfico de línea de usuarios que hacen órdenes por hora del día."""
    if 'order_hour_of_day' not in df.columns or 'user_id' not in df.columns:
        print("Error (grafico_ordenes_por_hora): Faltan las columnas 'order_hour_of_day' o 'user_id'.")
        return None
    
    usuarios_por_hora = df.groupby('order_hour_of_day')['user_id'].count()
    fig, ax = plt.subplots(figsize=(8, 4))
    usuarios_por_hora.plot(ax=ax, marker='o', linestyle='-', color='b', grid=True)
    ax.set_title('Usuarios que hacen órdenes por hora del día')
    ax.set_xlabel('Hora del Día')
    ax.set_ylabel('Cantidad de Usuarios')
    plt.tight_layout()
    return fig

# 2️⃣ Histograma de órdenes por hora
def grafico_histograma_por_hora(df: pd.DataFrame) -> plt.Figure | None:
    """Crea un histograma de la distribución de órdenes por hora del día."""
    if 'order_hour_of_day' not in df.columns:
        print("Error (grafico_histograma_por_hora): Falta la columna 'order_hour_of_day'.")
        return None
        
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(data=df, x='order_hour_of_day', bins=24, ax=ax, color='orange')
    ax.set_title('Distribución de órdenes por hora del día')
    ax.set_xlabel('Hora del Día')
    ax.set_ylabel('Frecuencia')
    plt.tight_layout()
    return fig

# 3️⃣ Órdenes por día de la semana
def grafico_ordenes_por_dia(df: pd.DataFrame) -> plt.Figure | None:
    """Crea un gráfico de línea de usuarios que hacen compras por día de la semana."""
    if 'order_dow' not in df.columns or 'user_id' not in df.columns:
        print("Error (grafico_ordenes_por_dia): Faltan las columnas 'order_dow' o 'user_id'.")
        return None

    usuarios_por_dia = df.groupby('order_dow')['user_id'].count()
    fig, ax = plt.subplots(figsize=(8, 4))
    usuarios_por_dia.plot(ax=ax, marker='o', linestyle='-', color='b', grid=True)
    ax.set_title('Usuarios que hacen compras por día')
    ax.set_xlabel('Día de la Semana')
    ax.set_ylabel('Usuarios por Día')
    plt.tight_layout()
    return fig

# 4️⃣ Histograma de compras por día
def grafico_histograma_por_dia(df: pd.DataFrame) -> plt.Figure | None:
    """Crea un histograma de compras por día de la semana, con etiquetas de días."""
    if 'order_dow' not in df.columns:
        print("Error (grafico_histograma_por_dia): Falta la columna 'order_dow'.")
        return None

    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(data=df, x='order_dow', bins=7, ax=ax, color='orange')
    ax.set_title('Compras por día de la Semana')
    ax.set_xlabel('Día de la Semana')
    ax.set_ylabel('Usuarios por Día')
    ax.set_xticks(range(7))
    ax.set_xticklabels(calendar.day_name[:7], rotation=45, ha='right')
    plt.tight_layout()
    return fig

# 5️⃣ Tiempo entre pedidos
def grafico_tiempo_entre_pedidos(df: pd.DataFrame) -> plt.Figure | None:
    """Crea un gráfico de línea del tiempo transcurrido entre pedidos."""
    if 'days_since_prior_order' not in df.columns:
        print("Error (grafico_tiempo_entre_pedidos): Falta la columna 'days_since_prior_order'.")
        return None

    tiempo_espera = df['days_since_prior_order'].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(8, 4))
    tiempo_espera.plot(ax=ax, marker='o', linestyle='-', color='b', grid=True)
    ax.set_title('Tiempo entre pedidos')
    ax.set_xlabel('Días desde el pedido anterior')
    ax.set_ylabel('Cantidad de Usuarios')
    plt.tight_layout()
    return fig

# 6️⃣ Miércoles vs sábado
def grafico_comparativo_miercoles_sabado(df: pd.DataFrame) -> plt.Figure | None:
    """Compara la distribución de órdenes por hora entre miércoles y sábado."""
    if 'order_dow' not in df.columns or 'order_hour_of_day' not in df.columns:
        print("Error (grafico_comparativo_miercoles_sabado): Faltan 'order_dow' o 'order_hour_of_day'.")
        return None

    # Filtrar y contar órdenes por hora para miércoles (día 3) y sábado (día 6)
    
    dif_wed = df[df['order_dow'] == 3]['order_hour_of_day'].value_counts().sort_index()
    dif_sat = df[df['order_dow'] == 6]['order_hour_of_day'].value_counts().sort_index()
    
    # Unir los DataFrames para comparar
    graphic_dif = dif_wed.to_frame(name='miércoles').join(dif_sat.to_frame(name='sábado'), how='outer').fillna(0)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    graphic_dif.plot(kind='bar', ax=ax, color=['skyblue', 'orange'], width=0.8)
    ax.set_title('Diferencia de Pedidos por Hora del Día')
    ax.set_xlabel('Hora del Día')
    ax.set_ylabel('Cantidad de Órdenes')
    ax.legend(title='Día')
    plt.xticks(rotation=0) 
    plt.tight_layout()
    return fig

# 7️⃣ Órdenes por cliente
def grafico_ordenes_por_cliente(df: pd.DataFrame) -> plt.Figure | None:
    """Muestra la distribución de la cantidad de órdenes por cliente."""
    if 'user_id' not in df.columns:
        print("Error (grafico_ordenes_por_cliente): Falta la columna 'user_id'.")
        return None

    orden_clientes = df['user_id'].value_counts()
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(orden_clientes, bins=24, ax=ax, color='#FF69B4') 
    ax.set_title('Distribución de órdenes por cliente')
    ax.set_xlabel('Cantidad de Órdenes')
    ax.set_ylabel('Número de Clientes')
    plt.tight_layout()
    return fig

# 8️⃣ Productos más comprados
def grafico_top_productos(order_products: pd.DataFrame, products: pd.DataFrame) -> plt.Figure | None:
    """Muestra los Top 20 productos más comprados."""
    required_cols_op = ['product_id']
    required_cols_p = ['product_id', 'product_name']
    
    if not all(col in order_products.columns for col in required_cols_op) or \
       not all(col in products.columns for col in required_cols_p):
        print("Error (grafico_top_productos): Faltan columnas en 'order_products' o 'products'.")
        return None

    conteo = order_products.groupby('product_id').size().reset_index(name='compras')
    top = conteo.merge(products, on='product_id').sort_values(by='compras', ascending=False).head(20)
    
    fig, ax = plt.subplots(figsize=(10, 7))
    sns.barplot(y=top['product_name'], x=top['compras'], ax=ax, palette='viridis') # Usar una paleta más genérica
    ax.set_title('Top 20 Productos Más Comprados')
    ax.set_xlabel('Cantidad de Compras')
    ax.set_ylabel('Producto')
    plt.tight_layout()
    return fig

# 9️⃣ Productos más reordenados
def grafico_top_reordenados(order_products: pd.DataFrame, products: pd.DataFrame, top_n: int = 20, orientacion: str = "horizontal") -> plt.Figure | None:
    """Muestra los Top N productos más reordenados, con opción de orientación."""
    required_cols_op = ['product_id', 'reordered']
    required_cols_p = ['product_id', 'product_name']

    if not all(col in order_products.columns for col in required_cols_op) or \
       not all(col in products.columns for col in required_cols_p):
        print("Error (grafico_top_reordenados): Faltan columnas en 'order_products' o 'products'.")
        return None

    reorders = order_products.groupby('product_id')['reordered'].sum().reset_index()
    top = reorders.merge(products, on='product_id').sort_values(by='reordered', ascending=False).head(top_n)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    palette = sns.color_palette('Blues_r', len(top))

    if orientacion == "horizontal":
        sns.barplot(data=top, x='reordered', y='product_name', ax=ax, palette=palette)
        # Anotaciones de valores en las barras
        for bar in ax.patches:
            ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2, str(int(bar.get_width())),
                            va='center', fontsize=9)
        ax.set_xlabel("Cantidad de Reordenes")
        ax.set_ylabel("Producto")
    else: # Orientación vertical
        sns.barplot(data=top, x='product_name', y='reordered', ax=ax, palette=palette)
        # Anotaciones de valores en las barras
        for bar in ax.patches:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, str(int(bar.get_height())),
                            ha='center', va='bottom', fontsize=9) # 'va' changed to 'bottom' for better placement
        ax.set_ylabel("Cantidad de Reordenes")
        ax.set_xlabel("Producto")
        plt.xticks(rotation=45, ha='right') # Rotar etiquetas para mejor legibilidad

    ax.set_title(f"Top {top_n} Productos Reordenados")
    plt.tight_layout()
    return fig

# 🔟 Reorden por departamento
def grafico_reorden_por_departamento(order_products: pd.DataFrame, products: pd.DataFrame, departments: pd.DataFrame) -> plt.Figure | None:
    """Muestra el ratio de reorden de productos agrupado por departamento."""
    required_cols_op = ['product_id', 'reordered']
    required_cols_p = ['product_id', 'department_id']
    required_cols_d = ['department_id', 'department']

    if not all(col in order_products.columns for col in required_cols_op) or \
       not all(col in products.columns for col in required_cols_p) or \
       not all(col in departments.columns for col in required_cols_d):
        print("Error (grafico_reorden_por_departamento): Faltan columnas en 'order_products', 'products' o 'departments'.")
        return None

    reorder_ratio = order_products.groupby('product_id')['reordered'].mean().reset_index(name='reorder_ratio')
    merged = reorder_ratio.merge(products[['product_id', 'department_id']], on='product_id')
    merged = merged.merge(departments, on='department_id')
    
    fig, ax = plt.subplots(figsize=(14, 6))
    sns.violinplot(data=merged, x='department', y='reorder_ratio', palette='coolwarm', ax=ax)
    ax.set_title('Reorden por Departamento')
    ax.set_xlabel('Departamento')
    ax.set_ylabel('Ratio de Reorden')
    plt.xticks(rotation=45, ha='right') 
    plt.tight_layout()
    return fig
