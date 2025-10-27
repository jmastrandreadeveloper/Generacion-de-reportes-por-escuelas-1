def tipoDesempeño(x):
    """
    diccionarioDesempeño = {'Crítico'   : 0 ,
                            'Básico'    : 1 ,
                            'Medio'     : 2 ,
                            'Avanzado'  : 3 ,
                            '0'         : 'Sin comparativa'
                            }
    """
    if x == 'Crítico':
        return 0
    elif x == 'Básico':
        return 1
    elif x == 'Medio':
        return 2
    elif x == 'Avanzado':
        return 3
    else:
        return 'Sin comparativa'