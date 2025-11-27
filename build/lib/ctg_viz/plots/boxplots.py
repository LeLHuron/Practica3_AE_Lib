import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st

def bx_plot(dataframe: pd.DataFrame) -> None:
    """
    Generates box plots for selected features in the given dataframe.

    Parameters:
    dataframe (pd.DataFrame): The input dataframe containing the data to plot.

    Returns:
    None: Displays the box plots.
    """
    plt.figure(figsize=(8, 4))
    sns.boxplot(x='NSP', y='ASTV', data=dataframe, palette="Set2")
    plt.title('Boxplot de ASTV (Abnormal Short Term Variability) por Clase NSP', fontsize=15)
    plt.xlabel('NSP (1=Normal, 2=Sospechoso, 3=Patológico)')
    plt.ylabel('ASTV (%)')

# Interactive plot with Plotly
def bx_plot_interactive(dataframe: pd.DataFrame) -> None:
    """
    Generates an interactive box plot from the given dataframe using Plotly.

    Parameters:
    dataframe (pd.DataFrame): The input dataframe containing the data to plot.
    
    Returns:
    None: Displays the interactive box plot."""
    fig = px.box(
        dataframe,
        x='NSP',
        y='ASTV',
        color='NSP',
        color_discrete_sequence=px.colors.qualitative.Set2,
        labels={
            'NSP': 'NSP (1=Normal, 2=Sospechoso, 3=Patológico)',
            'ASTV': 'ASTV (%)'
        },
        title='Boxplot de ASTV (Abnormal Short Term Variability) por Clase NSP'
    )
    st.plotly_chart(fig)