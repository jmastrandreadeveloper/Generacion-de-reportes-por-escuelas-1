import numpy as np
import pandas as pd
#import plotly.express as px  # Correct import for plotly.express
#import configfile as cf
#from tabulate import tabulatepip
import matplotlib.pyplot as plt 
from matplotlib.font_manager import FontProperties



def Plotly_stacked_bar_Chart(dictData , colores , index ):    
    dataFrame = pd.DataFrame(dictData).set_index(index)
    # no se puede centrar el texto dentro del grafico
    # https://github.com/plotly/plotly.js/issues/3524
    # tipo es : desempeño o prosodia
    # pasamos el objeto escuela para poder crear el archivo con el nombre de la escuela y todos los datos de la misma
    # debemos crear una carpeta para poder mantener las imagenes para cada escuela..
    
    
    # renombramos los nombres de las columnas...para que quede como el original
    #listaColumnas = list(dataFrame.columns.values)
    #dataFrame.rename(columns = {listaColumnas[1]:' Sup. (' + str(listaColumnas[1]) + ')' , 
    #                            listaColumnas[2]:' Provincial' + ' ' + listaColumnas[0]
    #                           }, inplace = True)
    # transponer el dataframe
    dataFrame = dataFrame.transpose()
    dataFrame = dataFrame.round(1)
    
    fig = px.bar(dataFrame ,    
                 barmode = 'stack' , 
                 text_auto = '5.92f' ,                 
                 color_discrete_sequence = colores, # ["#8A68A6", "#F1D447", "#A1C16D", "#0594A4"]
                 title = '',
                 width=1900, height=1900
                 )
    fig.update_layout(#xaxis_title = 'Nivel de Fluidez' + ' - ' + tipoDesempeñoOProsodia + ' - ',     
                      xaxis_title = ' ',     
                      yaxis_tickformat = "%f" , 
                      legend = dict(orientation = "h" , 
                                    yanchor = "top" , 
                                    #xanchor="left",                                    
                                    xanchor = 'center',
                                    y = -0.15,
                                    x = 0.5),
                      yaxis = {'visible' : False, 'showticklabels' : True},
                      legend_title_text = '' 
                     )
    fig.update_traces(textposition = 'auto' , 
                      textfont_size = 70 , # 80 , # 25, # 78
                      #textangle=90,
                      #textfont_color  = 'White',
                      textfont_family = 'Calibri',                      
                      texttemplate = "%{value:} %",
                      textangle = 0,
                      cliponaxis = False
                      )
    fig.update_layout(bargap=0.30)
    #fig.update_traces(width = 0.4)
    fig.update_traces(textangle=0)
    fig.update_xaxes(tickangle=0)
    fig.update_layout({ 'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})

    fig.update_layout(  legend       = dict(font = dict(family = "Calibri", size = 70, color = "black")),
                        legend_title = dict(font = dict(family = "Calibri", size = 70, color = "black")))

    fig.update_traces(width  = 0.55) # ancho de las barras 
    fig.update_layout(bargap = 0.9) # agujero entre las barras NO FUNCIONA
    
    fig.update_layout(xaxis = dict(
                      tickfont = dict(size=60)) # para regular el tamaño de las letras debajo de las barras ) 
                     )
    

    #fig.write_image(nombreArchivo)
    return fig

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def Matplotlib_stacked_bar_chart(
    dictData, 
    colores, 
    index, 
    bar_width=0.05,                                 
    width_per_bar=2.5,  # Controla cuán "ancho" es cada barra (en pulgadas)
    bar_height=8):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    # Convertir el diccionario en un DataFrame
    dataFrame = pd.DataFrame(dictData).set_index(index).transpose()
    dataFrame = dataFrame.round(1)

    # Crear la figura y los ejes
    fig, ax = plt.subplots(figsize=(15, 15))  # Tamaño de la figura
    
    # Calcular tamaño dinámico de la figura basado en cantidad de barras
    # num_barras = len(dataFrame.index)    
    # ancho_total = max(num_barras * width_per_bar, 4)  # mínimo 4 pulgadas    
    # fig, ax = plt.subplots(figsize=(ancho_total, height))

    # Definir la posición de las barras
    x = np.arange(len(dataFrame.index))

    # Inicializar la base para la pila
    bottom = np.zeros(len(dataFrame.index))

    # Iterar sobre las columnas para apilar las barras
    for i, (column, color) in enumerate(zip(dataFrame.columns, colores)):
        ax.bar(x, dataFrame[column], label=column, color=color,  width=bar_width, bottom=bottom , )
        bottom += dataFrame[column]  # Acumular valores para la pila

        # Agregar etiquetas de valor en cada barra
        for j, val in enumerate(dataFrame[column]):
            if val > 0:  # Evitar etiquetas en barras de valor 0
                ax.text(x[j], bottom[j] - val / 2, f"{val:.1f}%",
                        ha='center', va='center', fontsize=40, color='white', fontweight='bold')

    # Configuración de ejes y diseño
    ax.set_xticks(x)
    ax.set_xticklabels(dataFrame.index, fontsize=40)
    ax.set_yticklabels([])  # Ocultar etiquetas del eje Y
    ax.set_ylabel("")
    ax.set_title("", fontsize=16)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=len(dataFrame.columns), fontsize=20)

    # Eliminar bordes del gráfico
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Ajustar márgenes
    plt.tight_layout()

    return fig

def Matplotlib_stacked_bar_chart_2(dictData, colores, index='Número'):
    # Convertir el diccionario en un DataFrame
    df = pd.DataFrame(dictData).set_index(index)
    df = df[['Crítico', 'Básico', 'Medio', 'Avanzado']]  # Asegurar orden    
    df = df.round(1)

    # Crear la figura y los ejes
    fig, ax = plt.subplots(figsize=(40, 20))  # Tamaño de la figura

    # Definir la posición de las barras y el ancho
    bar_width = 100.8  # Antes era 0.5
    espaciado = 150.5  # Podés probar con 1.2, 1.3, etc.
    x = np.arange(len(df.index)) * espaciado

    # Inicializar la base para la pila
    bottom = np.zeros(len(df.index))

    # Iterar sobre las columnas para apilar las barras
    for i, (column, color) in enumerate(zip(df.columns, colores)):
        ax.bar(x, df[column], label=column, color=color, width=bar_width, bottom=bottom)
        
        # Etiquetas en el centro de cada barra apilada
        for j, val in enumerate(df[column]):
            # Etiquetas dentro de las barras
            hex_color = mcolors.to_hex(color)
            text_color = get_contrasting_text_color(hex_color)
            if val > 0:
                ax.text(x[j], bottom[j] + val / 2, f"{val:.1f}%", 
                        ha='center', va='center', fontsize=35, color=text_color, fontweight='bold')
        
        bottom += df[column]  # Acumular la altura para la pila

    # Etiquetas en el eje X
    ax.set_xticks(x)
    ax.set_xticklabels(df.index, rotation=0, ha='center', fontsize=32)  # Más grande y horizontal tamaño de los numeros d elas eculeas
    ax.tick_params(axis='x', pad=10)  # Aumentá el padding si querés más espacio

    # Ocultar etiquetas del eje Y si no las necesitás
    ax.set_yticks([])
    ax.set_ylabel("")
    
    # Eliminar bordes del gráfico
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Título y leyenda más grandes
    #ax.set_title("Desempeño por Escuela", fontsize=0, fontweight='bold')
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.08), ncol=len(df.columns), fontsize=40)

    plt.tight_layout()
    return fig

