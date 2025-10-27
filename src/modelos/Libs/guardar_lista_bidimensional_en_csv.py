import csv

def guardar_lista_bidimensional_en_csv(lista, nombre_archivo):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        writer = csv.writer(archivo_csv)
        # Escribe cada sublista como una fila
        writer.writerows(lista)

# # Ejemplo de uso
# mi_lista = [[1, 'A'], [2, 'B'], [3, 'C']]
# guardar_lista_bidimensional_en_csv(mi_lista, 'archivo_bidimensional.csv')