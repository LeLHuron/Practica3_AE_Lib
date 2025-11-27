# Practica3_AE_Lib
Profundización en el análisis exploratorio de datos mediante la creación de una librería personalizada de visualización con funciones reutilizables, aplicando buenas prácticas de desarrollo y análisis estadístico.

### Descripción
Este proyecto proporciona un paquete Python para el preprocesamiento, categorización y visualización de datos de cardiotocografía. Incluye una aplicación web interactiva desarrollada con Streamlit para explorar y analizar los datos de manera visual.

### 📊 Módulos Principales
- preprocessing.py  
Contiene funciones para limpiar y preparar los datos CTG antes del análisis.
- categorization.py  
Implementa métodos para categorizar y clasificar los datos según diferentes criterios.
- plots/  
Módulo con funciones especializadas para crear diferentes tipos de visualizaciones:  
  - histograms.py: Distribuciones de variables
  - boxplots.py: Análisis de dispersión y outliers
  - barplots.py: Comparaciones categóricas
  - density.py: Curvas de densidad
  - heatmap.py: Matrices de correlación
- utils.py  
Funciones auxiliares incluyendo la carga de datos para la aplicación Streamlit. Incluye pruebas con pytest.

### 📄 Datos
El proyecto incluye datos de cardiotocografía en dos formatos:

CTG.csv: Formato CSV para uso general  
CTG.xls: Formato Excel original
### Licencia
The MIT License(MIT)  
Copyright (2025)