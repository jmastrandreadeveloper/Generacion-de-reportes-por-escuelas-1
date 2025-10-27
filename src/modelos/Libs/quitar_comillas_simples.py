def quitar_comillas_simples(lista):
    resultado = []
    for elemento in lista:
        elemento_str = str(elemento)  # Convertir a cadena temporalmente para aplicar los chequeos
        # Verificar si el elemento es un número entero
        if elemento_str.isdigit():
            resultado.append(int(elemento_str))
        # Verificar si el elemento es un número flotante
        elif elemento_str.replace('.', '', 1).isdigit():
            resultado.append(float(elemento_str))
        # Si no es número, dejarlo como está
        else:
            resultado.append(elemento)
    return resultado