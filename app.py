"""
from ctg_viz import preprocessing, categorization
from ctg_viz.plots import barplots, boxplots, density, heatmap, histograms
"""
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#Configuración de la página
st.set_page_config(
    page_title="CTG Visualization",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded"
)