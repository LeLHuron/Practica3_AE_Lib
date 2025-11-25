"""
ctg_viz: Una biblioteca para la visualización y categorización de datos (CTG).

Proporciona herramientas para crear gráficos interactivos, preprocesar y categorizar datos.

Módulos:
 - preprocessing: Funciones para limpiar y preparar datos para su análisis.
 - categorization: Función para clasificar y categorizar conjuntos de datos.
 - plots: Funciones para generar gráficos y visualizaciones de datos.
 - utils: Funciones utilitarias para soporte adicional en el procesamiento y visualización de datos.
"""

from .preprocessing import *
from .categorization import categorize_data
from utils import *

from .plots.barplots import bar_plot
from .plots.boxplots import bx_plot
from .plots.density import density_plot
from .plots.heatmap import *
from .plots.histograms import *

"""
from setuptools import setup, find_packages

setup(
    name='mi_paquete',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    description='Una descripción corta de mi paquete',
    author='Tu Nombre',
    author_email='tu@email.com',
)
"""
__version__ = "0.1.0"
__author__ = "Yo mero"

__all__ = [
    
]