
# Evaluación Módulo 3: Transformación de Datos


## Descripción
Este proyecto corresponde a la evaluación final del Módulo 3 del curso de Adalab de Análisis de Datos. El objetivo principal es aplicar técnicas de transformación, limpieza y visualización de datos sobre un conjunto de datos relacionados con el comportamiento de los clientes dentro de un programa de lealtad de una aerolínea. Utilizamos herramientas de Pandas, Matplotlib, Seaborn y SciPy para analizar los datos.

## Objetivo
- Exploración y limpieza de datos: Identificar y tratar valores nulos, atípicos o inconsistentes.
- Transformación de datos: Crear nuevas columnas, agrupar o filtrar información según sea necesario.
- Análisis de datos: Explorar patrones y tendencias en los datos.
- Visualización de datos: Crear gráficos para comunicar los hallazgos.
- Evaluación de diferencias en reservas de vuelos según el nivel educativo.

## Datos
El proyecto utiliza dos archivos CSV que describen el comportamiento de los clientes dentro del programa de lealtad de la aerolínea:

1) Customer Flight Analysis.csv: Información sobre la actividad de vuelo de los clientes, incluyendo el número de vuelos, distancia volada, puntos acumulados y redimidos, y costos asociados a los puntos redimidos.

2) Customer Loyalty History.csv: Información detallada sobre el perfil de los clientes, como su ubicación, nivel educativo, ingresos, estado civil, tipo de tarjeta de lealtad y más.


## Estructura del Proyecto

- Carpeta 'Files': contiene los CSVs con los datos utilizados para el análisis, el CSV de las filas duplicadas que se eliminaron y el CSV con los datos finales, luego del filtrado y la limpieza. 
- Carpeta 'src': contiene el archivo py de soporte de funciones que se utilizaron en el archivo principal de la evaluación. 
- Archivo 'fase_1_2': contiene el análisis exploratorio y la transformación y limpieza de datos. 
- Archivo 'fase_3': incluye el análisis descriptivo, análisis estadístico y AB testing. 
- Archivo main: archivo py. No utilizado en este proyecto ya que se utilizó un archivo Jupyter para el análisis. 

## Fases del Proyecto

###  Fase 1: Exploración y Limpieza de Datos

Exploración Inicial:

- Inspección de los datos para identificar valores nulos, atípicos y la estructura de los datos.
- Análisis de la distribución de los datos y las estadísticas descriptivas para entender su naturaleza.

Limpieza de Datos:

- Tratamiento y eliminación de valores nulos en las columnas clave.
- Verificación de la consistencia de los datos (tipos de datos, rangos válidos, etc.).
- Conversión de los tipos de datos necesarios para el análisis.

### Fase 2: Visualización de Datos

Utilizando herramientas de visualización con Matplotlib y Seaborn, se generaron las siguientes visualizaciones:

1) Distribución de la cantidad de vuelos reservados por mes.
2) Relación entre la distancia de los vuelos y los puntos acumulados.
3) Distribución de los clientes por provincia o estado.
4) Comparación del salario promedio entre los diferentes niveles educativos.
5) Proporción de clientes con diferentes tipos de tarjetas de fidelidad.
6) Distribución de los clientes según su estado civil y género.

###  Fase 3: Análisis de Diferencias en Reservas de Vuelos por Nivel Educativo

Filtramos el conjunto de datos para trabajar solo con las columnas relevantes: Flights Booked y Education.
Agrupamos los datos por nivel educativo y calculamos estadísticas descriptivas como el promedio y la desviación estándar del número de vuelos reservados.
Realizamos una prueba de hipótesis para determinar si existen diferencias significativas en el número de vuelos reservados según el nivel educativo.


## Metodología

Pandas se utilizó para la limpieza, transformación y análisis de los datos.
Matplotlib y Seaborn se emplearon para la visualización de las tendencias y patrones en los datos.
SciPy se utilizó para realizar pruebas estadísticas (test A/B) y análisis inferencial.


## Requisitos

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy (para análisis estadísticos)










