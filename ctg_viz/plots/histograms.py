import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

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