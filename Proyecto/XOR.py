# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:32:21 2020

@author: Nico
"""
import random

def llavePrivada(a, b):
    return a ^ b

def cifrarX(lp, mensaje):
    aux = []
    aux2 = bytes(mensaje, "utf8")
    for i in range(0, len(aux2)):
        aux.append(aux2[i] ^ lp)
    return aux

def descifrarX(lp, mensaje):
    aux = []
    for i in range(0, len(mensaje)):
        aux.append(mensaje[i] ^ lp)
    return aux
"""
m = cifrar(llavePrivada(A, B), Mensaje)
print("Mensaje cifrado")
print("".join(map(chr, m)))
m2 = descifrar(llavePrivada(A, B), m)
print("Mensaje descifrado")
print("".join(map(chr, m2)))
"""