import pandas as pd
import numpy as np

"""
Función de preprocesamiento de datos CTG.
Realiza limpieza de datos, imputación de valores faltantes y tratamiento de outliers.
"""
def preprocessing(df_input : pd.DataFrame) -> pd.DataFrame:
    df_proc = df_input.copy()
    
    # 1. Eliminar columnas con más del 20% de valores nulos
    null_pct = df_proc.isnull().mean()                                          # Porcentaje de nulos por columna           
    cols_to_drop = null_pct[null_pct > 0.2].index                               # Umbral del 20%
    if len(cols_to_drop) > 0:
        print(f"Columnas eliminadas (>20% nulos): {list(cols_to_drop)}")
        df_proc = df_proc.drop(columns=cols_to_drop)
    else:
        print("No hay columnas con >20% de nulos para eliminar.")
    
    # 2. Imputar valores faltantes restantes
    numeric_cols = df_proc.select_dtypes(include=[np.number]).columns           ## Columnas numéricas
    categorical_cols = df_proc.select_dtypes(exclude=[np.number]).columns       ## Columnas categóricas
    
    # Imputación Numérica: Mediana
    for col in numeric_cols:
        if df_proc[col].isnull().sum() > 0:
            median_val = df_proc[col].median()
            df_proc[col] = df_proc[col].fillna(median_val)
            
    # Imputación Categórica: Moda
    for col in categorical_cols:
        if df_proc[col].isnull().sum() > 0:
            mode_val = df_proc[col].mode()[0]
            df_proc[col] = df_proc[col].fillna(mode_val)
            
    # 3. Detectar y tratar valores atípicos (Outliers) con IQR
    # Excluimos columnas target o identificadores si es necesario
    # En CTG, 'NSP' y 'CLASS' son targets, no deberíamos clipearlas.
    cols_exclude_outlier = ['NSP', 'CLASS', 'Tendency']
    cols_for_outliers = [c for c in numeric_cols if c not in cols_exclude_outlier]
    
    for col in cols_for_outliers:
        Q1 = df_proc[col].quantile(0.25)
        Q3 = df_proc[col].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Tratamiento: Clipping (limitar valores al rango)
        # Esto preserva la distribución mejor que eliminar filas
        df_proc[col] = np.clip(df_proc[col], lower_bound, upper_bound)
        
    return df_proc