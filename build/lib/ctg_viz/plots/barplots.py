import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
def bar_plot(dataframe: pd.DataFrame) -> None:
    """
    Generates a bar plot from the given dataframe.

    Parameters:
    dataframe (pd.DataFrame): The input dataframe containing the data to plot.

    Returns:
    None: Displays the bar plot.
    """
    plt.figure(figsize=(6, 4))
    class_counts = dataframe['CLASS'].value_counts().sort_values(ascending=True)
    class_counts.plot(kind='barh', color=sns.color_palette("husl", len(class_counts)))
    plt.title('Frecuencia de Clases Morfológicas (CLASS)', fontsize=15)
    plt.xlabel('Frecuencia')
    plt.ylabel('Clase')
    plt.grid(axis='x', linestyle='--', alpha=0.7)

#Interactive plot with Plotly
def bar_plot_interactive(dataframe: pd.DataFrame) -> None:
    """
    Generates an interactive bar plot from the given dataframe using Plotly.

    Parameters:
    dataframe (pd.DataFrame): The input dataframe containing the data to plot.
    
    Returns:
    None: Displays the interactive bar plot.
    """
    class_counts = dataframe['CLASS'].value_counts().sort_values(ascending=True)
    fig = px.bar(
        x=class_counts.values,
        y=class_counts.index,
        orientation='h',
        labels={'x': 'Frecuencia', 'y': 'Clase'},
        title='Frecuencia de Clases Morfológicas (CLASS)',
        color=class_counts.index
    )
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig)