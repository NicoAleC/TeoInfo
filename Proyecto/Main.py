# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:50:22 2020

@author: Nico
"""

import ast
from XOR import * 
from Arco import *

diccionario = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ "

Mensaje = "hola bola"

print("Inicializando valores para el cifrador de Arco")
#R = int(input("Introducir el valor de R:\n"))
R = 100

Alfa = R / len(diccionario)

print("Inicializando valores para el cifrador de XOR")
A = random.getrandbits(8)

#B = int(input("Introducir valor de la llave B:\n"))
B = 15

#cifrado
mensaje_cifradoA = str(cifrarA(R, Alfa, Mensaje, diccionario)) + ";" + str(R)
print("Mensaje cifrado con Arco:\n" + mensaje_cifradoA)
mensaje_cifradoX = str(cifrarX(llavePrivada(A, B), mensaje_cifradoA))
print("Mensaje cifrado con XOR:\n" + "".join(map(chr, ast.literal_eval(mensaje_cifradoX))))

#descifrado
mensaje_descifradoX = descifrarX(llavePrivada(A, B), ast.literal_eval(mensaje_cifradoX))
aux_mdX = "".join(map(chr, mensaje_descifradoX))
aux_mdX2, radio = aux_mdX.split(";")
print("Mensaje descifrado con XOR:\n" + aux_mdX)
mensaje_descifradoA = descifrarA(int(radio), Alfa, ast.literal_eval(aux_mdX2), diccionario)
print("Mensaje descifrado con Arco\n" + mensaje_descifradoA)