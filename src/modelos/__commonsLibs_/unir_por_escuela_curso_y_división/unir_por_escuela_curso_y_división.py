import pandas as pd

def unir_por_escuela_curso_division(
    df_left: pd.DataFrame,
    df_right: pd.DataFrame,
    how: str = "inner",
    suffixes: tuple = ("_x", "_y"),
    validate: str | None = "one_to_one"
) -> pd.DataFrame:
    """
    Une dos DataFrames por Escuela_ID, Curso  y División.

    Parámetros
    ----------
    df_left, df_right : pd.DataFrame
        DataFrames a unir.  Deben contener las columnas
        'Escuela_ID', 'Curso ' y 'División'.
    how : {'left','right','inner','outer'}, opcional (default='inner')
        Tipo de unión (merge).
    suffixes : tuple[str,str], opcional
        Sufijos para columnas que se repitan fuera de las claves.
    validate : str | None, opcional
        Valida la relación entre claves.  
        - 'one_to_one', 'one_to_many', 'many_to_one', 'many_to_many'  
        - None desactiva la validación.

    Devuelve
    --------
    pd.DataFrame
        DataFrame resultado del merge.
    """
    claves = ["Escuela_ID", "Curso ", "División"]

    # — Comprobamos que los dos DF tengan las columnas requeridas
    faltantes_left  = set(claves) - set(df_left.columns)
    faltantes_right = set(claves) - set(df_right.columns)
    if faltantes_left or faltantes_right:
        raise KeyError(
            f"Columnas faltantes → "
            f"df_left: {faltantes_left or 'OK'}, "
            f"df_right: {faltantes_right or 'OK'}"
        )

    # — Realizamos el merge
    merged = pd.merge(
        df_left,
        df_right,
        how=how,
        on=claves,
        suffixes=suffixes,
        validate=validate
    )

    return merged



"""
Cómo usarla
python
Copiar
Editar
# Supongamos que tienes df1 y df2 ya cargados
df_union = unir_por_escuela_curso_division(df1, df2, how="inner")

# Si quieres quedarte con todos los registros de ambos (similar a SQL FULL OUTER)
df_union = unir_por_escuela_curso_division(df1, df2, how="outer")
Detalles útiles
Parámetro	¿Para qué sirve?
how	El tipo de unión:
• 'inner' = intersección de claves.
• 'left', 'right' = como en SQL.
• 'outer' = unión completa.
suffixes	Si fuera de las claves hay columnas con el mismo nombre, se renombran añadiendo estos sufijos.
validate	Controla la relación entre claves:
– 'one_to_one' (por defecto) asegura que en cada DF las claves no se repitan.
– Pon 'one_to_many', … según tu caso.
– None si no quieres validar.

"""
