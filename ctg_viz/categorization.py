import pandas as pd
import numpy as np
"""
    Función general para verificar la completitud y calidad de los datos.
    Parámetros:
    df (pd.DataFrame): DataFrame a analizar.
    Retorna:
    pd.DataFrame: DataFrame con el análisis de completitud y calidad de cada columna.
"""
def check_data_completeness_Magdaleno_Flores_Nilton_Sebastian(df : pd.DataFrame) -> pd.DataFrame:    
    res = []                                                        # Lista para almacenar resultados
    for col in df.columns:
        dtype = df[col].dtype                                       # Tipo de dato
        total_rows = len(df)                                        # Total de filas
        null_count = df[col].isnull().sum()                         # Conteo de valores nulos
        null_pct = (null_count / total_rows) * 100                  # Porcentaje de nulos
        completeness_pct = 100 - null_pct                           # Porcentaje de completitud        
        unique_vals = df[col].nunique()                             # Valores únicos
        
        # Estadísticos de dispersión y clasificación
        if pd.api.types.is_numeric_dtype(df[col]):
            std_dev = df[col].std()                                 # Desviación estándar
            variance = df[col].var()                                # Varianza
            # Clasificación automática
            if unique_vals > 10:
                col_type = 'Continua'
            else:
                col_type = 'Discreta'
        else:
            std_dev = np.nan                                        # Desviación estándar no aplicable
            variance = np.nan                                       # Varianza no aplicable
            col_type = 'Categórica'
            if unique_vals < 10:
                 col_type = 'Discreta (Cat)'

        res.append({
            'Columna': col,
            'Nulos': null_count,
            '% Completitud': round(completeness_pct, 2),
            'Tipo Dato': dtype,
            'Valores Únicos': unique_vals,
            'Std Dev': round(std_dev, 2) if not pd.isna(std_dev) else np.nan,
            'Varianza': round(variance, 2) if not pd.isna(variance) else np.nan,
            'Clasificación': col_type
        })
    
    return pd.DataFrame(res)