# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:54:07 2020

@author: Nico
"""

diccionario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

palabra = "LEUUCRIBCIEV FSHCKYEVH XLIMRJSVQEXMSRW "

resultado = []

for i in range(1, len(diccionario)):
    res = ""
    for j in range(0, len(palabra)):
        if palabra[j] != " ":
            k = diccionario.index(palabra[j])
            k = (k - i) % len(diccionario)
            res += diccionario[k]
        else:
            res += " "
    resultado.append(res)

print(resultado)

def contador(p):
    return 0