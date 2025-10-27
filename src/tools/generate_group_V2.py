import os
import re

def generate_group_aggregation_functions_V2(group_params_dict, output_dir):
    """Genera funciones de agrupación y filtrado y las guarda en subdirectorios específicos."""
    os.makedirs(output_dir, exist_ok=True)

    for function_name, params in group_params_dict.items():
        columns, agg_dict, rename_params, *optional_params = params
        filter_params = optional_params[0] if optional_params else {}
        filter_columns = filter_params.get("filter", [])

        function_dir = os.path.join(output_dir, function_name)
        os.makedirs(function_dir, exist_ok=True)
        file_path = os.path.join(function_dir, f"group_{function_name}.py")

        contenido_existente = leer_archivo(file_path)
        if contenido_existente and re.search(rf"def {function_name}_group\(.*\):", contenido_existente):
            print(f"La función '{function_name}_group' ya existe en {file_path} y no será sobrescrita.")
            continue

        function_content = generate_group_function_content(function_name, columns, agg_dict, rename_params)
        if filter_columns:
            function_content += generate_filter_function_content(function_name, filter_columns)

        with open(file_path, 'a', encoding='utf-8') as f:
            if contenido_existente:
                f.write("\n\n")
            f.write(function_content)

        print(f"Función '{function_name}' generada exitosamente en {file_path}")

def generate_group_function_content(function_name, columns, agg_dict, rename_params):
    """Genera el contenido de una función de agrupación."""
    agg_operations = {col: func for func, col in agg_dict.items()}
    group_columns = [col for col in columns if col not in agg_operations.keys()]
    rename_columns = rename_params.get("rename_columns", {})
    
    function_content = "import pandas as pd\n"
    function_content += "import os\n"
    function_content += "import sys\n"
    function_content += "import json\n\n"

    function_content += "project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..' ))\n"
    function_content += "sys.path.append(project_root)\n"
    
    function_content += "import src.tools.utils as u\n"
    function_content += "import src.modelos.Libs.validar_columna as valCols\n"
    function_content += "from  src.modelos.Libs.filtrado_condicional import aplicar_condiciones_avanzadas\n\n"

    function_content += "def {0}_group(dataframe):\n".format(function_name)
    function_content += "    required_columns = {0}\n\n".format(columns)

    function_content += "    # Validar las columnas requeridas\n"
    function_content += "    missing_columns = valCols.validar_columnas(dataframe, required_columns)\n\n"

    function_content += "    if missing_columns:\n"
    function_content += "        raise ValueError(f'Columnas faltantes en el DataFrame: {{missing_columns}}')\n\n"


    function_content += "    result = dataframe.groupby({0}).agg({1})\n".format(group_columns, agg_operations)
    function_content += "    result.reset_index(inplace=True)\n"
    function_content += "    result.rename(columns={0}, inplace=True)\n".format(rename_columns)
    function_content += "    return result\n\n"
    return function_content

def generate_filter_function_content(function_name, filter_columns):
    """Genera el contenido de una función de filtrado."""
    function_content = "def {0}_filter({1}, dataframe, show_index=True, columns=None, orientacion='records', condiciones=None):\n".format(function_name, filter_columns[0])
    function_content += "    try:\n"
    function_content += "        if {0} not in dataframe['{0}'].unique():\n".format(filter_columns[0])
    function_content += "            return []\n\n"
    function_content += "        dFrame_filtrado = dataframe[dataframe['{0}'] == {0}]\n".format(filter_columns[0])
    function_content += "        if condiciones:\n"
    function_content += "            dFrame_filtrado = aplicar_condiciones_avanzadas(dFrame_filtrado, condiciones)\n\n"
    function_content += "        if columns:\n"
    function_content += "            missing_columns = set(columns) - set(dFrame_filtrado.columns)\n"
    function_content += "            if missing_columns:\n"
    function_content += "                raise ValueError(f'Columnas faltantes en el DataFrame filtrado: {missing_columns}')\n"
    function_content += "            dFrame_filtrado = dFrame_filtrado[columns]\n\n"
    function_content += "        if not show_index:\n"
    function_content += "            dFrame_filtrado = dFrame_filtrado.reset_index(drop=True)\n\n"
    function_content += "        return dFrame_filtrado.to_dict(orient=orientacion)\n"
    function_content += "    except Exception as e:\n"
    function_content += "        raise ValueError(f'Error al filtrar el DataFrame: {e}')\n\n"
    return function_content

