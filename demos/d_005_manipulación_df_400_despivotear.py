# 7 exploraremos técnicas avanzadas de manipulación de datos utilizando pandas. 
# Esto incluye operaciones complejas de agrupación, pivotaje, y manejo de datos de series temporales.

# 2. Pivotaje y Despivotaje
# Crear tablas pivote
# Las tablas pivote son útiles para reorganizar y resumir datos.

import pandas as pd

print('\n')
# Crear un DataFrame de ejemplo
print('Crear un DataFrame de ejemplo')
data = {
    'ID': [1, 2, 3],
    'Nombre': ['Ana', 'Luis', 'Carlos'],
    'Edad': [28, 34, 29]
}
df = pd.DataFrame(data)
print(df,'\n')

# Despivotar el DataFrame
print('Despivotar el DataFrame')
melted = pd.melt(df, id_vars='ID', value_vars=['Nombre', 'Edad'], var_name='Atributo', value_name='Valor')
print(melted,'\n')