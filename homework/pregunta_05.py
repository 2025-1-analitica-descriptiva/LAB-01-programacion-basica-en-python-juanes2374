"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
import os

def pregunta_05():
    min_max = {}
    ruta = os.path.join(os.path.dirname(__file__), '..', 'files', 'input', 'data.csv')

    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo, delimiter='\t')
        for fila in lector:
            letra = fila[0]
            valor = int(fila[1])
            if letra in min_max:
                min_max[letra].append(valor)
            else:
                min_max[letra] = [valor]

    resultado = [(letra, max(valores), min(valores)) for letra, valores in sorted(min_max.items())]
    return resultado
