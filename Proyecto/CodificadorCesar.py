# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:04:09 2020

@author: Nico
"""

palabra = "Al cesar lo que es del cesar"

pcodif = []

pdcodif = []

linf = 31

lsup = 127

k = 3

tdic = lsup - linf

def codificar(caracter):
    aux = ord(caracter)
    aux += k
    aux = (aux % lsup)
    if(aux < linf):
        aux += linf
    aux = chr(aux)
    return aux

def decodificar(caracter):
    aux = ord(caracter)
    aux -= k
    aux = aux % lsup
    if(aux < linf):
        aux -= lsup
    aux = chr(aux)
    return aux

def toString(cp):  
    aux = ""  
    for caracter in cp:  
        aux += caracter   
    
    return aux 

print("Tamaño del diccionario: " + str(tdic))

for i in range(0, len(palabra)):
    pcodif.append(codificar(palabra[i]))

for i in range(0, len(palabra)):
    pdcodif.append(decodificar(pcodif[i]))

print("Original")
print(palabra)
print("Codificada")
print(toString(pcodif))
print("Decodificada")
print(toString(pdcodif))

    