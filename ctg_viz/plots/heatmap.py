import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

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
    corr_matrix = dataframe[cols_corr].corr(method='spearman') # Se puede cambiar a 'spearman'

    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Mapa de Calor de Correlación (Spearman)', fontsize=15)