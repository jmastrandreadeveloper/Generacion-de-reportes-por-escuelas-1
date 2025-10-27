import pandas as pd

print('\n')
# 4. Creación de un DataFrame vacío y luego agregar datos
# A veces es útil crear un DataFrame vacío y luego agregar datos fila por fila.
print('Crear un DataFrame vacío con columnas específicas')
df = pd.DataFrame(columns=['Nombre', 'Edad', 'Ciudad'])
# Agregar filas al DataFrame
df = df._append({'Nombre': 'Ana', 'Edad': 28, 'Ciudad': 'Guaymallén'}, ignore_index=True)
df = df._append({'Nombre': 'Luis', 'Edad': 34, 'Ciudad': 'Godoy Cruz'}, ignore_index=True)
df = df._append({'Nombre': 'Carlos', 'Edad': 29, 'Ciudad': 'San Rafael'}, ignore_index=True)
df = df._append({'Nombre': 'Marta', 'Edad': 42, 'Ciudad': 'San Martín'}, ignore_index=True)
# Mostrar el DataFrame
print(df,'\n')