"""
from ctg_viz import preprocessing, categorization
from ctg_viz.plots import barplots, boxplots, density, heatmap, histograms
"""
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd

from ctg_viz.plots import barplots, boxplots, density, heatmap, histograms
import ctg_viz as ctv
from ctg_viz.utils import upload_and_process_data
from ctg_viz.preprocessing import preprocessing
from ctg_viz.categorization import check_data_completeness_Magdaleno_Flores_Nilton_Sebastian
#Configuración de la página
st.set_page_config(
    page_title="CTG Visualization",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título de la aplicación
st.title("CTG Data Visualization App")
st.markdown("Explora y visualiza datos CTG utilizando diversas herramientas gráficas.")

#1. Introducción
with st.expander("Introducción", expanded=True):
    st.markdown("""
    Esta aplicación permite a los usuarios cargar, preprocesar y visualizar datos CTG utilizando módulos propios en Python:
    * **Matplotlib**: Biblioteca base de visualización
    * **Seaborn**: Biblioteca para gráficos estadísticos
    * **Plotly**: Biblioteca para gráficos interactivos
    * **ctg_viz**: Biblioteca personalizada para procesamiento y visualización de datos CTG
    * **Streamlit**: Framework para crear aplicaciones web interactivas
    """)

#2. Carga de datos
df_user = ctv.upload_and_process_data()
if df_user is not None:
    st.write("Datos del usuario (primeras 5 filas):", df_user.head()) # Muestra el DataFrame
    
    # Aquí puedes añadir tu lógica de procesamiento de datos con Python/Pandas
    st.write("Resumen estadístico:", df_user.describe())
    # Preprocesamiento
    df_preprocessed = preprocessing(df_user)
    # Verificar que no queden nulos
    st.write(f"\nTotal de nulos después del procesamiento: {df_preprocessed.isnull().sum().sum()}")
    # Análisis de completitud
    df_completeness = check_data_completeness_Magdaleno_Flores_Nilton_Sebastian(df_preprocessed)
    st.write("Análisis de completitud y calidad de datos:", df_completeness)
    # Visualizaciones
    st.subheader("Visualizaciones")
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Gráfico de Barras")
            barplots.bar_plot(df_preprocessed)
            st.pyplot()
            st.markdown("### Histograma")
            histograms.histogram_plot(df_preprocessed)
            st.pyplot() 
            st.markdown("### Gráfico de Caja")
            boxplots.bx_plot(df_preprocessed)
            st.pyplot()
        with col2:
            st.markdown("### Gráfico de Densidad")
            density.density_plot(df_preprocessed)
            st.pyplot()
            st.markdown("### Mapa de Calor")
            heatmap.heatmap_plot(df_preprocessed)
            st.pyplot()
