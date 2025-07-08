
import pandas as pd

def limpieza_general(df):
    """
    Realiza una limpieza básica de nombres de columnas y optimiza tipos de datos (sin category para depurar).
    """
    # Limpiar nombres de columnas: poner en minúsculas y reemplazar espacios por guiones bajos
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # --- Optimización de tipos de datos para reducir el uso de memoria ---
    # Aplica estas optimizaciones a las columnas que existen en tu DataFrame

    # Manejar nulos en 'days_since_prior_order' ANTES de la conversión de tipo si es necesario
    if 'days_since_prior_order' in df.columns:
        # Llenar nulos con un valor específico (por ejemplo, -1 o 0)
        # Elegimos 0 si asumimos que es el primer pedido del usuario o -1 si queremos distinguirlos
        # Vamos a usar 0 por ahora para simplificar los cálculos si un gráfico lo usa.
        df['days_since_prior_order'] = df['days_since_prior_order'].fillna(0).astype('float16')
        # Si en algún punto se necesitara como entero (ej. para graficar conteos discretos)
        # y queremos mantenerla como un número que no sea una fecha real,
        # podríamos convertirla a Int16 (con 'I' mayúscula para enteros nullable de Pandas)
        # o a int16 después de rellenar los nulos.
        # Por ahora, con fillna(0) y float16, debería ser suficiente para quitar el error.


    # Ejemplo para el DataFrame 'orders'
    if 'order_dow' in df.columns:
        df['order_dow'] = df['order_dow'].astype('int8')
    if 'order_hour_of_day' in df.columns:
        df['order_hour_of_day'] = df['order_hour_of_day'].astype('int8')
    # La línea days_since_prior_order ya está manejada arriba
    if 'user_id' in df.columns:
        df['user_id'] = df['user_id'].astype('int32')

    # Ejemplo para el DataFrame 'order_products'
    if 'add_to_cart_order' in df.columns:
        # Llenar nulos en 'add_to_cart_order' si los hay (tu terminal mostró 2 nulos aquí)
        # Usaremos 0, asumiendo que un producto con nulo en add_to_cart_order se agregó primero
        df['add_to_cart_order'] = df['add_to_cart_order'].fillna(0).astype('int16')
    if 'reordered' in df.columns:
        df['reordered'] = df['reordered'].astype('bool')

    # Ejemplo para los DataFrames que tienen IDs como 'product_id', 'department_id', 'aisle_id'
    if 'product_id' in df.columns:
        df['product_id'] = df['product_id'].astype('int32')
    if 'order_id' in df.columns:
        df['order_id'] = df['order_id'].astype('int32')
    if 'department_id' in df.columns:
        df['department_id'] = df['department_id'].astype('int8')
    if 'aisle_id' in df.columns:
        df['aisle_id'] = df['aisle_id'].astype('int16')

    # Si 'product_name' tiene nulos y causa problemas en algún gráfico, podríamos rellenarlos también.
    # Por ejemplo: df['product_name'] = df['product_name'].fillna('Desconocido')

    return df
