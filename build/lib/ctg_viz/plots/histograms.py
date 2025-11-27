import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st

def histogram_plot(dataframe: pd.DataFrame) -> None:
    """
    Generates histograms for selected features in the given dataframe.

    Parameters:
    dataframe (pd.DataFrame): The input dataframe containing the data to plot.

    Returns:
    None: Displays the histograms.
    """
    plt.figure(figsize=(6, 4))
    sns.histplot(data=dataframe, x='LB', hue='NSP', kde=True, element="step", palette="viridis", common_norm=False)
    plt.title('Distribución de LB (Baseline Heart Rate) por Clase NSP', fontsize=15)
    plt.xlabel('Latidos por minuto (LB)')
    plt.ylabel('Densidad')

# Interactive plot with Streamlit
def histogram_plot_interactive(dataframe: pd.DataFrame) -> None:
    """
    Generates an interactive histogram from the given dataframe using Plotly.
    
    Parameters:
    dataframe (pd.DataFrame): The input dataframe containing the data to plot.
    
    Returns:
    None: Displays the interactive histogram.
    """
    fig = px.histogram(
        dataframe,
        x='LB',
        color='NSP',
        barmode='overlay',
        marginal='rug',  # Opcional, para mostrar distribución adicional
        histnorm='density',  # Para obtener densidades como en kde=True en Seaborn
        color_discrete_sequence=px.colors.sequential.Viridis,
        labels={'LB': 'Latidos por minuto (LB)', 'NSP': 'Clase NSP'},
        title='Distribución de LB (Baseline Heart Rate) por Clase NSP'
    )
    fig.update_traces(opacity=0.75)
    st.plotly_chart(fig)