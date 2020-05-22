# -*- coding: utf-8 -*-
"""
Created on Thu May 21 16:54:37 2020

@author: Nico
"""

import math

def arco(r, alfa, letra):
    return 2 * math.pi * r * (alfa * letra) / 360

def angulo(r, arc):
    return arc * 360 / (2 * math.pi * r )

def cifrarA(r, alfa, mensaje, diccionario):
    aux = []
    for i in range(0, len(mensaje)):
        arc = 0
        arc = arco(r, alfa, diccionario.index(mensaje[i]))
        #print(mensaje[i] + " = " + str(arc))
        aux.append(arc)
    return aux

def descifrarA(r, alfa, mensaje, diccionario):
    aux = ""
    for i in range(0, len(mensaje)):
        ang = angulo(r, mensaje[i])
        letra = ang / alfa
        #print("ángulo: " + str(ang) + "\narco: " + str(mensaje[i]))
        aux += diccionario[int(round(letra))]
    return aux
"""
m = cifrar(R, "hola bola")
print("Mensaje cifrado:\n")
print(m)
print("Mensaje descifrado:\n" + descifrar(R, m))
"""