import matplotlib.pyplot as plt

# def Matplotlib_bar_chart(dictData, colores, index, columnas_a_excluir=None):
#     """
#     Genera un gráfico de barras a partir de un diccionario de datos.
    
#     Parámetros:
#     - dictData: diccionario con los datos (por ejemplo, fila de un DataFrame convertido con .to_dict()).
#     - colores: lista de colores para las barras.
#     - index: valor identificador para el título del gráfico (como Escuela_ID).
#     - columnas_a_excluir: lista de claves a excluir del gráfico (como ['Escuela_ID', 'total_alumnos']).
    
#     Retorna:
#     - fig: objeto Figure de matplotlib.
#     """

#     # Asegura que columnas_a_excluir sea una lista (puede ser None)
#     columnas_a_excluir = columnas_a_excluir or []

#     # Filtra las claves según lo que se desea excluir
#     etiquetas = [k for k in dictData.keys() if k not in columnas_a_excluir]
#     valores = [dictData[k] for k in etiquetas]

#     # Crea figura y ejes
#     fig, ax = plt.subplots(figsize=(10, 5))

#     # Ajusta colores si no hay suficientes
#     if not colores or len(colores) < len(etiquetas):
#         colores = plt.cm.Paired(range(len(etiquetas)))

#     # Dibuja las barras
#     ax.bar(etiquetas, valores, color=colores[:len(etiquetas)])

#     # Etiquetas y título
#     ax.set_title(f'Distribución por porcentaje de respuestas correctas - Escuela {index}')
#     ax.set_xlabel('Porcentaje de respuestas correctas')
#     ax.set_ylabel('Cantidad de estudiantes')

#     # Mostrar valores arriba de las barras
#     for i, valor in enumerate(valores):
#         ax.text(i, valor + 1, str(valor), ha='center', va='bottom')

#     plt.tight_layout()
#     return fig

# def Matplotlib_stacked_bar_chart_from_df(
#     df,
#     colores,
#     columnas_a_incluir=None,
#     index='resultado',
#     fig_size=(10, 6),
#     fontsize_labels=12,
#     fontsize_legend=12
# ):
#     df = df.copy()

#     # Asegurarse de que las columnas a incluir estén definidas
#     if columnas_a_incluir is None:
#         columnas_a_incluir = df.columns.drop([index, 'Escuela_ID']).tolist()

#     # Agrupar por índice (por si hay varias escuelas, podrías usar groupby más adelante)
#     df.set_index(index, inplace=True)

#     # Convertir a numérico
#     for col in columnas_a_incluir:
#         df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

#     df = df[columnas_a_incluir].round(1)
    
#     # Invertir el orden de las respuestas
#     df = df[::-1]

#     fig, ax = plt.subplots(figsize=fig_size)

#     x = np.arange(len(columnas_a_incluir))  # eje x: ALGEBRA, GEOMETRÍA, NÚMEROS
#     bar_width = 0.8

#     bottom = np.zeros(len(x))

#     for resultado, color in zip(df.index, colores):
#         valores = df.loc[resultado].values
#         ax.bar(x, valores, label=resultado, color=color, width=bar_width, bottom=bottom)

#         for j, val in enumerate(valores):
#             if val > 0:
#                 ax.text(
#                     x[j], bottom[j] + val / 2, f"{val:.1f}%",
#                     ha='center', va='center', fontsize=fontsize_labels, color='white', fontweight='bold'
#                 )
#         bottom += valores

#     ax.set_xticks(x)
#     ax.set_xticklabels(columnas_a_incluir, fontsize=fontsize_labels)
#     ax.set_yticks([])
#     ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=len(df.index), fontsize=fontsize_legend)

#     plt.tight_layout()
#     return fig

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def wrap_labels(labels, width=25):
    """Agrega saltos de línea en etiquetas largas."""
    return ['\n'.join([label[i:i+width] for i in range(0, len(label), width)]) for label in labels]



