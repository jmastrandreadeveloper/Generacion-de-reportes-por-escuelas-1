# 7 exploraremos técnicas avanzadas de manipulación de datos utilizando pandas. 
# Esto incluye operaciones complejas de agrupación, pivotaje, y manejo de datos de series temporales.

# 1. Agrupación Avanzada
# Agrupación y transformación
# Puedes aplicar transformaciones a grupos específicos utilizando transform.

import pandas as pd

print('\n')
# Crear un DataFrame de ejemplo
print('Crear un DataFrame de ejemplo')
data = {
    'Grupo': ['A', 'A', 'B', 'B'],
    'Valor': [10, 15, 20, 25]
}
df = pd.DataFrame(data)
print(df,'\n')

# Calcular la media del grupo y restarla de cada valor
print('Calcular la media del grupo y restarla de cada valor')
df['Valor Ajustado'] = df.groupby('Grupo')['Valor'].transform(lambda x: x - x.mean())
print(df,'\n')