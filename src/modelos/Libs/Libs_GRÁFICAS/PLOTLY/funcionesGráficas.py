# https://stackoverflow.com/questions/61453796/better-way-to-plot-a-dataframe-on-a-plotly-table
# https://www.geeksforgeeks.org/how-to-create-tables-using-plotly-in-python/
# https://www.codespeedy.com/how-to-change-figure-size-in-plotly-in-python/
# https://stackoverflow.com/questions/63366363/plotly-how-to-remove-white-space-after-saving-an-image


# crear imagenes desde varios data frames
# Removed unused import: plotly.graph_objects as go
import numpy as np
import pandas as pd
import plotly.express as px  # Correct import for plotly.express
#import configfile as cf
#from tabulate import tabulatepip
import matplotlib.pyplot as plt 



def dibujarDiagramaDeBarras_(dataFrame ,  nombreArchivo):
    dataFrame = dataFrame.transpose()
    dataFrame = dataFrame.round(1)
    
    ax = dataFrame.plot(kind='bar', 
                        stacked=True,
                        title='Stacked Bar Graph by dataframe'
                        )
    plt.xticks(rotation = 0)
    ax.tick_params(which='minor', width=0.75, length=2.5, labelsize=10)
    
    
    for bar in ax.patches:
        height = bar.get_height()
        width = bar.get_width()
        x = bar.get_x()
        y = bar.get_y()
        
        label_text = height
        label_x = x + width / 2
        label_y = y + height / 2
        
        y_offset = -15
        
        ax.text(
                bar.get_x() + bar.get_width(),
                 round(bar.get_height()) ,
                #label_x, 
                #label_y, 
                #label_text, 
                ha='center',    
                #va='center',
                color='b',
                weight='normal',
                size=8
                )
    """
   
    for bar in ax.patches:
        ax.text(
            # Put the text in the middle of each bar. get_x returns the start
            # so we add half the width to get to the middle.
            bar.get_x() + bar.get_width() / 2,
            # Vertically, add the height of the bar to the start of the bar,
            # along with the offset.
            bar.get_height() + bar.get_y() + y_offset,
            # This is actual value we'll show.
            round(bar.get_height()),
            # Center the labels and style them a bit.
            ha='center',
            color='w',
            weight='bold',
            size=8
        )    
    """
        
    
    plt.savefig(nombreArchivo)
    
    """
    plot = dataFrame.plot.bar(stacked=True)
    fig = plot.get_figure()
    fig.savefig(nombreArchivo)
    """
    return 
    

# controlar
# https://www.google.com/search?q=python+plotly+xaxis+text+centered&oq=python+plotly+xaxis+text+cen&aqs=chrome.3.69i57j33i160l4.34087j0j7&sourceid=chrome&ie=UTF-8
# https://community.plotly.com/t/x-y-axis-label-alignment/36949/2
# https://plotly.com/python-api-reference/generated/plotly.graph_objects.Bar.html#plotly.graph_objects.Bar

def FL_ESCUELA_007_desempeño_por_curso_supervisión_y_nivel(dataFrame , colores ,  nombreArchivo):
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
                 width=900, height=850
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
                      textfont_size = 35 , # 45 , # 25 , # 78 ,
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

    fig.update_layout(  legend       = dict(font = dict(family = "Calibri", size = 30, color = "black")),
                        legend_title = dict(font = dict(family = "Calibri", size = 30, color = "black")))

    fig.update_layout(xaxis = dict(
                      tickfont = dict(size=19)) # para regular el tamaño de las letras debajo de las barras ) 
                     )
    
    fig.update_traces(width  = 0.75)

    fig.write_image(nombreArchivo)
    return

def FL_SUPERVISIÓN_007_desempeño_crítico_por_escuela(dataFrame , colores ,  nombreArchivo):
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
                 width=900+200, height=850+200
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
                      textfont_size = 35 , # 45 , # 25 , # 78 ,
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

    fig.update_layout(  legend       = dict(font = dict(family = "Calibri", size = 30, color = "black")),
                        legend_title = dict(font = dict(family = "Calibri", size = 30, color = "black")))

    fig.update_layout(xaxis = dict(
                      tickfont = dict(size=10)) # para regular el tamaño de las letras debajo de las barras ) 
                     )
    
    fig.update_traces(width  = 0.55)

    fig.write_image(nombreArchivo)
    return

