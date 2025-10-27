import pandas as pd

def combinar_columnas(
    df: pd.DataFrame,
    cols_a_combinar: list[str],
    *,
    nombre_columna_nueva: str | None = None,
    separador: str = "-",
    drop_originales: bool = True,
) -> pd.DataFrame:
    """
    Combina (concatena) varias columnas de un DataFrame en una sola.

    Parámetros
    ----------
    df : pd.DataFrame
        DataFrame de entrada (no se modifica in-place: se devuelve una copia).
    cols_a_combinar : list[str]
        Lista con los nombres de las columnas que quieres concatenar.
    nombre_columna_nueva : str o None, opcional
        Nombre de la columna resultante.  
        Si es None, se crea un nombre a partir de las columnas y el separador.
    separador : str, opcional (default='-')
        Cadena que se colocará entre los valores concatenados.
    drop_originales : bool, opcional (default=True)
        Si True, elimina las columnas originales después de combinarlas.

    Devuelve
    --------
    pd.DataFrame
        Nuevo DataFrame con la columna combinada.
    """
    # --- Validaciones rápidas
    faltantes = set(cols_a_combinar) - set(df.columns)
    if faltantes:
        raise KeyError(f"Columnas no encontradas en el DataFrame: {faltantes}")

    # Nombre automático si el usuario no da uno
    if nombre_columna_nueva is None:
        nombre_columna_nueva = separador.join(cols_a_combinar)

    # Creamos una copia para no tocar el df original
    df_out = df.copy()

    # Concatenamos (convertimos a string para evitar problemas con valores numéricos)
    df_out[nombre_columna_nueva] = df_out[cols_a_combinar] \
        .astype(str) \
        .agg(separador.join, axis=1)

    # Eliminamos columnas originales si corresponde
    if drop_originales:
        df_out = df_out.drop(columns=cols_a_combinar)

    return df_out


"""
Ejemplo de uso
python
Copiar
Editar
# --------------------------- Datos de partida ---------------------------
from io import StringIO
csv = Escuela_ID;Curso ;División;matricula_por_escuela_curso_y_division
989;1°;1ra;33
989;1°;2da;27
989;1°;3°;32
989;1°;5ta;31
989;1°;6ta;27
989;1°;7ma;27
df = pd.read_csv(StringIO(csv), sep=";")

# ----------------------- Combinar Curso  y División ----------------------
df_comb = combinar_columnas(
    df,
    cols_a_combinar=["Curso ", "División"],
    nombre_columna_nueva="Curso-División",  # opcional
    separador="-",                          # opcional
    drop_originales=True                    # deja solo la nueva columna
)

print(df_comb)
Salida

perl
Copiar
Editar
Escuela_ID  matricula_por_escuela_curso_y_division Curso-División
0         989                                      33         1°-1ra
1         989                                      27         1°-2da
2         989                                      32          1°-3°
3         989                                      31         1°-5ta
4         989                                      27         1°-6ta
5         989                                      27         1°-7ma
Variantes útiles
Uso	Llamada	Resultado
Mantener las columnas originales	drop_originales=False	Se añaden ambas columnas (nueva + originales).
Cambiar separador	separador=" · "	Ej: "1° · 1ra".
Dejar que el nombre se genere solo	omite nombre_columna_nueva	Con "Curso -División" obtendrías columna "Curso -División" (ojo a espacios).

Con esta función puedes combinar dos, tres o más columnas simplemente listándolas en cols_a_combinar.

"""
