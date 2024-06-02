# -*- coding: utf-8 -*-
"""
Created on Wed May 29 09:55:59 2024

@author: Alice
"""

from struct import *

f=open("the_wall.wav", "rb")
data=f.read()

L=[]
size=unpack_from("I", data, 40)[0]
for i in range(size):
    r=unpack_from("hh", data, 40+i)  #Utilise h car prend des plus petites valeurs donc besoin de stocker sur 2 octets uniquement
    L.append(r)

print(len(L))

def pistes(L):
    L=[]
    size=unpack_from("I", data, 40)[0]
    for i in range(size):
        r=unpack_from("hh", data, 40+i)  #Utilise h car prend des plus petites valeurs donc besoin de stocker sur 2 octets uniquement
        L.append(r)
    pistedte=[]
    pistegauche=[]
    for i in L:
        pistedte.append(i[0])
        pistegauche.append(i[1])
    print(pistedte)

pistes(L)

def header():
    with open(New, "wb") as New:
        New.write(b"RIFF") #permet de transformer caractère en bits
        New.write(pack("I", len(pistedte)+44-8)) #pack permet de transformer nombre en bits
        New.write(b"WAVEfmt")
        New.write(pack("IHHIIII", 16, 1, 2, 44100, 176400, 4, 16))
        New.write(b"data")
        New.write(pack("I", len(L)*4))
    for i in range(len(pistedte)):
        New.write(pack("hh", pistedte[i], pistegauche[i]))
    return New


    
        



        