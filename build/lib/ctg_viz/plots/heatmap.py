import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st

def heatmap_plot(dataframe: pd.DataFrame) -> None:
    """
    Generates a heatmap for the correlation matrix of the given dataframe.

    Parameters:
    dataframe (pd.DataFrame): The input dataframe containing the data to plot.

    Returns:
    None: Displays the heatmap.
    """
    plt.figure(figsize=(6, 5))
    cols_corr = ['LB', 'AC', 'FM', 'UC', 'ASTV', 'MSTV', 'ALTV', 'MLTV', 'Width', 'NSP']
    corr_matrix = dataframe[cols_corr].corr(method='spearman') # Se puede cambiar a 'pearson' si se desea

    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Mapa de Calor de Correlación (Spearman)', fontsize=15)

# Interactive plot with Plotly
def heatmap_plot_interactive(dataframe: pd.DataFrame) -> None:
    """
    Generates an interactive heatmap from the given dataframe using Plotly.
    
    Parameters:
    dataframe (pd.DataFrame): The input dataframe containing the data to plot.

    Returns:
    None: Displays the interactive heatmap.
    """
    cols_corr = ['LB', 'AC', 'FM', 'UC', 'ASTV', 'MSTV', 'ALTV', 'MLTV', 'Width', 'NSP']
    corr_matrix = dataframe[cols_corr].corr(method='spearman')
    fig = px.imshow(
        corr_matrix,
        text_auto=".2f",
        color_continuous_scale='RdBu_r',
        origin='lower',
        aspect='auto',
        title='Mapa de Calor de Correlación (Spearman)'
    )
    fig.update_layout(width=600, height=500)
    st.plotly_chart(fig)