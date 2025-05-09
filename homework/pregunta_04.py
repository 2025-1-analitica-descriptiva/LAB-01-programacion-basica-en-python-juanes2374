"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
import os

def pregunta_04():
    conteo_meses = {}
    ruta = os.path.join(os.path.dirname(__file__), '..', 'files', 'input', 'data.csv')

    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo, delimiter='\t')
        for fila in lector:
            fecha = fila[2]
            mes = fecha.split('-')[1]
            if mes in conteo_meses:
                conteo_meses[mes] += 1
            else:
                conteo_meses[mes] = 1

    resultado = sorted(conteo_meses.items())
    return resultado
