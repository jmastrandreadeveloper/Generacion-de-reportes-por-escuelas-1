# 3 Histograma
# Un histograma es útil para mostrar la distribución de una variable.

import pandas as pd
import matplotlib.pyplot as plt

print('\n')
# Crear un DataFrame de ejemplo
print('Crear un DataFrame de ejemplo')
data = {
    'Edad': [23, 45, 56, 67, 29, 34, 42, 55, 63, 31]
}
df = pd.DataFrame(data)
print(df,'\n')

# Crear un histograma
df.plot(kind='hist', y='Edad', bins=5, title='Distribución de Edades')
plt.xlabel('Edad')
plt.show()