def Matplotlib_bar_chart_from_df(
    df,
    colores=None,
    index_col=None,
    columnas_a_excluir=None,
    fig_size=(10, 5),
    fontsize_columnas=12,
    fontsize_valores=12,
    bar_width=0.6,
    espacio_columnas=0.2,
    value_format='percent',  # 👈 Nuevo parámetro: 'percent', 'integer', 'float'
    centrar_etiquetas=True,
    mostrar_porcentaje = False,
    
):
    """
    Genera un gráfico de barras individuales a partir de un DataFrame (de una fila),
    con valores siempre dentro de las barras.

    Args:
        df (pd.DataFrame): DataFrame con una fila.
        value_format (str): 'percent', 'integer' o 'float' para definir el formato de los valores.
    """
    if df.shape[0] != 1:
        raise ValueError("El DataFrame debe tener exactamente una fila.")

    columnas_a_excluir = columnas_a_excluir or []
    row = df.iloc[0]
    datos = row.drop(labels=columnas_a_excluir)

    etiquetas = datos.index.tolist()
    valores = pd.to_numeric(datos, errors='coerce').fillna(0).tolist()
    x = np.arange(len(etiquetas)) * (1 + espacio_columnas)

    # Colores
    if not colores or len(colores) < len(etiquetas):
        colores = plt.cm.Paired(np.arange(len(etiquetas)))

    fig, ax = plt.subplots(figsize=fig_size)

    bars = ax.bar(x, valores, width=bar_width, color=colores[:len(etiquetas)])

    # Mostrar valores dentro de las barras
    padding = max(valores) * 0.02  # Espacio dentro de la barra
    for i, bar in enumerate(bars):
        altura = bar.get_height()

        # Definir el formato del texto
        if value_format == 'percent':
            texto = f"{altura:.1f}%"
        elif value_format == 'integer':
            texto = f"{int(round(altura))}"
        elif value_format == 'float':
            texto = f"{altura:.1f}"
        else:
            raise ValueError("value_format debe ser 'percent', 'integer' o 'float'.")

        ax.text(
            bar.get_x() + bar.get_width() / 2,
            altura + padding + 1,
            texto,
            ha='center',
            va='top',
            fontsize=fontsize_valores,
            color='black'
        )

    # Etiquetas bajo las barras
    ax.set_xticks(x)
    ax.set_xticklabels(etiquetas, fontsize=fontsize_columnas)

    # Ocultar ejes y bordes
    ax.set_yticks([])
    ax.set_yticklabels([])
    ax.set_ylabel("")
    ax.set_title("")
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Definir alineación horizontal de las etiquetas según centrar_etiquetas
    ha_labels = 'center' if centrar_etiquetas else 'right'
    plt.setp(ax.get_xticklabels(), rotation=0, ha=ha_labels)

    # Ajuste de margen superior
    ax.set_ylim(0, max(valores) * 1.05)

    plt.tight_layout()
    fig.subplots_adjust(top=0.95)

    return fig


def Matplotlib_stacked_bar_chart_from_df(
    df,
    colores,
    columnas_a_incluir=None,
    index='resultado',
    fig_size=(12, 6),
    fontsize_columnas=12,
    fontsize_valores=12,
    bar_width=0.8,
    espacio_columnas=0.2,
    centrar_etiquetas=True,
    ordenar_respuestas=None  # ejemplo: ['Sin respuesta', 'Incorrecto', 'Correcto']
):
    df = df.copy()

    # Selección de columnas si no se indica explícitamente
    if columnas_a_incluir is None:
        columnas_a_incluir = df.columns.drop([index, 'Escuela_ID'], errors='ignore').tolist()

    # Asegurar tipos numéricos
    for col in columnas_a_incluir:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    # Reorganizar índice
    df.set_index(index, inplace=True)
    df = df[columnas_a_incluir].round(1)
    
    # Invertir el orden de las respuestas
    df = df[::-1]

    # Ordenar el índice si se proporciona una lista personalizada
    if ordenar_respuestas:
        df = df.loc[[r for r in ordenar_respuestas if r in df.index]]

    fig, ax = plt.subplots(figsize=fig_size)

    x = np.arange(len(columnas_a_incluir)) * (1 + espacio_columnas)  # separación horizontal
    bottom = np.zeros(len(x))  # altura inicial para apilar

    # Iterar filas para crear el gráfico apilado
    for i, (label, color) in enumerate(zip(df.index, colores)):
        valores = df.loc[label].values
        bars = ax.bar(x, valores, label=label, color=color, width=bar_width, bottom=bottom)

        for j, val in enumerate(valores):
            if val > 0:
                ax.text(
                    x[j], bottom[j] + val / 2, f"{val:.1f}%",
                    ha='center', va='center',
                    fontsize=fontsize_valores,
                    color='white', fontweight='bold'
                )
        bottom += valores

    # Etiquetas envueltas y rotadas
    etiquetas_envueltas = wrap_labels(columnas_a_incluir, width=25)
    ax.set_xticks(x)
    ax.set_xticklabels(etiquetas_envueltas, fontsize=fontsize_columnas)
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

    ax.set_yticks([])
    ax.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, -0.1),
        ncol=len(df.index),
        fontsize=fontsize_valores
    )

    # Quitar los bordes (spines) del gráfico
    for spine in ax.spines.values():
        spine.set_visible(False)

    plt.tight_layout()
    return fig

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from textwrap import fill

def wrap_labels(labels, width=25):
    """Parte etiquetas largas en varias líneas."""
    return ['\n'.join(label[i:i+width] for i in range(0, len(label), width)) for label in labels]

def Matplotlib_stacked_bar_chart_from_df_v3(
    df,
    colores: dict,  # nuevo: dict {'Etiqueta': 'Color'}
    columnas_a_incluir=None,
    index='resultado',
    fig_size=(12, 6),
    fontsize_columnas=12,
    fontsize_valores=12,
    bar_width=0.8,
    espacio_columnas=0.2,
    centrar_etiquetas=True,
    ordenar_respuestas=None,
    rotacion=45,
    debug=False
):
    df = df.copy()

    # Validar columnas seleccionadas
    if columnas_a_incluir is None:
        columnas_a_incluir = df.columns.drop([index, 'Escuela_ID'], errors='ignore').tolist()
    if debug:
        print("Columnas seleccionadas:", columnas_a_incluir)

    for col in columnas_a_incluir:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    if index not in df.columns:
        raise ValueError(f"La columna '{index}' no está en el DataFrame.")

    df.set_index(index, inplace=True)
    df = df[columnas_a_incluir].round(1)

    # Orden personalizado
    if ordenar_respuestas:
        respuestas_en_df = [r for r in ordenar_respuestas if r in df.index]
        if debug:
            print("Respuestas ordenadas presentes:", respuestas_en_df)
        df = df.reindex(respuestas_en_df)
    else:
        df = df[::-1]

    # Validar que haya datos para graficar
    if df.sum().sum() == 0:
        raise ValueError("Todos los valores son cero. No se pueden graficar barras.")

    fig, ax = plt.subplots(figsize=fig_size)

    x = np.arange(len(columnas_a_incluir)) * (1 + espacio_columnas)
    bottom = np.zeros(len(x))
    handles = []

    # Generar barras apiladas
    df = df[~df.index.isin(['no_legend', '', None])]
    for label in df.index:
        if label not in colores:
            continue  # saltar si no tiene color definido
        color = colores[label]
        valores = df.loc[label].values
        bars = ax.bar(x, valores, label=label, color=color, width=bar_width, bottom=bottom)
        handles.append(bars[0])
        for j, val in enumerate(valores):
            if val > 0:
                ax.text(
                    x[j], bottom[j] + val/2,
                    f"{val:.1f}%",
                    ha='center', va='center', fontsize=fontsize_valores,
                    color='white', fontweight='bold'
                )
        bottom += valores

    # Etiquetas del eje X
    etiquetas_envueltas = wrap_labels(columnas_a_incluir)
    ax.set_xticks(x)
    ax.set_xticklabels(etiquetas_envueltas, fontsize=fontsize_columnas)
    ha_param = 'center' if centrar_etiquetas else 'right'
    plt.setp(ax.get_xticklabels(), rotation=rotacion, ha=ha_param)

    # Limpiar bordes
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_yticks([])

    # Leyenda
    if handles:
        ax.legend(
            handles=handles,
            loc="upper center",
            bbox_to_anchor=(0.5, -0.09),
            ncol=len(handles),
            fontsize=fontsize_valores,
            title="Respuestas"
        )

    plt.tight_layout()
    return fig

