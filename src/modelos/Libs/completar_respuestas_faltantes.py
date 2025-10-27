import pandas as pd

# def completar_respuestas_faltantes(df, dict_pregunta_id_RespuestaAlumno):
#     # Lista de preguntas esperadas
#     preguntas_esperadas = list(dict_pregunta_id_RespuestaAlumno.keys())

#     # Lista para guardar nuevos registros
#     filas_a_agregar = []

#     # Recorremos cada alumno individualmente
#     for alumno_id, grupo in df.groupby('Alumno_ID'):
#         preguntas_respondidas = grupo['pregunta_id'].unique().tolist()
#         preguntas_faltantes = set(preguntas_esperadas) - set(preguntas_respondidas)

#         for pregunta_faltante in preguntas_faltantes:
#             # Tomamos una fila cualquiera del grupo para copiar estructura
#             fila_base = grupo.iloc[0].copy()

#             fila_base['pregunta_id'] = pregunta_faltante
#             fila_base['opcion_id'] = dict_pregunta_id_RespuestaAlumno[pregunta_faltante]['Sin respuesta']
#             filas_a_agregar.append(fila_base)

#     # Creamos un DataFrame con las filas nuevas y las unimos al original
#     df_completado = pd.concat([df, pd.DataFrame(filas_a_agregar)], ignore_index=True)

#     # Ordenamos por Alumno_ID y pregunta_id para mantener orden lógico
#     df_completado.sort_values(by=['Alumno_ID', 'pregunta_id'], inplace=True)
#     df_completado.reset_index(drop=True, inplace=True)

#     return df_completado
import pandas as pd

def completar_y_limitar_respuestas(df, dict_pregunta_id_RespuestaAlumno):
    preguntas_esperadas = list(dict_pregunta_id_RespuestaAlumno.keys())
    filas_resultantes = []

    # Procesar cada alumno individualmente
    for alumno_id, grupo in df.groupby('Alumno_ID'):
        grupo = grupo.copy()

        # Eliminar respuestas duplicadas por pregunta_id (por si hay más de una respuesta a la misma pregunta)
        grupo = grupo.drop_duplicates(subset='pregunta_id')

        # Si tiene más de 16 respuestas, dejamos solo las primeras 16 ordenadas por pregunta_id
        if len(grupo) > 16:
            grupo = grupo.sort_values(by='pregunta_id').head(16)

        # Si tiene menos de 16, completamos
        preguntas_respondidas = set(grupo['pregunta_id'])
        preguntas_faltantes = set(preguntas_esperadas) - preguntas_respondidas

        for pregunta_faltante in preguntas_faltantes:
            fila_base = grupo.iloc[0].copy()
            fila_base['pregunta_id'] = pregunta_faltante
            fila_base['opcion_id'] = dict_pregunta_id_RespuestaAlumno[pregunta_faltante]['Sin respuesta']
            grupo = pd.concat([grupo, pd.DataFrame([fila_base])], ignore_index=True)

        # Asegurar que tenga exactamente 16 respuestas (por si después de completar hay más)
        grupo = grupo.sort_values(by='pregunta_id').head(16)

        filas_resultantes.append(grupo)

    df_final = pd.concat(filas_resultantes, ignore_index=True)
    df_final.sort_values(by=['Alumno_ID', 'pregunta_id'], inplace=True)
    df_final.reset_index(drop=True, inplace=True)
    return df_final

