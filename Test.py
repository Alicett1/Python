# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:18:20 2024

@author: Alice TOUTAIN
"""

'''Q1 : On peut représenter le labyrinthe comme un dictionnaire avec comme clés les numéros des carrefours X et
comme valeurs des listes qui contiennent les numéros des portes partant du carrefour X et la destination de ces portes'''

Labyrinthe={0:[(0,2),(1,1),(2,3)], 1:[(0,0)], 2:[(1,0),(0,4),(2,3)], 3:[(1,0),(0,5),(2,2)], 4:[(0,6),(1,2)], 5:[(0,6),(1,3)], 6:[(0,4),(1,5)]}

def parcours(laby, cardépart, ordre):
    indice=cardépart
    for j in range(len(ordre)):
        for i in laby[indice]:
            if i[0]==ordre[j]:
                indice=i[1]
            if indice not in laby:
                indice=indice
    return indice


print(parcours(Labyrinthe, 2, [0,0,1,1,1]))
print(parcours(Labyrinthe, 2, [2,2,1,0]))


def retourpas(laby, cardépart, ordre):
    indice=cardépart
    listeparcours={indice:1}  #permet de compter le nombre de passage sur un même carrefour
    nbrecarrefoursatteints=0
    for j in range(len(ordre)):
        for i in laby[indice]:
            if i[0]==ordre[j]:
                indice=i[1]
                if indice not in listeparcours:
                    listeparcours.setdefault(indice, 1)  
                elif indice in listeparcours:
                    listeparcours[indice]+=1
    for pos in listeparcours:
        if listeparcours[pos]>=2:
            nbrecarrefoursatteints+=1
    return nbrecarrefoursatteints
            
print(retourpas(Labyrinthe, 6, [1,1,0,1,0,1,2]))  


def passagepartous(laby, cardépart, ordre):
    indice=cardépart
    passé=[]  
    nbrecarrefoursatteints=0
    for j in range(len(ordre)):
        for i in laby[indice]:
            if i[0]==ordre[j]:
                indice=i[1]
                if indice not in passé:
                    passé.append(indice)
    if len(passé)==len(laby):
        return True
    return False
    
print(passagepartous(Labyrinthe, 2, [0,0,1,1,1]))


def simplifie(L, cardépart, ordre):
    indice=cardépart
    listeparcours=[indice]  #permet de retracer le parcours en entier et de voir s'il y a une boucle
    for j in range(len(ordre)):
        for i in laby[indice]:
            if i[0]==ordre[j]:
                indice=i[1]
                listeparcours.append(indice)
    for j in range(len(listeparcours)):
        if listeparcours[j-2]==listeparcours[j]:
            return True
                
#programme non fini        
                
        
        
    