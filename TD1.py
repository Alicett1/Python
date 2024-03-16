# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:15:44 2024

@author: Alice
"""
print("test")

liste = []


f=open("frenchssaccent.dic", 'r')

for ligne in f:
    liste.append(ligne[0: len(ligne)-1])
f.close()
    
nbre=[]
for mot in liste:
    n=0
    tirage = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']
    for lettre in mot: 
        if lettre in tirage:
            n=n+1
            tirage.remove(lettre)
    if n==len(mot):
        nbre.append(mot)
            
maxi=nbre[0]
for k in nbre:
    if len(k)>len(maxi):
        maxi=k
print(maxi)


#Pour représenter les points associés aux lettres, on utilise des listes.

def scoredf(mot):
    score=0
    moins=['a','e','i','l','n','o','r','s','t','u']
    deux=['d','g','m']
    trois=['b','c','p']
    quatre=['f','h','v']
    huit=['j','q']
    dix=['k','w','x','y','z']
    
    for i in mot:
        if i in moins:
            score=score+1
        if i in deux:
            score=score+2
        if i in trois:
            score=score+3
        if i in quatre:
            score=score+4
        if i in huit:
            score=score+8
        if i in dix:
            score=score+10
    return score
            
def max_score(listemots):
    scoretotal=[0 for i in range(len(listemots))]
    for i in range(len(listemots)):
        scoretotal[i]=scoretotal[i]+scoredf(listemots[i])
        
    maxi2=scoretotal[0]
    p=0
    for k in range(len(scoretotal)):
        if scoretotal[k]> maxi2:
            p=listemots[k]
            maxi2= scoretotal[k]
    return maxi2, p


#%%Exercice 4
#Il faut ajouter une liste de 0 points avec le symbole '?'. Et ajouter une condition qui fait que lorsque i parcourt les lettres d'un mot, s'il trouve plus d'un joker, le joueur perd. 

def scoredf(mot):
    score=0
    moins=['a','e','i','l','n','o','r','s','t','u']
    deux=['d','g','m']
    trois=['b','c','p']
    quatre=['f','h','v']
    huit=['j','q']
    dix=['k','w','x','y','z']
    zero=['?']
    
    for i in mot:
        b=0
        if i in moins:
            score=score+1
        if i in deux:
            score=score+2
        if i in trois:
            score=score+3
        if i in quatre:
            score=score+4
        if i in huit:
            score=score+8
        if i in dix:
            score=score+10
        if i in zero:
            b=b+1
            score=score
    return score
            
def max_score(listemots):
    nbre_interrogation=0
    scoretotal=[0 for i in range(len(listemots))]
    for i in range(len(listemots)):
        scoretotal[i]=scoretotal[i]+scoredf(listemots[i])
        nbre_interrogation=nbre_interrogation+b
    if nbre_interrogation>1:
        return False
    maxi2=scoretotal[0]
    p=0
    for k in range(len(scoretotal)):
        if scoretotal[k]> maxi2:
            p=listemots[k]
            maxi2= scoretotal[k]
    return maxi2, p