def FL_ESCUELA_010_comparativa_según_progreso(dataFrame , colores ,  nombreArchivo):
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
                 width=900, height=850 ,
                 orientation='h'
                 )
    fig.update_layout(#xaxis_title = 'Nivel de Fluidez' + ' - ' + tipoDesempeñoOProsodia + ' - ',     
                      xaxis_title = ' ',     
                      # yaxis_tickformat = "%f" , 
                      legend = dict(orientation = "h" , 
                                    yanchor = "top" , 
                                    #xanchor="left",                                    
                                    xanchor = 'center',
                                    y = -0.15,
                                    x = 0.5),
                      yaxis = {'visible' : True, 'showticklabels' : True},
                      legend_title_text = '' 
                     )
    fig.update_traces(textposition = 'auto' , 
                      textfont_size = 35 , # 45 , # 25 , # 78 ,
                      #textangle=90,
                      #textfont_color  = 'White',
                      textfont_family = 'Calibri',                      
                      #texttemplate = "%{value:} %",
                      textangle = 0,
                      cliponaxis = False
                      )
    fig.update_layout(bargap=0.30)
    #fig.update_traces(width = 0.4)
    fig.update_traces(textangle=0)
    fig.update_xaxes(tickangle=0)
    fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
    fig.update_layout({ 'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})

    fig.update_layout(  legend       = dict(font = dict(family = "Calibri", size = 30, color = "black")),
                        legend_title = dict(font = dict(family = "Calibri", size = 30, color = "black")))

    fig.update_layout(xaxis = dict(
                      tickfont = dict(size=40)) # para regular el tamaño de las letras debajo de las barras ) 
                     )
    
    fig.update_traces(width  = 0.10)

    fig.update_layout(
        yaxis = dict(
        tickfont = dict(size=50))) # para cambiar el tamaño de la letra de la izquierda
    
    fig.update_yaxes(
        showgrid=False,  # Ocultar las líneas de la cuadrícula horizontales
        tickfont=dict(size=50)
    )
    

    fig.write_image(nombreArchivo)
    return

def FL_ESCUELA_010_comparativa_según_progreso____(dataFrame, colores, nombreArchivo):
    # Transponer el dataframe y redondear los valores
    dataFrame = dataFrame.transpose()
    dataFrame = dataFrame.round(1)
    
    # Crear el gráfico de barras horizontales
    fig = px.bar(dataFrame,    
                 barmode='stack', 
                 text_auto='5.92f',                 
                 color_discrete_sequence=colores,
                 title='',
                 width=900, height=850,
                 orientation='h'
                 )
    
    # Configurar el layout del gráfico
    fig.update_layout(
        xaxis_title=' ',
        yaxis={'visible': True, 'showticklabels': True},
        legend=dict(
            orientation="h",
            yanchor="top",
            xanchor='center',
            y=-0.15,
            x=0.5,
            font=dict(family="Calibri", size=30, color="black"),
            title=dict(font=dict(family="Calibri", size=30, color="black"))
        ),
        bargap=0.30,
        barmode='stack',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
    )
    
    # Configurar los ejes
    fig.update_xaxes(
        categoryorder='total descending',
        showgrid=False,  # Ocultar las líneas de la cuadrícula verticales
        tickfont=dict(size=40)
    )
    
    fig.update_yaxes(
        showgrid=False,  # Ocultar las líneas de la cuadrícula horizontales
        tickfont=dict(size=50)
    )
    
    # Configurar las trazas del gráfico
    fig.update_traces(
        textposition='auto',
        textfont_size=35,
        textfont_family='Calibri',
        textangle=0,
        cliponaxis=False,
        width=0.10
    )

    # Guardar la imagen
    fig.write_image(nombreArchivo)

    return

def FL_SUPERVISIÓN_003_comparativa_entre_primera_y_segunda_medición(dataFrame , colores ,  nombreArchivo):
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
                 width=900, height=850 ,
                 orientation='h'
                 )
    fig.update_layout(#xaxis_title = 'Nivel de Fluidez' + ' - ' + tipoDesempeñoOProsodia + ' - ',     
                      xaxis_title = ' ',     
                      # yaxis_tickformat = "%f" , 
                      legend = dict(orientation = "h" , 
                                    yanchor = "top" , 
                                    #xanchor="left",                                    
                                    xanchor = 'center',
                                    y = -0.15,
                                    x = 0.5),
                      yaxis = {'visible' : True, 'showticklabels' : True},
                      legend_title_text = '' 
                     )
    fig.update_traces(textposition = 'auto' , 
                      textfont_size = 35 , # 45 , # 25 , # 78 ,
                      #textangle=90,
                      #textfont_color  = 'White',
                      textfont_family = 'Calibri',                      
                      #texttemplate = "%{value:} %",
                      textangle = 0,
                      cliponaxis = False
                      )
    fig.update_layout(bargap=0.30)
    #fig.update_traces(width = 0.4)
    fig.update_traces(textangle=0)
    fig.update_xaxes(tickangle=0)
    fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
    fig.update_layout({ 'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})

    fig.update_layout(  legend       = dict(font = dict(family = "Calibri", size = 30, color = "black")),
                        legend_title = dict(font = dict(family = "Calibri", size = 30, color = "black")))

    fig.update_layout(xaxis = dict(
                      tickfont = dict(size=20)) # para regular el tamaño de las letras debajo de las barras ) 
                     )
    
    fig.update_traces(width  = 0.10)

    fig.update_layout(
        yaxis = dict(
        tickfont = dict(size=50))) # para cambiar el tamaño de la letra de la izquierda
    

    fig.write_image(nombreArchivo)
    return

def dibujarDiagramaDeBarras(dataFrame , colores ,  nombreArchivo):
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
                 width=900, height=850
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
                      textfont_size = 35 , # 45 , # 25 , # 78 ,
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

    fig.update_layout(  legend       = dict(font = dict(family = "Calibri", size = 30, color = "black")),
                        legend_title = dict(font = dict(family = "Calibri", size = 30, color = "black")))

    fig.update_layout(xaxis = dict(
                      tickfont = dict(size=25)) # para regular el tamaño de las letras debajo de las barras ) 
                     )
    
    fig.update_traces(width  = 0.75)

    fig.write_image(nombreArchivo)
    return

def dibujarDiagramaDeBarras_EscuelasDeLaSupervsion(dataFrame , colores ,  nombreArchivo):
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
                 width=1900, height=1850
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
                      textfont_size = 40 , # 80 , # 25, # 78
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

    fig.update_layout(  legend       = dict(font = dict(family = "Calibri", size = 30, color = "black")),
                        legend_title = dict(font = dict(family = "Calibri", size = 30, color = "black")))

    fig.update_traces(width  = 0.95) # ancho de las barras 
    fig.update_layout(bargap = 0.9) # agujero entre las barras NO FUNCIONA
    
    fig.update_layout(xaxis = dict(
                      tickfont = dict(size=30)) # para regular el tamaño de las letras debajo de las barras ) 
                     )
    

    fig.write_image(nombreArchivo)
    return

def dibujarDiagramaDeBarras_EscuelasDeLaSupervsion_2024(dataFrame , colores ,  nombreArchivo):
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
    

    fig.write_image(nombreArchivo)
    return

# para cada una de las escuelas que tienen presentismo
def dibujarDiagramaDeBarras_Presentismo_para_cada_escuela(dataFrame , colores ,  nombreArchivo):
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
                 width=900, height=850
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
                      textfont_size = 25 , # 45 , # 25 , # 78 ,
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

    fig.update_layout(  legend       = dict(font = dict(family = "Calibri", size = 30, color = "black")),
                        legend_title = dict(font = dict(family = "Calibri", size = 30, color = "black")))

    fig.update_layout(xaxis = dict(
                      tickfont = dict(size=20)) # para regular el tamaño de las letras debajo de las barras ) 
                     )
    
    fig.update_traces(width  = 0.55)

    fig.write_image(nombreArchivo)
    return

# para aprender
def dibujarDiagramaDeBarras_Para_los_Aprender(dataFrame , colores ,  nombreArchivo):
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
                 width=900, height=850
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
                      textfont_size = 25 , # 45 , # 25 , # 78 ,
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

    fig.update_layout(  legend       = dict(font = dict(family = "Calibri", size = 25, color = "black")),
                        legend_title = dict(font = dict(family = "Calibri", size = 25, color = "black")))

    fig.update_layout(xaxis = dict(
                      tickfont = dict(size=20)) # para regular el tamaño de las letras debajo de las barras ) 
                     )
    
    fig.update_traces(width  = 0.55)

    fig.write_image(nombreArchivo)
    return


# para aprender leyenda vertical
def dibujarDiagramaDeBarras_Para_los_Aprender_leyenda_vertical(dataFrame , colores ,  nombreArchivo):
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
                 width=900, height=850
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
                      textfont_size = 25 , # 45 , # 25 , # 78 ,
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

    fig.update_layout(  legend       = dict(font = dict(family = "Calibri", size = 15, color = "black")),
                        legend_title = dict(font = dict(family = "Calibri", size = 15, color = "black")))

    fig.update_layout(xaxis = dict(
                      tickfont = dict(size=13))
                      
                     )
    
    fig.update_traces(width  = 0.95 ) # textangle= 90 rota el texto dentro de la barra
    fig.update_xaxes(tickangle=45)

    fig.write_image(nombreArchivo)
    return

def dibujarDiagramaDeBarras_Para_Fluidez_Lectora_por_depto_leyenda_vertical(dataFrame , colores ,  nombreArchivo):
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
                 width=900, height=850
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
                      textfont_size = 25 , # 45 , # 25 , # 78 ,
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

    fig.update_layout(  legend       = dict(font = dict(family = "Calibri", size = 15, color = "black")),
                        legend_title = dict(font = dict(family = "Calibri", size = 15, color = "black")))

    fig.update_layout(xaxis = dict(
                      tickfont = dict(size=13))
                      
                     )
    
    fig.update_traces(width  = 0.95 ) # textangle= 90 rota el texto dentro de la barra
    fig.update_xaxes(tickangle=45)

    fig.write_image(nombreArchivo)
    return

def dibujarDiagramaDeBarrasFluidezPorDEPARTAMENTO_IVE(dataFrame , colores ,  nombreArchivo):
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
    #dataFrame = dataFrame.transpose()
    dataFrame = dataFrame.round(1)
    
    fig = px.bar(dataFrame ,    
                 barmode = 'stack' , 
                 text_auto = '5.92f' ,                 
                 color_discrete_sequence = colores, # ["#8A68A6", "#F1D447", "#A1C16D", "#0594A4"]
                 title = '',
                 width=900, height=850 ,
                 orientation='h'
                 )
    fig.update_layout(#xaxis_title = 'Nivel de Fluidez' + ' - ' + tipoDesempeñoOProsodia + ' - ',     
                      xaxis_title = ' ',     
                      # yaxis_tickformat = "%f" , 
                      legend = dict(orientation = "h" , 
                                    yanchor = "top" , 
                                    #xanchor="left",                                    
                                    xanchor = 'center',
                                    y = -0.15,
                                    x = 0.5),
                      yaxis = {'visible' : True, 'showticklabels' : True},
                      legend_title_text = '' 
                     )
    fig.update_traces(textposition = 'auto' , 
                      textfont_size = 35 , # 45 , # 25 , # 78 ,
                      #textangle=90,
                      #textfont_color  = 'White',
                      textfont_family = 'Calibri',                      
                      #texttemplate = "%{value:} %",
                      textangle = 0,
                      cliponaxis = False
                      )
    fig.update_layout(bargap=0.30)
    #fig.update_traces(width = 0.4)
    fig.update_traces(textangle=0)
    fig.update_xaxes(tickangle=0)
    fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
    fig.update_layout({ 'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})

    fig.update_layout(  legend       = dict(font = dict(family = "Calibri", size = 30, color = "black")),
                        legend_title = dict(font = dict(family = "Calibri", size = 30, color = "black")))

    fig.update_layout(xaxis = dict(
                      tickfont = dict(size = 1)) # para regular el tamaño de las letras debajo de las barras ) 
                     )
    
    fig.update_traces(width  = 0.10)

    fig.update_layout(
        yaxis = dict(
        tickfont = dict(size = 1))) # para cambiar el tamaño de la letra de la izquierda
    

    fig.write_image(nombreArchivo)
    return

def dibujarDiagramaDeBarrasFluidezPorDEPARTAMENTO_IVE_vertical(dataFrame , colores ,  nombreArchivo):
    """
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
                 barmode = 'stack' ,  # ['stack', 'group', 'overlay', 'relative']
                 text_auto = '5.92f' ,                 
                 color = colores, # ["#8A68A6", "#F1D447", "#A1C16D", "#0594A4"]
                 title = '',
                 width=900, height=850 ,
                 orientation='v'
                 )
    fig.update_layout(#xaxis_title = 'Nivel de Fluidez' + ' - ' + tipoDesempeñoOProsodia + ' - ',     
                      xaxis_title = ' ',     
                      # yaxis_tickformat = "%f" , 
                      legend = dict(orientation = "v" , 
                                    yanchor = "top" , 
                                    #xanchor="left",                                    
                                    xanchor = 'center',
                                    y = -0.15,
                                    x = 0.5),
                      yaxis = {'visible' : True, 'showticklabels' : True},
                      legend_title_text = '' 
                     )
    fig.update_traces(textposition = 'auto' , 
                      textfont_size = 35 , # 45 , # 25 , # 78 ,
                      #textangle=90,
                      #textfont_color  = 'White',
                      textfont_family = 'Calibri',                      
                      #texttemplate = "%{value:} %",
                      textangle = 0,
                      cliponaxis = False
                      )
    fig.update_layout(bargap=0.30)
    #fig.update_traces(width = 0.4)
    fig.update_traces(textangle=0)
    fig.update_xaxes(tickangle=0)
    #fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
    fig.update_layout({ 'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})

    fig.update_layout(  legend       = dict(font = dict(family = "Calibri", size = 30, color = "black")),
                        legend_title = dict(font = dict(family = "Calibri", size = 30, color = "black")))

    fig.update_layout(xaxis = dict(
                      tickfont = dict(size = 1)) # para regular el tamaño de las letras debajo de las barras ) 
                     )
    
    fig.update_traces(width  = 0.50)

    fig.update_layout(
        yaxis = dict(
        tickfont = dict(size = 30))) # para cambiar el tamaño de la letra de la izquierda
    

    fig.write_image(nombreArchivo)
    """
    dataFrame = dataFrame.transpose()
    fig = px.bar(dataFrame ,                
                 text_auto = '5.92f' ,
                 color = ['IVE BAJO' , 'IVE MEDIO' , 'IVE ALTO'] , 
                 color_discrete_sequence=["#5E72EB",  "#FDC094", "#FF9190"] , # ["orange",  "blue", "purple"]
                 title = '',
                 width=900, height=850 ,
                 orientation='v'
                 )

    fig.update_layout(#xaxis_title = 'Nivel de Fluidez' + ' - ' + tipoDesempeñoOProsodia + ' - ',     
                      xaxis_title = ' ',     
                      # yaxis_tickformat = "%f" , 
                      legend = dict(orientation = "h" , 
                                    yanchor = "top" , 
                                    #xanchor="left",                                    
                                    xanchor = 'center',
                                    y = -0.15,
                                    x = 0.5),
                      yaxis = {'visible' : True, 'showticklabels' : True},
                      legend_title_text = '' 
                     )
    """
    fig.update_traces(textposition = 'auto' , 
                      textfont_size = 35 , # 45 , # 25 , # 78 ,
                      #textangle=90,
                      #textfont_color  = 'White',
                      textfont_family = 'Calibri',                      
                      #texttemplate = "%{value:} %",
                      textangle = 0,
                      cliponaxis = False
                      )
    fig.update_layout(bargap=0.30)
    #fig.update_traces(width = 0.4)
    fig.update_traces(textangle=0)
    fig.update_xaxes(tickangle=0)
    #fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
    """
    fig.update_traces(textposition = 'auto' , 
                      textfont_size = 35 , # 45 , # 25 , # 78 ,
                      #textangle=90,
                      #textfont_color  = 'White',
                      textfont_family = 'Calibri',                      
                      #texttemplate = "%{value:} %",
                      textangle = 0,
                      cliponaxis = False
                      )
    fig.update_layout({ 'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})

    
    fig.update_traces(showlegend=False)

    
    fig.update_layout(xaxis = dict(
                      tickfont = dict(size = 30)) # para regular el tamaño de las letras debajo de las barras ) 
                     )    
    

    fig.update_layout(
        yaxis = dict(
        tickfont = dict(size = 1))) # para cambiar el tamaño de la letra de la izquierda

    fig.update_layout(  #title=gene,
                        #xaxis_tickvals=obs["patient"],
                        xaxis_ticktext=[''],
                        xaxis_title="",
                        yaxis_title="")
    
    
    fig.write_image(nombreArchivo)
    return

def dibujarDiagramaDeBarras_EVOLUCION_Fluidez_Por_DEPARTAMENTO(dataFrame , colores ,  nombreArchivo):
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
    #dataFrame = dataFrame.transpose()
    dataFrame = dataFrame.round(1)
    
    fig = px.bar(dataFrame ,    
                 barmode = 'stack' , 
                 text_auto = '5.92f' ,                 
                 color_discrete_sequence = colores, # ["#8A68A6", "#F1D447", "#A1C16D", "#0594A4"]
                 title = '',
                 width=900, height=850 ,
                 orientation='h'
                 )
    fig.update_layout(#xaxis_title = 'Nivel de Fluidez' + ' - ' + tipoDesempeñoOProsodia + ' - ',     
                      xaxis_title = ' ',     
                      # yaxis_tickformat = "%f" , 
                      legend = dict(orientation = "h" , 
                                    yanchor = "top" , 
                                    #xanchor="left",                                    
                                    xanchor = 'center',
                                    y = -0.15,
                                    x = 0.5),
                      yaxis = {'visible' : True, 'showticklabels' : True},
                      legend_title_text = '' 
                     )
    fig.update_traces(textposition = 'auto' , 
                      textfont_size = 35 , # 45 , # 25 , # 78 ,
                      #textangle=90,
                      #textfont_color  = 'White',
                      textfont_family = 'Calibri',                      
                      #texttemplate = "%{value:} %",
                      textangle = 0,
                      cliponaxis = False
                      )
    fig.update_layout(bargap=0.30)
    #fig.update_traces(width = 0.4)
    fig.update_traces(textangle=0)
    fig.update_xaxes(tickangle=0)
    fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
    fig.update_layout({ 'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})

    fig.update_layout(  legend       = dict(font = dict(family = "Calibri", size = 30, color = "black")),
                        legend_title = dict(font = dict(family = "Calibri", size = 30, color = "black")))

    fig.update_layout(xaxis = dict(
                      tickfont = dict(size = 1)) # para regular el tamaño de las letras debajo de las barras ) 
                     )
    
    fig.update_traces(width  = 0.10)

    fig.update_layout(
        yaxis = dict(
        tickfont = dict(size = 30))) # para cambiar el tamaño de la letra de la izquierda
    
    fig.update_layout(  #title=gene,
                        #xaxis_tickvals=obs["patient"],
                        xaxis_ticktext=[''],
                        xaxis_title="",
                        yaxis_title="")

    fig.write_image(nombreArchivo)
    return


"""
def dibujar_imagen_de_Barras_dF(dataFrame , curso , tipoDesempeñoOProsodia): # objetoEscuela
    # no se puede centrar el texto dentro del grafico
    # https://github.com/plotly/plotly.js/issues/3524
    # tipo es : desempeño o prosodia
    # pasamos el objeto escuela para poder crear el archivo con el nombre de la escuela y todos los datos de la misma
    # debemos crear una carpeta para poder mantener las imagenes para cada escuela..
    
    
    # renombramos los nombres de las columnas...para que quede como el original
    listaColumnas = list(dataFrame.columns.values)
    dataFrame.rename(columns = {listaColumnas[1]:' Sup. (' + str(listaColumnas[1]) + ')' , 
                                listaColumnas[2]:' Provincial' + ' ' + listaColumnas[0]
                               }, inplace = True)
    # transponer el dataframe
    dataFrame = dataFrame.transpose()
    dataFrame = dataFrame.round(1)
    
    fig = px.bar(dataFrame ,    
                 barmode = 'stack' , 
                 text_auto = '.2f' ,                                  
                 color_discrete_sequence = ["#8A68A6", "#F1D447", "#A1C16D", "#0594A4"],
                 title = '',
                 width=900-200, height=850-200
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
                      textfont_size = 15,
                      #textangle=90,
                      #textfont_color  = 'White',
                      textfont_family = 'Calibri',
                      texttemplate = "%{value:} %"
                      )
    fig.update_layout(bargap=0.30)
    #fig.update_traces(width = 0.4)
    fig.update_traces(textangle=0)
    fig.update_xaxes(tickangle=0)
    fig.update_layout({ 'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})

    # si dentro del nombre que he construido hay caracteres especiales, debo reemplazarlos
    curso = curso.replace('"' , ' ')
    curso = curso.replace('/' , ' ')

    nombreArchivo = cf.rutaImagenes + tipoDesempeñoOProsodia +'_' + curso + '_' + '.png'

    fig.write_image(nombreArchivo)
    return nombreArchivo

def dibujar_imagen_de_Presentismo_en_formato_Barrass_dF(dataFrame , curso , tipoDesempeñoOProsodia): # objetoEscuela
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
                 text_auto = '.2f' ,                                  
                 color_discrete_sequence = ["#8A68A6", "#F1D447", "#A1C16D", "#0594A4"],
                 title = '',
                 width=900-200, height=850-200
                 )
    fig.update_layout(#xaxis_title = 'Nivel de Fluidez' + ' - ' + tipoDesempeñoOProsodia + ' - ',     
                      xaxis_title = ' ',     
                      yaxis_tickformat = "%f" , 
                      legend = dict(orientation = "h" , 
                                    yanchor = "top" , 
                                    #size = 150 ,
                                    #xanchor="left",
                                    xanchor = 'center',
                                    y = -0.15,
                                    x = 0.5),
                      yaxis = {'visible' : False, 'showticklabels' : True},
                      legend_title_text = '' 
                     )
    fig.update_traces(textposition = 'auto' , 
                      textfont_size = 15,
                      #textangle=90,
                      #textfont_color  = 'White',
                      textfont_family = 'Calibri',
                      texttemplate = "%{value:} %"
                      )
    fig.update_layout(bargap=0.30)
    #fig.update_traces(width = 0.4)
    fig.update_traces(textangle=0)
    fig.update_xaxes(tickangle=0)
    fig.update_layout({ 'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})

    # si dentro del nombre que he construido hay caracteres especiales, debo reemplazarlos
    curso = curso.replace('"' , ' ')
    curso = curso.replace('/' , ' ')

    nombreArchivo = cf.rutaImagenesEscuela + tipoDesempeñoOProsodia +'_' + curso + '_' + '.png'
    

    fig.write_image(nombreArchivo)
    return nombreArchivo

def dibujar_imagen_de_Presentismo_Escuela_Supervsion_Y_Nivel(dataFrame , Escuela_ID , Número_escuela , Nivel , Supervisión): # objetoEscuela
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
                 text_auto = '.2f' ,                                  
                 color_discrete_sequence = ["#8A68A6", "#F1D447", "#A1C16D", "#0594A4"],
                 title = '',
                 width=900-200, height=850-200
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
    fig.update_traces(textposition = ['auto' ] , 
                      textfont_size = 15,
                      #textangle=90,
                      #textfont_color  = 'White',
                      textfont_family = 'Calibri',
                      texttemplate = "%{value:} %"
                      )
    fig.update_layout(bargap=0.30)
    #fig.update_traces(width = 0.4)
    fig.update_traces(textangle=0)
    fig.update_xaxes(tickangle=0)
    fig.update_layout({ 'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})

    Escuela_ID_ = str(Escuela_ID)
    Escuela_ID_ = Escuela_ID_.replace('"' , ' ')
    Escuela_ID_ = Escuela_ID_.replace('/' , ' ')
    Escuela_ID_ = Escuela_ID_.replace('(' , '')
    Escuela_ID_ = Escuela_ID_.replace(')' , '')
    Escuela_ID_ = Escuela_ID_.replace(',' , '')

    nombreArchivo = cf.rutaImagenesEscuela + 'presentismo_escuela_supervision_nivel_'  + Escuela_ID_ + '_' + Número_escuela + '_' + Nivel + '_' + Supervisión + '.png'    

    fig.write_image(nombreArchivo)
    return nombreArchivo

def dibujarDesempeñoPorCurso(dataFrame , Escuela_ID  , Número_escuela , Nivel , Supervisión):
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
                 text_auto = '.2f' ,                                  
                 color_discrete_sequence = ["#8A68A6", "#F1D447", "#A1C16D", "#0594A4"],
                 title = '',
                 width=900-200, height=850-200
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
    fig.update_traces(textposition = ['auto' ] , 
                      textfont_size = 15,
                      #textangle=90,
                      #textfont_color  = 'White',
                      textfont_family = 'Calibri',
                      texttemplate = "%{value:} %"
                      )
    fig.update_layout(bargap=0.30)
    #fig.update_traces(width = 0.4)
    fig.update_traces(textangle=0)
    fig.update_xaxes(tickangle=0)
    fig.update_layout({ 'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})

    Escuela_ID_ = str(Escuela_ID)
    Escuela_ID_ = Escuela_ID_.replace('"' , ' ')
    Escuela_ID_ = Escuela_ID_.replace('/' , ' ')
    Escuela_ID_ = Escuela_ID_.replace('(' , '')
    Escuela_ID_ = Escuela_ID_.replace(')' , '')
    Escuela_ID_ = Escuela_ID_.replace(',' , '')

    # lo guardo para la escuela
    nombreArchivo = cf.rutaImagenesEscuela + 'presentismo_por_curso_' + Escuela_ID_ + '_' + Número_escuela + '_' + Nivel + '_' + Supervisión + '.png'   
    fig.write_image(nombreArchivo)
    nombreArchivo = cf.rutaImagenesSupervisiones + 'presentismo_por_curso_' + Escuela_ID_ + '_' + Número_escuela + '_' + Nivel + '_' + Supervisión + '.png'   
    fig.write_image(nombreArchivo)

    

    return nombreArchivo

def dibujarDataFramesSupervisiones(dataFrame , Supervisión , NivelOriginal):
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
                 text_auto = '.2f' ,                                  
                 color_discrete_sequence = ["#8A68A6", "#F1D447", "#A1C16D", "#0594A4"],
                 title = '',
                 width=900, height=850
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
    fig.update_traces(textposition = ['auto' ] , 
                      textfont_size = 15,
                      #textangle=90,
                      #textfont_color  = 'White',
                      textfont_family = 'Calibri',
                      texttemplate = "%{value:} %" 
                      )
    fig.update_layout(bargap=0.30)
    #fig.update_traces(width = 0.4)
    fig.update_traces(textangle=0)
    fig.update_xaxes(tickangle=0)
    fig.update_layout({ 'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})    
    
    # lo guardo para la supervision
    nombreArchivo = cf.rutaImagenesSupervisiones + 'presentismo_supervisión_' + Supervisión + '_' + NivelOriginal +  '.png'
    fig.write_image(nombreArchivo)
    return nombreArchivo

def dibujarDataFramesEscuelasDeLaSupervisiones(dataFrame , Supervisión , NivelOriginal):
    #print(tabulate(dataFrame.head(150), headers = 'keys' , tablefmt= 'psql'))
    
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
                 text_auto = '.2f' ,                                  
                 color_discrete_sequence = ["#8A68A6", "#F1D447", "#A1C16D", "#0594A4"],
                 title = '',
                 width=900, height=850
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
    fig.update_traces(textposition = ['auto' ] , 
                      textfont_size = 15,
                      #textangle=90,
                      #textfont_color  = 'White',
                      textfont_family = 'Calibri',
                      texttemplate = "%{value:} %" 
                      )
    fig.update_layout(bargap=0.30)
    #fig.update_traces(width = 0.4)
    fig.update_traces(textangle=0)
    fig.update_xaxes(tickangle=0)
    fig.update_layout({ 'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})    
    
    # lo guardo para la supervision
    nombreArchivo = cf.rutaImagenesSupervisiones + 'presentismo_por_escuelas_' + Supervisión + '_' + NivelOriginal +  '.png'
    fig.write_image(nombreArchivo)
    return nombreArchivo

"""
"""
def dibujar_imagen_dF_Desempeño(dataFrameDesempeño):
    fig = px.bar(dataFrameDesempeño, 
                title="Matrícula total a evaluar", # arreglar
                x='Nivel', 
                y='Matrícula_por_Nivel' , 
                color='Nivel' ,             
                color_discrete_sequence=["purple" , "orange" , "yellow"], 
                text = 'Nivel',
                barmode="group",             
                width=900 , height=400,                
                text_auto=True)
    
    # esto es para poder ajustar el ancho de las barras
    for data in fig.data:
        data["width"] = 0.9
    
    fig.update_layout(
        font_family="Lato",
        font_color="blue",
        title_font_family="Lato",
        title_font_color="blue",
        legend_title_font_color="blue"
    )
    fig.update_xaxes(title_font_family="Lato")
    fig.write_image("imagenes/02_imagen_dF_matriculaPorNivel.png")
    return
"""