def leer_archivo(file_path):
    """Lee el contenido de un archivo si existe."""
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""


#------------------------------------------------------------------------------------------------------------
# import os
# import re

# def generate_group_aggregation_functions_V2(group_params_dict, output_dir):
#     """Genera funciones de agrupación y las guarda en subdirectorios específicos."""
#     # Crear el directorio base si no existe
#     os.makedirs(output_dir, exist_ok=True)

#     for function_name, params in group_params_dict.items():
#         # Desempaquetar valores, asegurando compatibilidad con la nueva estructura
#         columns, agg_dict = params[:2]
#         rename_columns = params[2].get('rename_columns', {}) if len(params) > 2 else {}
        
#         # Crear subdirectorio con el nombre de la función
#         function_dir = os.path.join(output_dir, function_name)
#         os.makedirs(function_dir, exist_ok=True)

#         # Definir el archivo dentro del subdirectorio
#         file_path = os.path.join(function_dir, f"group_{function_name}.py")

#         # Leer contenido existente
#         contenido_existente = leer_archivo(file_path)

#         # Verificar si la función ya existe en el archivo
#         if contenido_existente and re.search(rf"def {function_name}_group\(.*\):", contenido_existente):
#             print(f"La función '{function_name}_group' ya existe en {file_path} y no será sobrescrita.")
#             continue

#         # Generar contenido de la nueva función
#         function_content = generate_group_function_content(function_name, columns, agg_dict, rename_columns)

#         # Agregar nueva función al archivo sin sobrescribir el contenido existente
#         with open(file_path, 'a', encoding='utf-8') as f:
#             if contenido_existente:  # Añadir separador si ya hay contenido previo
#                 f.write("\n\n")
#             f.write(function_content)

#         print(f"Función '{function_name}' generada exitosamente en {file_path}")


# def generate_group_function_content(function_name, columns, agg_dict, rename_columns):
#     """Genera el contenido de una función de agrupación."""
#     agg_operations = {col: func for func, col in agg_dict.items()}

#     # Remover columnas de agregación de las columnas de agrupación
#     group_columns = [col for col in columns if col not in agg_operations.keys()]

#     # Eliminar duplicados preservando el orden
#     required_columns = []
#     seen = set()
#     for col in columns + list(agg_operations.keys()):
#         if col not in seen:
#             required_columns.append(col)
#             seen.add(col)

#     function_content = """
# import pandas as pd
# import os
# import sys

# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
# sys.path.append(project_root)

# import src.tools.utils as u
# import src.modelos.Libs.validar_columna as valCols
# """.strip() + "\n\n"

#     function_content += f"def {function_name}_group(dataframe):\n"
#     function_content += f"    required_columns = {required_columns}\n"
#     function_content += f"    missing_columns = valCols.validar_columnas(dataframe, required_columns)\n"
#     function_content += f"    if missing_columns:\n"
#     function_content += f"        raise ValueError(f'Columnas faltantes en el DataFrame: {{missing_columns}}')\n"
#     function_content += f"    result = dataframe.groupby({group_columns}).agg({agg_operations})\n"
#     function_content += f"    result.reset_index(inplace=True)\n"

#     if rename_columns:
#         function_content += f"    result.rename(columns={rename_columns}, inplace=True)\n"

#     function_content += f"    return result\n"

#     return function_content


# def leer_archivo(file_path):
#     """Lee el contenido de un archivo si existe."""
#     if os.path.exists(file_path):
#         with open(file_path, 'r', encoding='utf-8') as f:
#             return f.read()
#     return ""
