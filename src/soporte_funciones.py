
## Importación Librerias

import pandas as pd
import os
import sys
from scipy import stats
from scipy.stats import shapiro, levene
from scipy.stats import ttest_ind
from scipy.stats import mannwhitneyu
from scipy.stats import chi2_contingency
import seaborn as sns
#from IPython.display import display

## Funciones EDA y transformación de datos: 

def exploracion(df):

## "Función exploración DF (pocentaje de nulos, tipo de datos, valores únicos, cantidad de registros duplicados y principales estadisticas)" #En el caso de duplicados, cambiamos a keep=False para que cuente todas las ocurrencias). 

    df_info = pd.DataFrame()

    df_info["% nulos"] = round(df.isna().sum()/df.shape[0]*100, 2).astype(str)+"%"
    df_info["% no_nulos"] = round(df.notna().sum()/df.shape[0]*100, 2).astype(str)+"%"
    df_info["tipo_dato"] = df.dtypes
    df_info["num_valores_unicos"] = df.nunique()

    print(f"""El DataFrame tiene {df.shape[0]} filas y {df.shape[1]} columnas.
Tiene {df.duplicated().sum()} datos duplicados, lo que supone un porcentaje de {round(df.duplicated().sum()/df.shape[0]*100,2)}% de los datos. 

Hay {len(list(df_info[(df_info["% nulos"] != "0.0%")].index))} columnas con datos nulos, y son: 
{list(df_info[(df_info["% nulos"] != "0.0%")].index)}

y sin nulos hay {len(list(df_info[(df_info["% nulos"] == "0.0%")].index))} columnas y son: 
{list(df_info[(df_info["% nulos"] == "0.0%")].index)}


A continuación tienes un detalle sobre los datos nulos y los tipos y número de datos:""")
    
    display(df_info.head())

    ## Comprobar si hay columnas categóricas y mostrar info de esas columnas
    col_categoricas = df.select_dtypes(include = "O").columns
    if len(col_categoricas) > 0: 
        print("Principales estadísticos de las columnas categóricas:")
        display(df.describe(include="O").T)
    
    else: 
        print("\nEl dataframe no tiene columnas categóricas. \n")

    ## Comprobar si hay columnas numéricas y mostrar info de esas columnas
    col_numericas = df.select_dtypes(exclude = "O").columns
    if len(col_numericas) > 0: 
        print("Principales estadísticos de las columnas numéricas:")
        display(df.describe(exclude="O").T)

    return df_info




## Función para cambiar valores negativos a positivos: 

def negativos(num):

    """
    Función para cambiar valores negativos a positivos

    """
    return abs(num) 




## Función para reemplazar espacios por guiones bajos y a minusculas: 

def espacios_guion_bajo(df):
    """
    Función para reemplazar los espacios en las columnas por guiones bajos 
    y convertirlas a minúsculas.
    
    Parámetros:
    df (DataFrame): DF cuyas columnas se desean modificar.

    Devuelve:
    DataFrame: DF con los nombres de las columnas modificados.
    """
    # Convertir nombres de columnas a minúsculas y reemplazar espacios por guiones bajos
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]
    return df

## Función para convertir a numero entero: 


def entero(df, columna):
    """
    Convierte una columna específica de un DataFrame a tipo entero (si la columna está presente). 

    Si no está, devuelve el mensaje indicando eso
    
    """
    # Comprobar si la columna existe en el DataFrame
    if columna in df.columns:
        # Convertir la columna a tipo entero (permitiendo valores nulos con 'Int64')
        df[columna] = df[columna].astype('Int64')
        print(f'Columna "{columna}" convertida a enteros.')
    else:
        print(f'La columna "{columna}" no se encuentra en el DataFrame.')
    
    return df



## Función para convertir a numero entero: 


def dos_decimales(df, col):
    """
    Cambia los decimales de los valores float a dos decimales en una columna del DataFrame. 
    """
    # Redondear los valores de la columna especificada a 2 decimales
    df[col] = df[col].round(2)
    
    return df


## FUNCIONES AB TESTING. 

def normalidad(dataframe, columna):
    """
    Evalúa la normalidad de una columna de datos de un DataFrame utilizando la prueba de Shapiro-Wilk.

    Parámetros:
        dataframe (DataFrame): El DataFrame que contiene los datos.
        columna (str): El nombre de la columna en el DataFrame que se va a evaluar para la normalidad.

    Returns:
        None: Imprime un mensaje indicando si los datos siguen o no una distribución normal.
    """

    statistic, p_value = stats.shapiro(dataframe[columna])
    if p_value > 0.05:
        print(f"Para la columna {columna} los datos siguen una distribución normal.")
    else:
        print(f"Para la columna {columna} los datos no siguen una distribución normal.")


# vamos a definir una función para poder hacer el t-test de Student

def prueba_hipotesis(*args):
    
    # lo primero que tenemos que hacer es mirar si las varianzas son iguales o no
    if len(args) == 2:
        p_valor_varianza = stats.levene(*args, center = "median")[1]
    else:
        p_valor_varianza = stats.bartlett(*args)[1]
    
    if p_valor_varianza > 0.05:
        # realizamos la prueba t de Student
        t_stat, p_valor = stats.ttest_ind(*args, equal_var=True)
    else:
        t_stat, p_valor = stats.ttest_ind(*args, equal_var=False)
        
    # Establecemos un nivel de significancia (alfa)
    alfa = 0.05

    # comparamos el p-valor con el nivel de significancia
    if p_valor < alfa:
        print("Rechazamos la hipótesis nula.")
        print("Hay una diferencia significativa en la variable analizada entre los dos grupos.")
    else:
        print("No podemos rechazar la hipótesis nula.")
        print("No hay evidencia suficiente para afirmar una diferencia significativa en la variable analizada entre los dos grupos.")



