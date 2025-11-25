import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def bar_plot(dataframe: pd.DataFrame) -> None:
    """
    Generates a bar plot from the given dataframe.

    Parameters:
    dataframe (pd.DataFrame): The input dataframe containing the data to plot.

    Returns:
    None: Displays the bar plot.
    """
    plt.figure(figsize=(10, 8))
    class_counts = dataframe['CLASS'].value_counts().sort_values(ascending=True)
    class_counts.plot(kind='barh', color=sns.color_palette("husl", len(class_counts)))
    plt.title('Frecuencia de Clases Morfológicas (CLASS)', fontsize=15)
    plt.xlabel('Frecuencia')
    plt.ylabel('Clase')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.show()