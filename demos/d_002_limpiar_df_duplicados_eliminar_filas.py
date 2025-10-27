# Limpieza de Datos con pandas
# En este tutorial, aprenderás cómo limpiar y preparar datos en pandas. 
# La limpieza de datos es un paso crucial en el análisis de datos, 
# ya que los datos en el mundo real a menudo están incompletos, 
# contienen errores o están en formatos inconsistentes.

import pandas as pd

print('\n')
# 2. Eliminación de Duplicados
print('Crear un DataFrame de ejemplo con valores duplicados')
# Crear un DataFrame de ejemplo con duplicados
data = {
    'Nombre': ['Ana', 'Luis', 'Ana', 'Marta'],
    'Edad': [28, 34, 28, 42],
    'Ciudad': ['Guaymallén', 'Godoy Cruz', 'Guaymallén', 'San Martín']
}
df = pd.DataFrame(data)
print(df,'\n')

# Eliminar filas duplicadas
# Puedes eliminar filas duplicadas utilizando drop_duplicates.
print('Eliminar filas duplicadas')
df_sin_duplicados = df.drop_duplicates()
print(df_sin_duplicados,'\n')