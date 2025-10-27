# Limpieza de Datos con pandas
# En este tutorial, aprenderás cómo limpiar y preparar datos en pandas. 
# La limpieza de datos es un paso crucial en el análisis de datos, 
# ya que los datos en el mundo real a menudo están incompletos, 
# contienen errores o están en formatos inconsistentes.

import pandas as pd

print('\n')
# Convertir columnas a tipo datetime
# Puedes convertir columnas a tipo datetime utilizando pd.to_datetime.
# Crear un DataFrame de ejemplo
print('Crear un DataFrame de ejemplo')
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Fecha': ['2023-01-01', '2023-05-12', '2023-07-19', '2023-11-30']
}
df = pd.DataFrame(data)
print(df,'\n')

# Convertir la columna 'Fecha' a tipo datetime
print('Convertir la columna Fecha a tipo datetime')
df['Fecha'] = pd.to_datetime(df['Fecha'])
print(df.dtypes,'\n')

# Extraer el año, mes y día
print('Extraer el año, mes y día')
df['Año'] = df['Fecha'].dt.year
df['Mes'] = df['Fecha'].dt.month
df['Día'] = df['Fecha'].dt.day
print(df,'\n')