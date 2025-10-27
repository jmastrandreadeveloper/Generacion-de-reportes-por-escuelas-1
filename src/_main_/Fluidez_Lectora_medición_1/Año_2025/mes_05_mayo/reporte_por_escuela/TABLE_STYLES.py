# acá se van a colocar los estilos de las tablas que se van a usar en el informe en PDF

from reportlab.lib import colors

tableStyle_1 = [
        ('BACKGROUND', (0, 0), (-1, 0), colors.Color(49/255, 122/255, 138/255)),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
        ('FONTNAME', (1, 1), (-1, -1), 'REM-Regular'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),  # Reducido de 6 a 3
        ('TOPPADDING', (0, 0), (-1, -1), 6),    # Añadido y ajustado a 3
        ('BACKGROUND', (0, 1), (-1, -2), colors.white),
        ('BACKGROUND', (0, -1), (-1, -1), colors.Color(157/255, 222/255, 220/255)),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 0), (-1, 0), 14),       # Tamaño de letra más pequeño para el encabezado
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke)  # Color de texto blanco para el encabezado
    ]

# Definir los colores deseados
color_columna_1 = colors.Color(32/255, 81/255, 89/255)  # "#205159"
color_columna_2 = colors.Color(48/255, 122/255, 138/255)  # "#307A8A"
color_columna_3 = colors.Color(74/255, 172/255, 174/255)  # "#4AACAE"

# Estilo de la tabla
tableStyle_2 = [
    ('BACKGROUND', (0, 0), (0, -1), color_columna_1),  # Color columna 1, incluyendo encabezado
    ('BACKGROUND', (1, 0), (1, -1), color_columna_2),  # Color columna 2, incluyendo encabezado
    ('BACKGROUND', (2, 0), (2, -1), color_columna_3),  # Color columna 3, incluyendo encabezado
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),  # Color del texto blanco en todas las celdas
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
    ('FONTNAME', (1, 1), (-1, -1), 'REM-Regular'),
    ('FONTSIZE', (0, 0), (-1, -1), 12),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
]

tableStyle_3 = [
        ('BACKGROUND', (0, 0), (-1, 0), colors.Color(49/255, 122/255, 138/255)),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
        ('FONTNAME', (1, 1), (-1, -1), 'REM-Regular'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),  # Reducido de 6 a 3
        ('TOPPADDING', (0, 0), (-1, -1), 6),    # Añadido y ajustado a 3
        ('BACKGROUND', (0, 1), (-1, -2), colors.white),
        ('BACKGROUND', (0, -1), (-1, -1), colors.Color(157/255, 222/255, 220/255)),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 0), (-1, 0), 6),       # Tamaño de letra más pequeño para el encabezado
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke)  # Color de texto blanco para el encabezado
]

tableStyle_4 = [
        ('BACKGROUND', (0, 0), (-1, 0), colors.Color(49/255, 122/255, 138/255)),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
        ('FONTNAME', (1, 1), (-1, -1), 'REM-Regular'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),  # Reducido de 6 a 3
        ('TOPPADDING', (0, 0), (-1, -1), 6),    # Añadido y ajustado a 3
        ('BACKGROUND', (0, 1), (-1, -2), colors.white),
        ('BACKGROUND', (0, -1), (-1, -1), colors.Color(157/255, 222/255, 220/255)),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 0), (-1, 0), 6),       # Tamaño de letra más pequeño para el encabezado
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke)  # Color de texto blanco para el encabezado
]

tableStyle_5 = [
    ('BACKGROUND', (0, 0), (-1, 0), colors.Color(49/255, 122/255, 138/255)),  # Color de fondo del encabezado
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Color del texto del encabezado
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alineación de todo el texto
    ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),  # Fuente del encabezado
    ('FONTNAME', (1, 1), (-1, -1), 'REM-Regular'),  # Fuente del resto de la tabla
    ('FONTSIZE', (0, 0), (-1, 0), 26),  # Tamaño de letra del encabezado
    ('FONTSIZE', (0, 1), (-1, -1), 12),  # Tamaño de letra del contenido
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('BACKGROUND', (0, 1), (-1, -2), colors.white),  # Fondo de las filas de datos
    ('BACKGROUND', (0, -1), (-1, -1), colors.Color(157/255, 222/255, 220/255)),  # Última fila de otro color
    ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Bordes de la tabla
] 

tableStyle_7 = [
        ('BACKGROUND', (0, 0), (-1, 0), colors.Color(157/255, 222/255, 220/255)),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Centrado vertical del título de las columnas de la tabla
        ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('FONTNAME', (0, 1), (-1, -1), 'REM-Regular'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]