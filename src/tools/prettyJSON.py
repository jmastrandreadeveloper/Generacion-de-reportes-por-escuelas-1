import json

def pretty_print_json(data):
    # Si hay valores que son JSON en formato string, los convertimos a diccionario o lista
    for key, value in data.items():
        if isinstance(value, dict):
            pretty_print_json(value)  # Llamado recursivo para limpiar subdiccionarios
        elif isinstance(value, str):
            try:
                parsed_value = json.loads(value)  # Intentamos convertir strings JSON en objetos Python
                data[key] = parsed_value
            except (json.JSONDecodeError, TypeError):
                pass  # Si no es JSON válido, lo dejamos como está

    print(json.dumps(data, indent=4, ensure_ascii=False))  # Imprimimos el JSON formateado
