# 6 Gráfico de Calor (Heatmap)
# Un gráfico de calor es útil para mostrar correlaciones entre variables.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print('\n')
# Crear un DataFrame de ejemplo
print('Crear un DataFrame de ejemplo')
data = {
    'A': [1, 21, 3, 4, 5],
    'B': [15, 4, 3, 2, 1],
    'C': [2, 32, 4, 52, 6]
}
df = pd.DataFrame(data)
print(df,'\n')

# Crear una matriz de correlación
print('Crear una matriz de correlación')
corr = df.corr()
print(corr,'\n')

# Crear un gráfico de calor
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlación')
plt.show()