def Matplotlib_stacked_bar_chart_from_df_v2(
    df,
    colores,
    columnas_a_incluir=None,
    index='resultado',
    fig_size=(12, 6),
    fontsize_columnas=12,
    fontsize_valores=12,
    bar_width=0.8,
    espacio_columnas=0.2,
    centrar_etiquetas=True,
    ordenar_respuestas=None,
    etiquetas = None,
    rotacion=45,  # rotación de etiquetas X
    debug=False  # para imprimir info de depuración
):
    df = df.copy()

    # Selección de columnas
    if columnas_a_incluir is None:
        columnas_a_incluir = df.columns.drop([index, 'Escuela_ID'], errors='ignore').tolist()
    if debug:
        print("Columnas seleccionadas:", columnas_a_incluir)

    # Asegurar datos numéricos
    for col in columnas_a_incluir:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    if index not in df.columns:
        raise ValueError(f"La columna '{index}' no está en el DataFrame.")

    # Reorganizar índice
    df.set_index(index, inplace=True)
    df = df[columnas_a_incluir].round(1)

    # Orden personalizado de respuestas
    if ordenar_respuestas:
        respuestas_en_df = [r for r in ordenar_respuestas if r in df.index]
        if debug:
            print("Respuestas ordenadas presentes:", respuestas_en_df)
        df = df.reindex(respuestas_en_df)
    else:
        df = df[::-1]

    if df.sum().sum() == 0:
        raise ValueError("Todos los valores son cero. No se pueden graficar barras.")

    fig, ax = plt.subplots(figsize=fig_size)

    x = np.arange(len(columnas_a_incluir)) * (1 + espacio_columnas)
    bottom = np.zeros(len(x))
    handles = []

    # Generar barras apiladas
    df = df[~df.index.isin(['no_legend', '', None])]
    for label, color in zip(df.index, colores):
        valores = df.loc[label].values
        bars = ax.bar(x, valores, label=label, color=color, width=bar_width, bottom=bottom)
        handles.append(bars[0])
        # Etiquetas internas de valor
        for j, val in enumerate(valores):
            if val > 0:
                ax.text(
                    x[j], bottom[j] + val/2,
                    f"{val:.1f}%",
                    ha='center', va='center', fontsize=fontsize_valores,
                    color='white', fontweight='bold'
                )
        bottom += valores

    # Etiquetas X
    etiquetas_envueltas = wrap_labels(columnas_a_incluir)
    ax.set_xticks(x)
    ax.set_xticklabels(etiquetas_envueltas, fontsize=fontsize_columnas)
    ha_param = 'center' if centrar_etiquetas else 'right'
    plt.setp(ax.get_xticklabels(), rotation=rotacion, ha=ha_param)

    # Quitar bordes y ejes Y
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_yticks([])

    # Legend
    if handles:
        ax.legend(
            handles=handles,
            loc="upper center",
            bbox_to_anchor=(0.5, -0.09),
            #bbox_to_anchor=(0.5, -0.50),  # Por encima del gráfico
            ncol=len(handles),
            fontsize=fontsize_valores
        )

    plt.tight_layout()
    return fig

def Matplotlib_stacked_bar_chart_from_df_v4(
    df,
    colores,
    columnas_a_incluir=None,
    index='resultado',
    fig_size=(12, 6),
    fontsize_columnas=12,
    fontsize_valores=12,
    bar_width=0.8,
    espacio_columnas=0.2,
    centrar_etiquetas=True,
    ordenar_respuestas=None,
    rotacion=45,  # rotación de etiquetas X
    debug=False  # para imprimir info de depuración
):
    df = df.copy()

    # Selección de columnas
    if columnas_a_incluir is None:
        columnas_a_incluir = df.columns.drop([index, 'Escuela_ID'], errors='ignore').tolist()
    if debug:
        print("Columnas seleccionadas:", columnas_a_incluir)

    # Asegurar datos numéricos
    for col in columnas_a_incluir:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    if index not in df.columns:
        raise ValueError(f"La columna '{index}' no está en el DataFrame.")

    # Reorganizar índice
    df.set_index(index, inplace=True)
    df = df[columnas_a_incluir].round(1)

    # Orden personalizado de respuestas
    if ordenar_respuestas:
        respuestas_en_df = [r for r in ordenar_respuestas if r in df.index]
        if debug:
            print("Respuestas ordenadas presentes:", respuestas_en_df)
        df = df.reindex(respuestas_en_df)
    else:
        df = df[::-1]

    if df.sum().sum() == 0:
        raise ValueError("Todos los valores son cero. No se pueden graficar barras.")

    fig, ax = plt.subplots(figsize=fig_size)

    x = np.arange(len(columnas_a_incluir)) * (1 + espacio_columnas)
    bottom = np.zeros(len(x))
    handles = []

    # Generar barras apiladas
    df = df[~df.index.isin(['no_legend', '', None])]
    for label in df.index:
        if label not in colores:
            continue  # saltar si no tiene color definido
        color = colores[label]
        valores = df.loc[label].values
        bars = ax.bar(x, valores, label=label, color=color, width=bar_width, bottom=bottom)
        handles.append(bars[0])
        for j, val in enumerate(valores):
            if val > 0:
                ax.text(
                    x[j], bottom[j] + val/2,
                    f"{val:.1f}%",
                    ha='center', va='center', fontsize=fontsize_valores,
                    color='white', fontweight='bold'
                )
        bottom += valores

    # Etiquetas X
    etiquetas_envueltas = wrap_labels(columnas_a_incluir)
    ax.set_xticks(x)
    ax.set_xticklabels(etiquetas_envueltas, fontsize=fontsize_columnas)
    ha_param = 'center' if centrar_etiquetas else 'right'
    plt.setp(ax.get_xticklabels(), rotation=rotacion, ha=ha_param)

    # Quitar bordes y ejes Y
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_yticks([])

    # Legend
    if handles:
        ax.legend(
            handles=handles,
            loc="upper center",
            bbox_to_anchor=(0.5, -0.09),
            #bbox_to_anchor=(0.5, -0.50),  # Por encima del gráfico
            ncol=len(handles),
            fontsize=fontsize_valores
        )

    plt.tight_layout()
    return fig

