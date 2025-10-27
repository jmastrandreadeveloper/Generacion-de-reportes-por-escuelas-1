# Limpieza de Datos con pandas
# En este tutorial, aprenderás cómo limpiar y preparar datos en pandas. 
# La limpieza de datos es un paso crucial en el análisis de datos, 
# ya que los datos en el mundo real a menudo están incompletos, 
# contienen errores o están en formatos inconsistentes.

import pandas as pd

print('\n')
# Transformación de Datos
print('Crear un DataFrame de ejemplo con valores tipo string(obj) cuando deberían ser enteros')
# Cambio de tipo de datos
# Puedes cambiar el tipo de datos de una columna utilizando astype.
# Crear un DataFrame de ejemplo
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Edad': ['28', '34', '29', '42']
}
df = pd.DataFrame(data)
print(df,'\n')
print(df.dtypes,'\n')

# Cambiar el tipo de datos de la columna 'Edad' a entero
print('Cambiar el tipo de datos de la columna Edad a entero')
df['Edad'] = df['Edad'].astype(int)

print(df,'\n')
print(df.dtypes,'\n')