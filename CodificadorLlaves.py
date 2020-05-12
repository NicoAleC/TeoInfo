# -*- coding: utf-8 -*-
"""
Created on Mon May 11 18:27:12 2020

@author: Nico
"""

import sys
import math
import ast

def toString(cp):  
    aux = ""  
    for caracter in cp:  
        aux += caracter   
    
    return aux 

diccionario = "abcdefghijklmnopqrstuvwxyz "

palabra = input("Escriba el mensaje a cifrar\n")
#palabra = "la casa grande"

pcodif = []

pdcodif = []

#p = 17
try:
    p = int(input("Introduzca el valor de la variable p: "))
except:
    print("El valor ingresado no fue un número entero")
    sys.exit()

#q = 2
try:
    q = int(input("Introduzca el valor de la variable q: "))
except:
    print("El valor ingresado no fue un número entero")
    sys.exit()

n = p * q
print("n = " + str(n))

z = (p - 1) * (q - 1)
print("z = " + str(z))

#d = 3
try:
    d = int(input("Introduzca el valor de la variable d: "))
except:
    print("El valor ingresado no fue un número entero")
    sys.exit()

e = 1

lprivada = []
lpublica = []

if d > z or math.gcd(d, z) != 1:
    print("La variable d no cumple con las condiciones necesarias")
    sys.exit()

def encontrarE(x):
    while (True):
        if ((z * (x + 1)) % d == 0) and ((x * d) % z == 1):
            break
        x = x + 1
    e = x
    print("e = " + str(e))
    lprivada.append(n)
    lprivada.append(d)
    lpublica.append(n)
    lpublica.append(e)


def codificar(llave, mensaje):
    for i in range(0, len(mensaje)):
        aux = (diccionario.index(mensaje[i]) ** llave[1]) % llave[0]
        pcodif.append(aux)

def decodificar(llave, mensaje):
    for i in range(0, len(mensaje)):
        aux = (mensaje[i] ** llave[1]) % llave[0]
        pdcodif.append(diccionario[aux])


encontrarE(e)

try:
    print("1: encriptar con llave propia\n2: encriptar con otra llave pública\n0: saltar")
    escojer = int(input("Introduzca el valor para escojer: "))
except:
    print("El valor ingresado no fue un número entero")
    sys.exit()

if escojer == 1:
    codificar(lpublica, palabra)
elif escojer == 2:
    try:
        aux_n = int(input("Valor n: "))
        aux_e = int(input("Valor e: "))
        aux_p = [aux_n, aux_e]
        codificar(aux_p, palabra)
    except:
        print("El valor ingresado no fue un número entero")
        sys.exit()

try:
    print("1: desencriptar mensaje propio\n2: desencriptar mensaje ajeno\n0: saltar")
    escojer = int(input("Introduzca el valor para escojer: "))
except:
    print("El valor ingresado no fue un número entero")
    sys.exit()
    
if escojer == 1:
    decodificar(lprivada, pcodif)
elif escojer == 2:
    try:
        mensaje_exterior = ast.literal_eval(input("Ingresar mensaje para desencriptar:\n"))
    except:
        print("Los datos ingresados no son una lista")
        sys.exit()
    
    decodificar(lprivada, mensaje_exterior)

print("Palabra original:\n" + palabra)
print("Llave pública:")
print(lpublica)
print("Llave privada:")
print(lprivada)
print("Palabra encriptada:")
print(pcodif)
print("Palabra desencriptada:\n" + toString(pdcodif))

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        