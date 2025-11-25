import matplotlib.pyplot as plt
import seaborn as sns

def bx_plot(dataframe):
    """
    Generates box plots for selected features in the given dataframe.

    Parameters:
    dataframe (pd.DataFrame): The input dataframe containing the data to plot.

    Returns:
    None: Displays the box plots.
    """
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='NSP', y='ASTV', data=dataframe, palette="Set2")
    plt.title('Boxplot de ASTV (Abnormal Short Term Variability) por Clase NSP', fontsize=15)
    plt.xlabel('NSP (1=Normal, 2=Sospechoso, 3=Patológico)')
    plt.ylabel('ASTV (%)')
    plt.show()