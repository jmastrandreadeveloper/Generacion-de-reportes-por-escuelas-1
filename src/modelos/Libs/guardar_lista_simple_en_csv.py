import csv

def guardar_lista_simple_en_csv(lista, nombre_archivo):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        writer = csv.writer(archivo_csv)
        # Escribe cada elemento en una fila
        for item in lista:
            writer.writerow([item])