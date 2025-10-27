import pandas as pd
import json
import os
import sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(project_root)
import src.tools.utils as u
import src.tools.data_loading as u

# Datos de ejemplo
codigos = ['C1', 'C2', 'C3']
diccionarios = [
    {'nombre': 'Juan', 'edad': 25},
    {'nombre': 'María', 'edad': 30},
    {'nombre': 'Pedro', 'edad': 35}
]

# Convertir diccionarios a JSON
json_diccionarios = [json.dumps(d) for d in diccionarios]

# Crear DataFrame
df = pd.DataFrame({
    'Código': codigos,
    'Diccionario': json_diccionarios
})

print(df)

# Función para obtener valor asociado por código
def obtener_valor_asociado(df, codigo):
    fila = df[df['Código'] == codigo]
    if not fila.empty:
        return json.loads(fila['Diccionario'].values[0])
    else:
        return None

# Ejemplo de uso
codigo_busqueda = 'C2'
valor_asociado = obtener_valor_asociado(df, codigo_busqueda)

if valor_asociado:
    print(f"Valor asociado al código {codigo_busqueda}:")
    print(json.dumps(valor_asociado, indent=4))
else:
    print(f"No se encontró valor asociado al código {codigo_busqueda}")

u.guardar_dataframe_a_csv(df,'data/processed/transformed/Nominal/_df_json.csv')
csv_path_1 = os.path.join(project_root, 'data', 'processed', 'transformed', 'Nominal', '_df_json.csv')
_df_json = u.cargar_csv(csv_path_1)

valor_asociado = obtener_valor_asociado(_df_json, 'C2')

print(json.dumps(valor_asociado, indent=4))



