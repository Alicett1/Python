# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:49:01 2024

@author: Alice
"""

import matplotlib.pyplot as plt

def naive(chaine, t):
    return sum(ord(i) for i in chaine)%t


class Hashtable:
    def __init__(self, f, t):
        self._fonctionhash=f
        self._taille=t #init permet de définir les différents éléments de self
        self._table=[[] for i in range(t)]
    
    def put(self, key, value):
        l=0
        i=self._fonctionhash(key, self._taille)
        if self._table[i]==[]:
            self._table[i].append((key, value))
            l=l+1
        elif key not in (j[0] for j in self._table[i]):
            self._table[i].append((key, value))
            l+=1
        else:
            for j in range(len(self._table[i])):
                if self._table[i][j][0]==key:
                    self._table[i][j]=(key,value)
        if l>=1.2*self._taille:
            self._table=resize(self)
            self._taille=len(resize(self))
        return self
    
    
    def __str__(self):
        return f"{self._table}"
    
    def get(self, key):
        i=self._fonctionhash(key, self._taille)
        for j in range(len(self._table[i])):
            if key==self._table[i][j][0]:
                return self._table[i][j][1]
            else:
                return None
    
    
    def repartition(self):
        y=[]
        for j in range(self._taille):
            y.append(len(self._table[j]))
        N = len(y)
        x = range(N)
        width = 1/1.5
        plt.bar(x, y, width, color="blue")
        plt.show()
        
    def resize(self):
        h=Hashtable(naive, self._taille)
        for i in h._table:
            L=self._table+h._table
        return L
        
 


f=open("frenchssaccent.dic", 'r')
liste=[]
for ligne in f:
    liste.append(ligne[0: len(ligne)-1])
f.close()

    
def exo5(liste):
    H=Hashtable(naive, 320)
    for i in liste:
        m=len(i)
        H.put(i, m)
    return H
    
        
        
           
            


c='abc'
print(fonctionnaive(c))

Hash=Hashtable(naive, 10) #crée l'objet directement --> pas besoin de __init__
print(Hash.put('abc', 7).put('abc', 5))
print(Hash.get('aaa'))
print(Hash.get('abc'))
print(Hash.repartition())
print(exo5(liste).repartition()) #je ne comprends pas pourquoi il y a des espaces sur mon graphique
print(Hash.resize())





        
        