import matplotlib.pyplot as plt
import seaborn as sns

def heatmap_plot(dataframe):
    """
    Generates a heatmap for the correlation matrix of the given dataframe.

    Parameters:
    dataframe (pd.DataFrame): The input dataframe containing the data to plot.

    Returns:
    None: Displays the heatmap.
    """
    plt.figure(figsize=(12, 10))
    correlation_matrix = dataframe.corr()
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
    plt.title('Mapa de Calor de la Matriz de Correlación', fontsize=15)
    plt.show()