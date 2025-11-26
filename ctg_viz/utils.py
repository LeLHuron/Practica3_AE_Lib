"""
Módulo de utilidades para visualización de datos CTG.
Archivo para hacer test de importación de funciones así como crear auxiliares.
"""
import pandas as pd

import streamlit as st

def upload_and_process_data() -> pd.DataFrame :
    """
    Permite al usuario subir un archivo y lo convierte en un DataFrame de Pandas.
    """
    uploaded_file = st.file_uploader("Sube tu archivo CSV o Excel", type=["csv", "xlsx"])
    if uploaded_file is not None:
        # Detectar el tipo de archivo para usar la función de lectura correcta
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        else:
            st.error("Formato de archivo no compatible. Sube un CSV o XLSX.")
            return None
            
        st.success("Dataset cargado exitosamente.")
        return df
    return None