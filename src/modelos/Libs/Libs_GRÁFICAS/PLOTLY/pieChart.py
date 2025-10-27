import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

def es_color_oscuro(rgb):
    r, g, b = rgb
    luminancia = 0.299*r + 0.587*g + 0.114*b
    return luminancia < 0.5

def graficar_torta_respuestas(col_df, colores_ , labels_ , columnas_ ,  titulo=None):
    if isinstance(col_df, pd.DataFrame):
        col_df = col_df.iloc[0]

    labels = labels_
    values = [col_df[col] for col in columnas_]
    colores = colores_

    fig, ax = plt.subplots(figsize=(8, 8))  # más grande para espacio

    # Hacemos el pie sin etiquetas (labels=None), solo porcentajes
    wedges, texts, autotexts = ax.pie(
        values,
        labels=None,
        autopct='%1.1f%%',
        startangle=90,
        colors=colores,
        textprops={'fontsize': 20, 'weight': 'bold'},
        pctdistance=0.75,
        wedgeprops=dict(width=1.0)  # opcional, para hacer un "donut"
    )
    ax.axis('equal')

    # Cambiar color de los porcentajes según fondo
    for wedge, autotext in zip(wedges, autotexts):
        rgb = wedge.get_facecolor()[:3]
        autotext.set_color('white' if es_color_oscuro(rgb) else 'black')
        autotext.set_fontsize(20)

    # Añadimos etiquetas fuera con líneas guía
    bbox_props = dict(boxstyle="round,pad=0.3", fc="white", ec="gray", lw=0.8)
    kw = dict(arrowprops=dict(arrowstyle="-"),
              bbox=bbox_props, zorder=0, va="center")

    # for i, p in enumerate(wedges):
    #     ang = (p.theta2 - p.theta1)/2. + p.theta1
    #     y = np.sin(np.deg2rad(ang))
    #     x = np.cos(np.deg2rad(ang))
    #     horizontalalignment = "left" if x > 0 else "right"
    #     connectionstyle = f"angle,angleA=0,angleB={ang}"
    #     kw["arrowprops"].update({"connectionstyle": connectionstyle})
    #     ax.annotate(labels[i], xy=(x*0.7, y*0.7), xytext=(1.3*np.sign(x), 1.4*y),
    #                 horizontalalignment=horizontalalignment, 
    #                 fontsize=20,  # <-- aquí defines el tamaño del texto
    #                 **kw)
    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = "left" if x > 0 else "right"
        connectionstyle = "arc3,rad=0.3"  # <--- cambio aquí
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(labels[i], xy=(x, y), xytext=(1.1*np.sign(x), 1.2*y),
                    horizontalalignment=horizontalalignment, 
                    fontsize=20,
                    **kw)

    if titulo:
        ax.set_title(titulo, fontsize=16, weight='bold')

    return fig