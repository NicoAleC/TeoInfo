# -*- coding: utf-8 -*-
"""
Created on Thu May  7 17:35:03 2020

@author: Nico
"""

def toString(cp):  
    aux = ""  
    for caracter in cp:  
        aux += caracter   
    
    return aux 

diccionario = "abcdefghijklmnopqrstuvwxyz "

palabra = "su majestad ha vuelto garfield"

pcodif =  []

pdcodif = []
a = 7
#a = 4

b = 11
#b = 15

m = len(diccionario)

def inversA(a):
    aux = 0
    for i in range(0, m):
        if((a*i)%m == 1):
            aux = i
            pass
        else:
            i += 1
    return aux

def codificar(lpalabra):
    for i in range(0,len(lpalabra)):
        aux = (a * diccionario.index(lpalabra[i]) + b) % m
        pcodif.append(diccionario[aux])

def decodificar(lpalabra):
    for i in range(0,len(lpalabra)):
        aux = (inversA(a) * (diccionario.index(lpalabra[i]) - b)) % m
        pdcodif.append(diccionario[aux])
        
codificar(palabra)
decodificar(pcodif)
print("Palabra original:\n" + palabra)
print("Palabra codificada:\n" + toString(pcodif))
print("Palabra decodificada:\n" + toString(pdcodif))