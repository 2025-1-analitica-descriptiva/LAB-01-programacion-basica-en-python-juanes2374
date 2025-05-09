import csv
import os

def pregunta_12():
    suma_por_letra = {}
    ruta = os.path.join(os.path.dirname(__file__), '..', 'files', 'input', 'data.csv')

    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo, delimiter='\t')
        for fila in lector:
            letra = fila[0]
            suma_valores = sum(int(par.split(':')[1]) for par in fila[4].split(','))
            if letra in suma_por_letra:
                suma_por_letra[letra] += suma_valores
            else:
                suma_por_letra[letra] = suma_valores

    return dict(sorted(suma_por_letra.items()))
