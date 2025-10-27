# Función para manejar las comparaciones
def comparar(val1, val2):
    try:
        # Convertir a enteros para la comparación
        val1 = int(val1)
        val2 = int(val2)
        
        if val1 == val2:
            return 'Se mantuvo' #'Se Mantiene'
        elif val1 < val2:
            return 'Subió de nivel' #'Mejoró'
        else:
            return 'Bajó de nivel' #'Bajó'
    except (ValueError, TypeError):
        # Si hay un error en la conversión, devolvemos 'sin comparación'
        return 'sin comparación'