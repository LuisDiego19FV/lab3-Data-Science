#Universidad del Valle de Guatemala
#23/07/2020
#Luis Esturban 17256
#Luis Fernandez 16344
#Juan Menchu 16150
#Lab3
import pandas as pd
import numpy as np

url = 'D:/aptos2019-blindness-detection/train.csv'
df = pd.read_csv(url)

print(df.head(1))
#Se verifica el nombre de las columnas que tiene el dataframe
print('Nombre columnas:',df.columns)
#Se examina la cantidad de filas y columnas que tiene el dataframe
print('Cantidad de Filas y columnas:',df.shape)
#Se verifica si la informacion tiene informacion nula
df.info()
#Tabla de frecuencia
print(pd.value_counts(df["diagnosis"]))
#Se crea un pequenio resumen de los datos
print(df.describe())