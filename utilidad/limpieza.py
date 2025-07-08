
import pandas as pd

def limpieza_general(df):
    """
    Realiza una limpieza general de un DataFrame:
    - Copia para evitar modificar el original
    - Estandariza nombres de columnas
    - Elimina duplicados
    - Elimina espacios innecesarios en strings
    - Convierte columnas con fechas cuando es posible
    - Reporta tipos de datos y nulos

    Retorna:
    - df_limpio: DataFrame limpio
    """
    df = df.copy()

   
    df.columns = (
        df.columns.str.strip()
                    .str.lower()
                    .str.replace(" ", "_")
                    .str.replace(r"[^\w]", "_", regex=True))

    df.drop_duplicates(inplace=True)

    for col in df.select_dtypes(include='object'):
        df[col] = df[col].str.strip()

    
    for col in df.columns:
        if "date" in col or "fecha" in col:
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass  

    
    print("Tipos de columnas:")
    print(df.dtypes)
    print("\nNulos por columna:")
    print(df.isnull().sum())

    return df