def Matplotlib_stacked_bar_chart_from_df_v5(
    df,
    colores,
    columnas_a_incluir=None,
    index='resultado',
    fig_size=(12, 6),
    fontsize_columnas=12,
    fontsize_valores=12,
    bar_width=0.8,
    espacio_columnas=0.2,
    centrar_etiquetas=True,
    ordenar_respuestas=None,
    etiquetas=None,
    rotacion=45,
    debug=False
):
    df = df.copy()

    if columnas_a_incluir is None:
        columnas_a_incluir = df.columns.drop([index, 'Escuela_ID'], errors='ignore').tolist()
    if debug:
        print("Columnas seleccionadas:", columnas_a_incluir)

    for col in columnas_a_incluir:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    if index not in df.columns:
        raise ValueError(f"La columna '{index}' no está en el DataFrame.")

    df.set_index(index, inplace=True)
    df = df[columnas_a_incluir].round(1)

    # Reordenar el índice según el orden deseado
    if ordenar_respuestas:
        respuestas_en_df = [r for r in ordenar_respuestas if r in df.index]
        df = df.reindex(respuestas_en_df)
    else:
        df = df[::-1]

    # Verificación
    if df.sum().sum() == 0:
        raise ValueError("Todos los valores son cero. No se pueden graficar barras.")

    fig, ax = plt.subplots(figsize=fig_size)

    x = np.arange(len(columnas_a_incluir)) * (1 + espacio_columnas)
    bottom = np.zeros(len(x))
    handles = []

    df = df[~df.index.isin(['no_legend', '', None])]

    # Aplicar etiquetas personalizadas si se proveen
    if etiquetas is not None:
        if len(etiquetas) != len(df.index):
            raise ValueError("La cantidad de etiquetas no coincide con la cantidad de categorías del índice.")
        etiquetas_legenda = etiquetas
    else:
        etiquetas_legenda = df.index.tolist()

    # Graficar barras apiladas
    for i, (label, color) in enumerate(zip(df.index, colores)):
        valores = df.loc[label].values
        bars = ax.bar(x, valores, label=etiquetas_legenda[i], color=color, width=bar_width, bottom=bottom)
        handles.append(bars[0])
        for j, val in enumerate(valores):
            if val > 0:
                ax.text(
                    x[j], bottom[j] + val/2,
                    f"{val:.1f}%",
                    ha='center', va='center', fontsize=fontsize_valores,
                    color='white', fontweight='bold'
                )
        bottom += valores

    # Etiquetas X
    etiquetas_envueltas = wrap_labels(columnas_a_incluir)
    ax.set_xticks(x)
    ax.set_xticklabels(etiquetas_envueltas, fontsize=fontsize_columnas)
    ha_param = 'center' if centrar_etiquetas else 'right'
    plt.setp(ax.get_xticklabels(), rotation=rotacion, ha=ha_param)

    # Limpiar bordes y eje Y
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_yticks([])

    # Leyenda con etiquetas personalizadas
    if handles:
        ax.legend(
            handles=handles,
            loc="upper center",
            bbox_to_anchor=(0.5, -0.09),
            ncol=len(handles),
            fontsize=fontsize_valores
        )

    plt.tight_layout()
    return fig





# def Matplotlib_stacked_bar_chart_from_df(
#     df,
#     colores,
#     columnas_a_incluir=None,
#     index='resultado',
#     fig_size=(12, 6),
#     fontsize_columnas=12,
#     fontsize_valores=12,
#     bar_width=0.8,
#     espacio_columnas=0.2,
#     centrar_etiquetas=True,
#     ordenar_respuestas=None  # ejemplo: ['Sin respuesta', 'Incorrecto', 'Correcto']
# ):
#     df = df.copy()

#     # Selección de columnas si no se indica explícitamente
#     if columnas_a_incluir is None:
#         columnas_a_incluir = df.columns.drop([index, 'Escuela_ID'], errors='ignore').tolist()

#     # Asegurar tipos numéricos
#     for col in columnas_a_incluir:
#         df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

#     # Reorganizar índice
#     df.set_index(index, inplace=True)
#     df = df[columnas_a_incluir].round(1)
    
#     # Invertir el orden de las respuestas
#     df = df[::-1]

#     # Ordenar el índice si se proporciona una lista personalizada
#     if ordenar_respuestas:
#         df = df.loc[[r for r in ordenar_respuestas if r in df.index]]

#     fig, ax = plt.subplots(figsize=fig_size)

#     x = np.arange(len(columnas_a_incluir)) * (1 + espacio_columnas)  # separación horizontal
#     bottom = np.zeros(len(x))  # altura inicial para apilar

#     # Iterar filas para crear el gráfico apilado
#     for i, (label, color) in enumerate(zip(df.index, colores)):
#         valores = df.loc[label].values
#         bars = ax.bar(x, valores, label=label, color=color, width=bar_width, bottom=bottom)

#         for j, val in enumerate(valores):
#             if val > 0:
#                 ax.text(
#                     x[j], bottom[j] + val / 2, f"{val:.1f}%",
#                     ha='center', va='center',
#                     fontsize=fontsize_valores,
#                     color='white', fontweight='bold'
#                 )
#         bottom += valores

#     # Configuración de ejes
#     ax.set_xticks(x)
#     ax.set_xticklabels(columnas_a_incluir, fontsize=fontsize_columnas)

