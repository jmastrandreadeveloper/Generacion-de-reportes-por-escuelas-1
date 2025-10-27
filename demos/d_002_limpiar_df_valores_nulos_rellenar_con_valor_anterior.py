# Limpieza de Datos con pandas
# En este tutorial, aprenderás cómo limpiar y preparar datos en pandas. 
# La limpieza de datos es un paso crucial en el análisis de datos, 
# ya que los datos en el mundo real a menudo están incompletos, 
# contienen errores o están en formatos inconsistentes.

import pandas as pd

print('\n')
print('Crear un DataFrame de ejemplo con valores nulos')
data = {
    'Nombre': ['Ana', 'Luis', None, 'Marta'],
    'Edad': [28, None, 29, 42],
    'Ciudad': ['Guaymallén', 'Godoy Cruz', 'San Rafael', None]
}
df = pd.DataFrame(data)
print(df,'\n')

# 1-Manejo de Valores Nulos
# Rellenar valores nulos
# Puedes rellenar valores nulos con un valor específico o utilizando métodos como fillna.
# Rellenar valores nulos con el valor anterior en la columna
print('Rellenar valores nulos con el valor anterior en la columna')
df_rellenado_ffill = df.ffill()
print(df_rellenado_ffill,'\n')

print('Rellenar valores nulos con el valor siguiente en la columna usando bfill')
df_rellenado_bfill = df.bfill()
print(df_rellenado_bfill)