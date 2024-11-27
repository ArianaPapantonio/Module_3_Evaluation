import pandas as pd
import numpy as np

# Visualización
# ------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

# Evaluar linealidad de las relaciones entre las variables
# y la distribución de las variables
# ------------------------------------------------------------------------------
#from scipy.stats import shapiro, kstest, poisson, chisquare, ttest_ind, levene, bartlett, sem, ppf
import scipy.stats as stats
from scipy.stats import shapiro, levene
from scipy.stats import ttest_ind
from scipy.stats import mannwhitneyu
from scipy.stats import chi2_contingency

def intervalo(dataframe, columna, nivel = 0.95):

    """falta terminar de documentar"""
    
    media = dataframe[columna].mean()
    error = stats.sem(dataframe[columna], nan_policy="omit")
    
    grados_libertad = len(dataframe[columna]) - 1

    valor_crit = stats.t.ppf((1 + nivel)/2, df=grados_libertad)

    limite_inferior = media - valor_crit * error
    limite_superior = media + valor_crit * error

    print(f"El intervalo del {nivel} para la columna {columna} es {round(limite_inferior, 2)} -> {round(limite_superior, 2)}")