#     if centrar_etiquetas:
#         for label in ax.get_xticklabels():
#             label.set_ha('center')

#     ax.set_yticks([])
#     ax.legend(
#         loc="upper center",
#         bbox_to_anchor=(0.5, -0.1),
#         ncol=len(df.index),
#         fontsize=fontsize_valores
#     )

#     plt.tight_layout()
#     return fig



import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.colors as mcolors

def get_contrasting_text_color(hex_color):
    """
    Devuelve 'black' o 'white' según el contraste del color recibido (hexadecimal).
    """
    rgb = mcolors.hex2color(hex_color)
    luminancia = 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]
    return 'black' if luminancia > 0.6 else 'white'

def Matplotlib_bar_chart_from_df_v6(
    df,
    index='resultado',
    colores=None,
    columnas_a_incluir=None,
    fig_size=(12, 6),
    bar_width=0.5,
    espacio_columnas=5,
    centrar_etiquetas=True,
    fontsize_columnas=10,
    fontsize_valores=9,
    title=None,
    ylabel=None,
    legend_labels=None,
    rotacion=45,
    invert_resultados=False,
    legend_loc='upper center',
    legend_outside=False,
    legend_fontsize=20,
    legend_bold=True  # 👈 Nuevo parámetro
):
    df = df.copy()

    # Invertir el orden de las filas
    if invert_resultados:
        df = df[::-1]

    if index not in df.columns:
        raise ValueError(f"La columna '{index}' no se encuentra en el DataFrame.")

    # Mover columna índice a índice real
    df.set_index(index, inplace=True)

    # Filtrar columnas
    if columnas_a_incluir is not None:
        df = df[columnas_a_incluir]
    else:
        df = df.select_dtypes(include='number')

    df.columns = [col.replace(' - ', '\n') for col in df.columns]

    etiquetas = df.columns.tolist()
    categorias = df.index.tolist()

    if colores is None:
        colores = plt.cm.tab10.colors[:len(categorias)]

    x = np.arange(len(etiquetas)) * espacio_columnas
    bottom = np.zeros(len(etiquetas), dtype=float)

    fig, ax = plt.subplots(figsize=fig_size)

    for i, categoria in enumerate(categorias):
        valores = df.loc[categoria].astype(float).values
        color_categoria = colores[i]
        bars = ax.bar(
            x,
            valores,
            bottom=bottom,
            label=legend_labels[i] if legend_labels else categoria,
            color=color_categoria,
            width=bar_width,
        )

        # Etiquetas dentro de las barras
        hex_color = mcolors.to_hex(color_categoria)
        text_color = get_contrasting_text_color(hex_color)

        for j, val in enumerate(valores):
            if val > 0:
                ax.text(
                    x[j],
                    bottom[j] + val / 2,
                    f"{val:.1f}%",
                    ha='center',
                    va='center',
                    fontsize=fontsize_valores,
                    color=text_color,
                    fontweight='bold'
                )

        bottom += valores

    # Ajustar etiquetas del eje X
    if centrar_etiquetas:
        ax.set_xticks(x)
    else:
        ax.set_xticks(x + bar_width / 2)

    #ax.set_xticklabels(etiquetas, fontsize=fontsize_columnas, rotation=rotacion)
    ax.set_xticklabels(etiquetas, fontsize=fontsize_columnas, rotation=rotacion, fontweight='bold')
    ha_param = 'center' if centrar_etiquetas else 'right'
    plt.setp(ax.get_xticklabels(), ha=ha_param)

    # Estética
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_yticks([])

    if ylabel:
        ax.set_ylabel(ylabel)
    if title:
        ax.set_title(title)

    # Leyenda
    if legend_loc is not None:
        from matplotlib.font_manager import FontProperties
        #font_prop = FontProperties(weight='bold') if legend_bold else FontProperties(weight='normal')
        font_prop = FontProperties(family='Arial', weight='bold') if legend_bold else FontProperties(family='Arial', weight='normal')

        if legend_outside:
            ax.legend(
                loc=legend_loc,
                bbox_to_anchor=(0.5, 1.0),
                ncol=len(categorias),
                fontsize=legend_fontsize,
                prop=font_prop
            )
            fig.subplots_adjust(bottom=0.25)
        else:
            ax.legend(
                loc=legend_loc,
                fontsize=legend_fontsize,
                prop=font_prop
            )

    fig.tight_layout()

    return fig

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

def get_contrasting_text_color(hex_color):
    r, g, b = mcolors.to_rgb(hex_color)  # valores entre 0 y 1
    # Convertir a escala 0–255
    r *= 255
    g *= 255
    b *= 255
    # Fórmula de luminosidad perceptiva
    brightness = r * 0.299 + g * 0.587 + b * 0.114
    # Umbral más claro (ej: 186)
    return 'black' if brightness > 186 else 'white'

