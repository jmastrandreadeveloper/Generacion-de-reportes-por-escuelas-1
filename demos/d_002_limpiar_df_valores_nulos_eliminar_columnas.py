# Limpieza de Datos con pandas
# En este tutorial, aprenderás cómo limpiar y preparar datos en pandas. 
# La limpieza de datos es un paso crucial en el análisis de datos, 
# ya que los datos en el mundo real a menudo están incompletos, 
# contienen errores o están en formatos inconsistentes.

import pandas as pd

print('\n')
print('_'*50 + '\n 0_Crear un DataFrame de ejemplo con valores nulos______________\n' + '_'*50)
data = {
    'Nombre': ['Ana', 'Luis', None, 'Marta'],
    'Edad': [28, None, 29, 42],
    'Ciudad': ['Guaymallén', 'Godoy Cruz', 'San Rafael', None]
}
df = pd.DataFrame(data)
print(df,'\n')

# 1-Manejo de Valores Nulos
# Puedes eliminar filas o columnas que contienen valores nulos utilizando dropna.
print('Eliminar columnas con cualquier valor nulo')
# Eliminar columnas con cualquier valor nulo
df_sin_nulos_col = df.dropna(axis=1)
print(df_sin_nulos_col,'\n')