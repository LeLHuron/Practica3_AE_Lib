"""
Módulo de utilidades para visualización de datos CTG en app.py y pruebas unitarias.
Archivo para hacer test de importación de funciones así como crear auxiliares.
"""
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import pytest
import numpy as np
#Importar funciones de plot para pruebas unitarias

from ctg_viz.plots import barplots, boxplots ,histograms
from ctg_viz.preprocessing import preprocessing
from ctg_viz.categorization import check_data_completeness_Magdaleno_Flores_Nilton_Sebastian
#Función para subir y procesar datos en app.py
def upload_and_process_data() -> pd.DataFrame :
    """
    Permite al usuario subir un archivo CSV o Excel y lo convierte en un DataFrame de Pandas.

    Returns:
        Optional[pd.DataFrame]: DataFrame cargado si el archivo es válido, 'None' si no se ha cargado archivo o si el formato es inválido.
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

### Pruebas unitarias ###
# Gráficos #
def test_bar_plot_runs_without_error():
    df = pd.DataFrame({"CLASS": ["A", "B", "A", "C", "B", "B"]})
    try:
        barplots.bar_plot(df)
    except Exception as e:
        pytest.fail(f"bar_plot raised an exception {e}")

def test_bx_plot_runs_without_error():
    df = pd.DataFrame({
        'NSP': [1, 2, 1, 3, 2],
        'ASTV': [10.5, 15.2, 13.1, 9.8, 14.3]
    })
    try:
        boxplots.bx_plot(df)
    except Exception as e:
        pytest.fail(f"bx_plot raised an exception {e}")

def test_histogram_plot_runs_without_error():
    # Crear DataFrame de prueba
    df = pd.DataFrame({
        'LB': [70, 75, 80, 85],
        'NSP': ['A', 'B', 'A', 'B']
    })
    # Verificar que la función se ejecuta sin lanzar errores
    try:
        histograms.histogram_plot(df)
    except Exception as e:
        pytest.fail(f"histogram_plot raised an exception {e}")

# Procesamiento de datos y Categorización #
def test_preprocessing_basic():
    df = pd.DataFrame({
        'A': [1, 2, np.nan, 4, 1000],     # Outlier en columna numérica
        'B': ['cat', np.nan, 'dog', 'cat', 'dog'],
        'NSP': [1, 2, 1, 3, 2],            # Target para excluir en outlier
        'CLASS': ['x', 'y', 'x', 'y', 'x']
    })
    result = preprocessing(df)
    assert isinstance(result, pd.DataFrame)
    assert result.isnull().sum().sum() == 0     # Sin valores faltantes
    assert 'A' in result.columns                  # Columna numérica no eliminada si no > 20% nulo

def test_check_data_completeness():
    df = pd.DataFrame({
        'num_col': [1, 2, np.nan, 4, 5],
        'cat_col': ['a', 'b', 'b', np.nan, 'a'],
        'mixed_col': [1, 'x', 2, 'y', np.nan]
    })
    result = check_data_completeness_Magdaleno_Flores_Nilton_Sebastian(df)
    assert isinstance(result, pd.DataFrame)
    assert 'Columna' in result.columns
    assert 'Nulos' in result.columns
    assert 'Clasificación' in result.columns