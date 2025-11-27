"""
ctg_viz: A library for CTG data visualization and processing.

Provides tools for loading, preprocessing, categorizing, and visualizing CTG datasets.

Modules included:
 - preprocessing: Functions for cleaning and preparing CTG data.
 - categorization: Functions for categorizing and analyzing data completeness.
 - plots: Functions for generating various types of plots for data visualization.
 - utils: Functions for data upload and utility operations.
"""

#Importación de módulos y funciones
from .preprocessing import preprocessing
from .categorization import check_data_completeness_Magdaleno_Flores_Nilton_Sebastian
from .utils import upload_and_process_data

__version__ = "0.1.0"
__author__ = "Yo mero, ChatGPT, Claude y demás colegas (otras IA's y tutoriales de yutu)"

__all__ = [
    
]