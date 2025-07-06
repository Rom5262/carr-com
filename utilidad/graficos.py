
import matplotlib.pyplot as plt
import seaborn as sns
import calendar

sns.set_style("whitegrid")

# 1️⃣ Órdenes por hora del día
def grafico_ordenes_por_hora(df):
    usuarios_por_hora = df.groupby('order_hour_of_day')['user_id'].count()
    fig, ax = plt.subplots(figsize=(8, 4))
    usuarios_por_hora.plot(ax=ax, marker='o', linestyle='-', color='b', grid=True)
    ax.set_title('Usuarios que hacen órdenes por hora del día')
    ax.set_xlabel('Hora del Día')
    ax.set_ylabel('Cantidad de Usuarios')
    return fig

# 2️⃣ Histograma de órdenes por hora
def grafico_histograma_por_hora(df):
    fig, ax = plt.subplots()
    sns.histplot(data=df, x='order_hour_of_day', bins=24, ax=ax, color='orange')
    ax.set_title('Distribución de órdenes por hora del día')
    ax.set_xlabel('Hora del Día')
    ax.set_ylabel('Frecuencia')
    return fig

# 3️⃣ Órdenes por día de la semana
def grafico_ordenes_por_dia(df):
    usuarios_por_dia = df.groupby('order_dow')['user_id'].count()
    fig, ax = plt.subplots(figsize=(8, 4))
    usuarios_por_dia.plot(ax=ax, marker='o', linestyle='-', color='b', grid=True)
    ax.set_title('Usuarios que hacen compras por día')
    ax.set_xlabel('Día de la Semana')
    ax.set_ylabel('Usuarios por Día')
    return fig

# 4️⃣ Histograma de compras por día
def grafico_histograma_por_dia(df):
    fig, ax = plt.subplots()
    sns.histplot(data=df, x='order_dow', bins=7, ax=ax, color='orange')
    ax.set_title('Compras por día de la Semana')
    ax.set_xlabel('Día de la Semana')
    ax.set_ylabel('Usuarios por Día')
    ax.set_xticks(range(7))
    ax.set_xticklabels(calendar.day_name[:7])
    return fig

# 5️⃣ Tiempo entre pedidos
def grafico_tiempo_entre_pedidos(df):
    tiempo_espera = df['days_since_prior_order'].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(8, 4))
    tiempo_espera.plot(ax=ax, marker='o', linestyle='-', color='b', grid=True)
    ax.set_title('Tiempo entre pedidos')
    ax.set_xlabel('Días desde el pedido anterior')
    ax.set_ylabel('Cantidad de Usuarios')
    return fig

# 6️⃣ Miércoles vs sábado
def grafico_comparativo_miercoles_sabado(df):
    dif_wed = df[df['order_dow'] == 3]['order_hour_of_day'].value_counts().sort_index()
    dif_sat = df[df['order_dow'] == 6]['order_hour_of_day'].value_counts().sort_index()
    graphic_dif = dif_wed.to_frame(name='miércoles').join(dif_sat.to_frame(name='sábado'))
    fig, ax = plt.subplots(figsize=(10, 5))
    graphic_dif.plot(kind='bar', ax=ax, color=['skyblue', 'orange'])
    ax.set_title('Diferencia de Pedidos por Hora del Día')
    ax.set_xlabel('Hora del Día')
    ax.set_ylabel('Cantidad de Órdenes')
    ax.legend(title='Día')
    return fig

# 7️⃣ Órdenes por cliente
def grafico_ordenes_por_cliente(df):
    orden_clientes = df['user_id'].value_counts()
    fig, ax = plt.subplots()
    sns.histplot(orden_clientes, bins=24, ax=ax, color='#FF69B4')
    ax.set_title('Distribución de órdenes por cliente')
    ax.set_xlabel('Cantidad de Órdenes')
    ax.set_ylabel('Número de Clientes')
    return fig

# 8️⃣ Productos más comprados
def grafico_top_productos(order_products, products):
    conteo = order_products.groupby('product_id').size().reset_index(name='compras')
    top = conteo.merge(products, on='product_id').sort_values(by='compras', ascending=False).head(20)
    fig, ax = plt.subplots()
    sns.barplot(y=top['product_name'], x=top['compras'], ax=ax, palette=['#32CD32'] * len(top))
    ax.set_title('Top 20 Productos Más Comprados')
    ax.set_xlabel('Cantidad de Compras')
    ax.set_ylabel('Producto')
    return fig

# 9️⃣ Productos más reordenados
def grafico_top_reordenados(order_products, products, top_n=20, orientacion="horizontal"):
    reorders = order_products.groupby('product_id')['reordered'].sum().reset_index()
    top = reorders.merge(products, on='product_id').sort_values(by='reordered', ascending=False).head(top_n)
    palette = sns.color_palette('Blues_r', len(top))
    fig, ax = plt.subplots(figsize=(10, 6))

    if orientacion == "horizontal":
        sns.barplot(data=top, x='reordered', y='product_name', ax=ax, palette=palette)
        for bar in ax.patches:
            ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2, str(int(bar.get_width())),
                    va='center', fontsize=9)
        ax.set_xlabel("Cantidad de Reordenes")
        ax.set_ylabel("Producto")
    else:
        sns.barplot(data=top, x='product_name', y='reordered', ax=ax, palette=palette)
        for bar in ax.patches:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, str(int(bar.get_height())),
                    ha='center', fontsize=9)
        ax.set_ylabel("Cantidad de Reordenes")
        ax.set_xlabel("Producto")
        plt.xticks(rotation=45)

    ax.set_title(f"Top {top_n} Productos Reordenados")
    return fig

# 🔟 Reorden por departamento
def grafico_reorden_por_departamento(order_products, products, departments):
    reorder_ratio = order_products.groupby('product_id')['reordered'].mean().reset_index(name='reorder_ratio')
    merged = reorder_ratio.merge(products[['product_id', 'department_id']], on='product_id')
    merged = merged.merge(departments, on='department_id')
    fig, ax = plt.subplots(figsize=(14, 6))
    sns.violinplot(data=merged, x='department', y='reorder_ratio', palette='coolwarm', ax=ax)
    ax.set_title('Reorden por Departamento')
    ax.set_xlabel('Departamento')
    ax.set_ylabel('Ratio de Reorden')
    plt.xticks(rotation=45)
    fig.tight_layout()
    return fig
