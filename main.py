## Importacíón librerias
#%%
import pandas as pd
import numpy as np
from src import soporte_funciones as spt

#%%
prueba_main = pd.read_csv('files/filas_duplicadas.csv')
#%%
spt.exploracion(prueba_main)
# %%
