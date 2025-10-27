def crear_lista_dos_operativos(
        lista_de_Escuela_IDs,
        listaEscuelas_IDs_FL_1,
        listaEscuelas_IDs_FL_2):
    
    """
    Verifica qué escuelas tienen los dos operativos, solo el segundo o solo el primero.

    Parámetros:
    - lista_de_Escuela_IDs: Lista de IDs de las escuelas.
    - ListadoDeObjetosEscuela_op_1: Lista de IDs de escuelas del primer operativo.
    - ListadoDeObjetosEscuela_op_2: Lista de IDs de escuelas del segundo operativo.

    Retorna:
    - Tres listas: 
        1. Escuelas con ambos operativos.
        2. Escuelas sin el primer operativo.
        3. Escuelas sin el segundo operativo.
    """
    
    lista_de_escuelas_con_dos_operativos = []
    lista_de_escuelas_que_le_falta_el_primer_operativo = []
    lista_de_escuelas_que_le_falta_el_segundo_operativo = []

    # Convertir los listados de IDs en conjuntos para búsqueda rápida
    ids_escuelas_op_1 = set(listaEscuelas_IDs_FL_1)
    ids_escuelas_op_2 = set(listaEscuelas_IDs_FL_2)

    # Revisar cada escuela y clasificarla
    for Escuela_ID in lista_de_Escuela_IDs:
        en_op_1 = Escuela_ID in ids_escuelas_op_1
        en_op_2 = Escuela_ID in ids_escuelas_op_2
        
        if en_op_1 and en_op_2:
            lista_de_escuelas_con_dos_operativos.append(Escuela_ID)
        elif not en_op_1 and en_op_2:
            lista_de_escuelas_que_le_falta_el_primer_operativo.append(Escuela_ID)
        elif en_op_1 and not en_op_2:
            lista_de_escuelas_que_le_falta_el_segundo_operativo.append(Escuela_ID)
    
    return (
        lista_de_escuelas_con_dos_operativos, 
        lista_de_escuelas_que_le_falta_el_primer_operativo, 
        lista_de_escuelas_que_le_falta_el_segundo_operativo
    )