def Matplotlib_bar_chart_from_df_con_colores(
    df,
    dict_resultado_colores,
    index='resultado',
    columnas_a_incluir=None,
    fig_size=(12, 6),
    bar_width=0.5,
    espacio_columnas=5,
    centrar_etiquetas=True,
    fontsize_columnas=10,
    fontsize_valores=9,
    title=None,
    ylabel=None,
    legend_loc='upper center',
    legend_outside=False,
    legend_fontsize=20,
    legend_bold=True,
    rotacion=45,
    invert_resultados=False
):
    df = df.copy()

    if invert_resultados:
        df = df[::-1]

    if index not in df.columns:
        raise ValueError(f"La columna '{index}' no se encuentra en el DataFrame.")

    df.set_index(index, inplace=True)

    if columnas_a_incluir is not None:
        df = df[columnas_a_incluir]
    else:
        df = df.select_dtypes(include='number')

    df.columns = [col.replace(' - ', '\n') for col in df.columns]

    etiquetas = df.columns.tolist()
    categorias = df.index.tolist()

    # Asignar colores según el diccionario
    colores = [dict_resultado_colores.get(cat, '#CCCCCC') for cat in categorias]

    x = np.arange(len(etiquetas)) * espacio_columnas
    bottom = np.zeros(len(etiquetas), dtype=float)

    fig, ax = plt.subplots(figsize=fig_size)

    for i, (categoria, color) in enumerate(zip(categorias, colores)):
        valores = df.loc[categoria].astype(float).values
        bars = ax.bar(
            x,
            valores,
            bottom=bottom,
            label=categoria,
            color=color,
            width=bar_width,
        )

        hex_color = mcolors.to_hex(color)
        text_color = get_contrasting_text_color(hex_color)

        for j, val in enumerate(valores):
            if val > 0:
                ax.text(
                    x[j],
                    bottom[j] + val / 2,
                    f"{val:.1f}%",
                    ha='center',
                    va='center',
                    fontsize=fontsize_valores,
                    color=text_color,
                    fontweight='bold'
                )

        bottom += valores

    # Etiquetas eje X
    if centrar_etiquetas:
        ax.set_xticks(x)
    else:
        ax.set_xticks(x + bar_width / 2)

    ax.set_xticklabels(etiquetas, fontsize=fontsize_columnas, rotation=rotacion, fontweight='bold')
    ha_param = 'center' if centrar_etiquetas else 'right'
    plt.setp(ax.get_xticklabels(), ha=ha_param)

    # Estética
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_yticks([])

    if ylabel:
        ax.set_ylabel(ylabel)
    if title:
        ax.set_title(title)

    # Leyenda
    if legend_loc is not None:
        from matplotlib.font_manager import FontProperties
        font_prop = FontProperties(family='Arial', weight='bold' if legend_bold else 'normal')

        if legend_outside:
            ax.legend(
                loc=legend_loc,
                bbox_to_anchor=(0.5, 1.0),
                ncol=len(categorias),
                fontsize=legend_fontsize,
                prop=font_prop
            )
            fig.subplots_adjust(bottom=0.25)
        else:
            ax.legend(
                loc=legend_loc,
                fontsize=legend_fontsize,
                prop=font_prop
            )

    fig.tight_layout()
    return fig

def Matplotlib_bar_chart_from_df_con_colores_v2(
    df,
    dict_resultado_colores,
    index='resultado',
    columnas_a_incluir=None,
    fig_size=(12, 6),
    bar_width=0.5,  # se mantiene para compatibilidad
    bar_thickness=0.8,  # <--- NUEVO PARÁMETRO
    espacio_columnas=5,
    centrar_etiquetas=True,
    fontsize_columnas=10,
    fontsize_valores=9,
    title=None,
    ylabel=None,
    legend_loc='upper center',
    legend_outside=False,
    legend_fontsize=20,
    legend_bold=True,
    rotacion=45,
    invert_resultados=False,
    horizontal=False,
    usar_porcentajes=True
):
    df = df.copy()

    if invert_resultados:
        df = df[::-1]

    if index not in df.columns:
        raise ValueError(f"La columna '{index}' no se encuentra en el DataFrame.")

    df.set_index(index, inplace=True)

    if columnas_a_incluir is not None:
        df = df[columnas_a_incluir]
    else:
        df = df.select_dtypes(include='number')

    df.columns = [col.replace(' - ', '\n') for col in df.columns]

    etiquetas = df.columns.tolist()
    categorias = df.index.tolist()

    colores = [dict_resultado_colores.get(cat, '#CCCCCC') for cat in categorias]

    x = np.arange(len(etiquetas)) * espacio_columnas
    bottom = np.zeros(len(etiquetas), dtype=float)

    # ⚠️ Auto-ajustar fig_size si horizontal y pocas columnas
    if horizontal and len(etiquetas) <= 2 and fig_size == (12, 6):
        fig_size = (10, 1.2)

    fig, ax = plt.subplots(figsize=fig_size, constrained_layout=True)

    for i, (categoria, color) in enumerate(zip(categorias, colores)):
        valores = df.loc[categoria].astype(float).values

        if usar_porcentajes:
            total_por_columna = df.sum()
            valores = (valores / total_por_columna.values) * 100

        hex_color = mcolors.to_hex(color)
        text_color = get_contrasting_text_color(hex_color)

        if horizontal:
            bars = ax.barh(
                x,
                valores,
                left=bottom,
                label=categoria,
                color=color,
                height=bar_thickness
            )
            for j, val in enumerate(valores):
                if val > 0:
                    ax.text(
                        bottom[j] + val / 2,
                        x[j],
                        f"{val:.1f}%" if usar_porcentajes else f"{int(val)}",
                        va='center',
                        ha='center',
                        fontsize=fontsize_valores,
                        color=text_color,
                        fontweight='bold'
                    )
        else:
            bars = ax.bar(
                x,
                valores,
                bottom=bottom,
                label=categoria,
                color=color,
                width=bar_thickness
            )
            for j, val in enumerate(valores):
                if val > 0:
                    ax.text(
                        x[j],
                        bottom[j] + val / 2,
                        f"{val:.1f}%" if usar_porcentajes else f"{int(val)}",
                        ha='center',
                        va='center',
                        fontsize=fontsize_valores,
                        color=text_color,
                        fontweight='bold'
                    )

        bottom += valores

    if centrar_etiquetas:
        if horizontal:
            ax.set_yticks(x)
        else:
            ax.set_xticks(x)
    else:
        if horizontal:
            ax.set_yticks(x + bar_thickness / 2)
        else:
            ax.set_xticks(x + bar_thickness / 2)

    if horizontal:
        ax.set_yticklabels(etiquetas, fontsize=fontsize_columnas, fontweight='bold')
        ax.set_xticks([])
    else:
        ax.set_xticklabels(etiquetas, fontsize=fontsize_columnas, rotation=rotacion, fontweight='bold')

    for spine in ax.spines.values():
        spine.set_visible(False)

    if horizontal:
        ax.set_xlabel(ylabel)
    else:
        ax.set_ylabel(ylabel)

    if title:
        ax.set_title(title)

    if legend_loc is not None:
        from matplotlib.font_manager import FontProperties
        font_prop = FontProperties(family='Arial', weight='bold' if legend_bold else 'normal')

        if legend_outside:
            ax.legend(
                loc=legend_loc,
                bbox_to_anchor=(0.5, 1.0),
                ncol=len(categorias),
                fontsize=legend_fontsize,
                prop=font_prop
            )
        else:
            ax.legend(
                loc=legend_loc,
                fontsize=legend_fontsize,
                prop=font_prop
            )

    return fig


