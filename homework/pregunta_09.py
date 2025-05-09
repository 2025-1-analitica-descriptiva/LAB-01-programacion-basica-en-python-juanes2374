"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
import os

def pregunta_09():
    conteo = {}
    ruta = os.path.join(os.path.dirname(__file__), '..', 'files', 'input', 'data.csv')

    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo, delimiter='\t')
        for fila in lector:
            claves = fila[4].split(',')
            for par in claves:
                clave = par.split(':')[0]
                if clave in conteo:
                    conteo[clave] += 1
                else:
                    conteo[clave] = 1

    resultado = dict(sorted(conteo.items()))
    return resultado
