# Limpieza de Datos con pandas
# En este tutorial, aprenderás cómo limpiar y preparar datos en pandas. 
# La limpieza de datos es un paso crucial en el análisis de datos, 
# ya que los datos en el mundo real a menudo están incompletos, 
# contienen errores o están en formatos inconsistentes.

import pandas as pd

print('\n')
# Crear un DataFrame de ejemplo
print('Crear un DataFrame de ejemplo')
data = {
    'Nombre': ['Ana', 'Luis', 'Ana', 'Marta'],
    'Edad': [28, 34, 28, 42],
    'Ciudad': ['Guaymallén', 'Godoy Cruz', 'Guaymallén', 'San Martín']
}
df = pd.DataFrame(data)
print(df,'\n')

# Renombrar columnas
# Puedes renombrar columnas utilizando rename.
# Renombrar columnas
print('Renombrar columnas')
df_renombrado = df.rename(columns={'Nombre': 'Nombre_Completo', 'Edad': 'Años'})
print(df_renombrado,'\n')