def dibujar_barra_apilada_horizontal_(datos, colores, titulo='Comparación de Niveles'):
    """
    Crea una figura de barra apilada horizontal con los datos y colores proporcionados.

    :param datos: Diccionario con claves de categoría y valores numéricos.
    :param colores: Diccionario con los mismos nombres de categoría como claves y colores hex como valores.
    :param titulo: Título del gráfico.
    :return: Objeto matplotlib.figure.Figure
    """
    categorias = datos['compara']
    valores = datos['.']

    y_pos = [0]
    izquierda = 0

    fig, ax = plt.subplots(figsize=(8, 8))  # Tamaño del gráfico
    # fig.patch.set_facecolor('#f5f5f5')  # Fondo de toda la figura
    # ax.set_facecolor('#e0e0e0')         # Fondo del área del gráfico

    for categoria, valor in zip(categorias, valores):
        ax.barh(y_pos, [valor], left=izquierda, color=colores.get(categoria, '#999999'), label=categoria,height=0.3)
        # Texto centrado en el medio del segmento
        ax.text(izquierda + valor / 2, 0, str(valor), va='center', ha='center', fontsize=40, color='white')
        izquierda += valor
        
    # eliminar los bordes del gráfico
    # Eliminar bordes y ejes
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    
    # Ajustar márgenes
    plt.subplots_adjust(left=0.01, right=0.99, top=0.8, bottom=0.3)
    
    ax.set_yticks([])
    ax.set_xticks([])
    ax.set_xlim(0, sum(valores))
    ax.set_ylim(-0.5, 0.5)  # Control de altura vertical fina
    ax.axis('on')  # quita ticks, spines y ejes
    
    # Limpiar todo lo visual
    ax.axis('on')
    ax.set_xlim(0, sum(valores))
    ax.set_ylim(-0.6, 0.6)

    # Eliminar márgenes internos
    #plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    #plt.subplots_adjust()

    
    
    #ax.set_ylim(-0.2, len(y_pos) - 0.8)  # Ajusta los límites verticales si solo hay 1 barra
    ax.set_title(titulo)
    # Leyenda centrada abajo
    ax.legend(
        loc='lower center',
        bbox_to_anchor=(0.5, -0.5),  # centrado horizontal, hacia abajo
        ncol=len(categorias),        # tantas columnas como categorías
        frameon=False,                # sin recuadro
        fontsize=20
    )
    
    
    
    
    plt.tight_layout()
    
    # Eliminar márgenes blancos
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

    return fig

def dibujar_barra_apilada_horizontal(datos, colores, titulo='Comparación de Niveles'):
    """
    Crea una figura de barra apilada horizontal con los datos y colores proporcionados.
    """

    categorias = datos['compara']
    valores = datos['.']

    fig, ax = plt.subplots(figsize=(8, 8)) 
    #fig.patch.set_facecolor('#f5f5f5')  # Fondo de toda la figura
    #ax.set_facecolor('#e0e0e0')         # Fondo del área del gráfico
     

    izquierda = 0
    for categoria, valor in zip(categorias, valores):
        ax.barh(
            y=0,
            width=valor,
            left=izquierda,
            height=0.2,
            color=colores.get(categoria, '#999999'),
            label=categoria,
        )
        ax.text(
            izquierda + valor / 2,
            0,
            str(valor),
            va='center',
            ha='center',
            fontsize=40,
            color='white'
        )
        izquierda += valor

    # Mostrar el eje X (escala horizontal)
    ax.set_xlim(0, sum(valores))
    ax.set_ylim(-0.1, 0.5)  # Control de altura vertical fina
    ax.set_xticks(range(0, sum(valores)+1, max(1, sum(valores)//5)))
    ax.tick_params(axis='x', labelsize=20)

    # Quitar eje Y
    ax.set_yticks([])

    # Eliminar bordes del gráfico
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Título
    ax.set_title(titulo, fontsize=14, pad=20)

    # Centrar leyenda debajo
    ax.legend(
        loc='upper center',
        bbox_to_anchor=(0.5, -0.1),
        ncol=len(categorias),
        frameon=False,
        fontsize=18
    )

    # Ajustes de layout
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.3)

    return fig






if __name__ == '__main__':
    
    # Supongamos que este es tu DataFrame:
    df = pd.DataFrame({
        "resultado": ["Correcto", "Incorrecto", "Sin respuesta"],
        "ALGEBRA Y FUNCIONES": [58.46, 38.8, 2.73],
        "GEOMETRÍA Y MEDIDA": [41.98, 54.4, 3.62],
        "NÚMEROS Y OPERACIONES": [61.82, 37.03, 1.15]
    })

    Matplotlib_bar_chart_from_df_v6(
        df=df,
        index='resultado',
        colores=['#5E227D', '#A361DA', '#CCC1DA'],
        columnas_a_incluir=None,
        title='Distribución por eje cognitivo',
        legend_labels=['Correcto', 'Incorrecto', 'Sin respuesta'],
        rotacion=45,
        invert_resultados=True,
        legend_loc='lower center', # 'best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'
        legend_outside=True
    )
    
    plt.show()   
    
    
#### NO BORRAR ####
# # # # # Ejemplo de gráfico de barras apiladas con matplotlib
# # # # import matplotlib.pyplot as plt
# # # # import numpy as np

# # # # # Categorías del eje X
# # # # etiquetas = ['Grupo A', 'Grupo B', 'Grupo C', 'Grupo D']

# # # # # Datos para cada subcategoría
# # # # categoria1 = [5, 7, 3, 4]
# # # # categoria2 = [2, 6, 4, 5]
# # # # categoria3 = [3, 2, 5, 2]

# # # # # Posiciones en el eje X
# # # # x = np.arange(len(etiquetas))

# # # # # Crear gráfico de barras apiladas
# # # # plt.bar(x, categoria1, label='Categoría 1')
# # # # plt.bar(x, categoria2, bottom=categoria1, label='Categoría 2')
# # # # plt.bar(x, categoria3, bottom=np.array(categoria1) + np.array(categoria2), label='Categoría 3')

# # # # # Etiquetas y leyenda
# # # # plt.xticks(x, etiquetas)
# # # # plt.ylabel('Valores')
# # # # plt.title('Ejemplo de gráfico de barras apiladas')
# # # # plt.legend()

# # # # # Mostrar gráfico
# # # # plt.tight_layout()
# # # # plt.show()
