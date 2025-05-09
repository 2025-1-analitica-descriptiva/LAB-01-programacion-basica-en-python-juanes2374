"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
import os

def pregunta_06():
    valores = {}
    ruta = os.path.join(os.path.dirname(__file__), '..', 'files', 'input', 'data.csv')

    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo, delimiter='\t')
        for fila in lector:
            pares = fila[4].split(',')
            for par in pares:
                clave, valor = par.split(':')
                valor = int(valor)
                if clave in valores:
                    valores[clave].append(valor)
                else:
                    valores[clave] = [valor]

    resultado = [(clave, min(v), max(v)) for clave, v in sorted(valores.items())]
    return resultado
