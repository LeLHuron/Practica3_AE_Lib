import matplotlib.pyplot as plt
import seaborn as sns

def density_plot(dataframe):
    """
    Generates density plots for selected features in the given dataframe.

    Parameters:
    dataframe (pd.DataFrame): The input dataframe containing the data to plot.

    Returns:
    None: Displays the density plots.
    """
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=dataframe, x='Width', hue='NSP', fill=True, palette="crest", alpha=0.5, linewidth=2)
    plt.title('Gráfico de Densidad de Width por Clase NSP', fontsize=15)
    plt.xlabel('Width')
    plt.show()