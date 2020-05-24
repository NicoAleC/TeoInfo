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

print("Inicializando valores para el cifrador de XOR")
A = int(input("Introducir valor de la llave A:\n")) % 256
#B = 15
B = int(input("Introducir valor de la llave B:\n")) % 256
LP = llavePrivada(A, B)

operar = input("Escoja una opción:\n0: Saltar\n1: Encriptar\n2: Desencriptar\n")

if operar == "1":
    print("Inicializando valores para el cifrador de Arco")
    R = int(input("Introducir el valor de R:\n"))
    #R = 100
    Alfa = R / len(diccionario)
    
    #cifrado
    mensaje_cifradoA = str(cifrarA(R, Alfa, Mensaje, diccionario)) + ";" + str(R)
    print("Mensaje cifrado con Arco:\n" + mensaje_cifradoA)
    mensaje_cifradoX = cifrarX(LP, mensaje_cifradoA)
    print("Mensaje cifrado con XOR:\n" + "".join(map(chr, mensaje_cifradoX)))
elif operar == "2":
    #descifrado
    mensaje_descifradoX = descifrarX(LP, aLista(input("Introduzca el mensaje encriptado:\n")))
    aux_mdX = "".join(map(chr, mensaje_descifradoX))
    aux_mdX2, radio = aux_mdX.split(";")
    Alfa = int(radio) / len(diccionario)
    print("Mensaje descifrado con XOR:\n" + aux_mdX)
    mensaje_descifradoA = descifrarA(int(radio), Alfa, ast.literal_eval(aux_mdX2), diccionario)
    print("Mensaje descifrado con Arco\n" + mensaje_descifradoA)
else:
    print("Programa terminado")