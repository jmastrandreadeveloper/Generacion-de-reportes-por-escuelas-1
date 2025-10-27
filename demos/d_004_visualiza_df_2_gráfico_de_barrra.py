# 2 Gráfico de Barra
# Un gráfico de barra es útil para comparar diferentes categorías.

import pandas as pd
import matplotlib.pyplot as plt

print('\n')
# Crear un DataFrame de ejemplo
print('Crear un DataFrame de ejemplo')
data = {
    'Producto': ['A', 'B', 'C', 'D'],
    'Ventas': [150, 200, 250, 300]
}
df = pd.DataFrame(data)
print(df,'\n')

# Crear un gráfico de barra
df.plot(kind='bar', x='Producto', y='Ventas', title='Ventas por Producto')
plt.ylabel('Ventas')
plt.show()