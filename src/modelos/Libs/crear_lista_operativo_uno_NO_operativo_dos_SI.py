# la idea es que sea una lista de los ID de las escuelas y no una lista de objetos
def crear_lista_operativo_uno_NO_operativo_dos_SI(
        lista_de_Escuela_IDs,
        listaEscuelas_IDs_FL_1,
        listaEscuelas_IDs_FL_2):
    
    # Convertir los listados de IDs en conjuntos para búsqueda rápida
    ids_escuelas_op_1 = set(listaEscuelas_IDs_FL_1)
    ids_escuelas_op_2 = set(listaEscuelas_IDs_FL_2)
    # Lista de escuelas a las que les falta el primer operativo pero que sí tienen el segundo
    lista_de_escuelas_que_le_falta_el_primer_operativo_pero_tiene_el_segundo = []
    
    for Escuela_ID in lista_de_Escuela_IDs:
        en_op_1 = Escuela_ID in ids_escuelas_op_1
        en_op_2 = Escuela_ID in ids_escuelas_op_2
        
        # Si no está en el primer operativo pero sí está en el segundo
        if not en_op_1 and en_op_2:
            lista_de_escuelas_que_le_falta_el_primer_operativo_pero_tiene_el_segundo.append(Escuela_ID)
    
    return lista_de_escuelas_que_le_falta_el_primer_operativo_pero_tiene_el_segundo