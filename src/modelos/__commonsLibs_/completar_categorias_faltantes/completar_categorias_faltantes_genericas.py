# ✅ Objetivo de la función genérica
# ✔️ La lista de diccionarios (salida de tu función original) tiene:

# Una columna de categoría (ejemplo: “compara”), que define las clases que debe haber.

# Una columna de valor numérico (ejemplo: “matricula_por_escuela_curso_y_progreso”), donde pondremos cero si falta.

# Varias columnas de contexto (como ID de escuela, curso, etc.) que se copian desde los datos ya presentes.

# ✅ Enfoque
# ✅ El usuario le pasa el nombre del campo de categoría, el campo de valor, y los campos de contexto.
# ✅ La función no tiene nombres fijos por dentro.

def completar_categorias_faltantes_generica(
    lista_resultado,
    categorias_esperadas,
    campo_categoria,
    campo_valor,
    campos_contexto=None,
    valor_por_defecto=0
):
    """
    Completa la lista de resultados con categorías faltantes (valor por defecto) 
    y la devuelve en el orden dado por categorias_esperadas.
    """
    if not lista_resultado:
        # No podemos deducir contexto: devolver lista vacía
        return []

    # Averiguar las categorías presentes
    existentes = set(d[campo_categoria] for d in lista_resultado)
    faltantes = [cat for cat in categorias_esperadas if cat not in existentes]

    # Tomar el contexto de la primera fila (asumiendo mismo contexto para todas)
    contexto_base = {}
    if campos_contexto:
        contexto_base = {k: lista_resultado[0].get(k) for k in campos_contexto}

    # Agregar filas faltantes
    for cat in faltantes:
        fila = dict(contexto_base)
        fila[campo_categoria] = cat
        fila[campo_valor] = valor_por_defecto
        lista_resultado.append(fila)

    # Ordenar según el orden de categorias_esperadas
    orden = {cat: i for i, cat in enumerate(categorias_esperadas)}
    lista_resultado_ordenada = sorted(
        lista_resultado,
        key=lambda x: orden.get(x[campo_categoria], len(orden))
    )

    return lista_resultado_ordenada



# ✅ Uso práctico (genérico)
# Así podés llamarla con cualquier estructura de tus datos:

# python
# Copiar
# Editar
# # Resultado de tu función original
# data = filtrar_alumnos_por_escuela_curso_y_progreso_group(...)

# # Definís las categorías obligatorias
# categorias_deseadas = ["Subió de nivel", "Se mantuvo", "Bajó de nivel"]

# # Usás la función genérica
# data_completa = completar_categorias_faltantes_generica(
#     lista_resultado=data,
#     categorias_esperadas=categorias_deseadas,
#     campo_categoria='compara',
#     campo_valor='matricula_por_escuela_curso_y_progreso',
#     campos_contexto=['Escuela_ID', 'Curso ']
# )


# ✅ Características
# ✨ No nombra ninguna columna fija adentro.
# ✨ Te permite especificar:
# ✅ qué columna es la categoría
# ✅ qué columna es el valor
# ✅ qué columnas son contexto
# ✅ qué valor por defecto poner

# ✅ Bonus: valor por defecto opcional
# Si querés, podés pasar otro valor (por ejemplo None, o "") con valor_por_defecto.

# python
# Copiar
# Editar
# data_completa = completar_categorias_faltantes_generica(
#     data,
#     categorias_deseadas,
#     campo_categoria='compara',
#     campo_valor='matricula_por_escuela_curso_y_progreso',
#     campos_contexto=['Escuela_ID', 'Curso '],
#     valor_por_defecto=0
# )
