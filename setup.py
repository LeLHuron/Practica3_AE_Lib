from setuptools import setup, find_packages

setup(
    name='mi_paquete',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'numpy',
        'pandas',
        'matplotlib',
        'pathlib',
        'seaborn'
    ],
    description='Una descripción corta de mi paquete',
    author='Nilton Magdaleno',
    author_email='nilton_magdaleno@hotmail.com',
    
)
