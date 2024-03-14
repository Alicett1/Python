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

def score(mot):
    moins=[a,e,i,l,n,o,r,s,t,u]
    deux=[d,g,m]
    trois=[b,c,p]
    quatre=[f,h,v]
    huit=[j,q]
    dix=[k,w,x,y,z]
    
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
            
def max_score(listemots):
    scoretotal=[]
    for i in listemots:
        scoretotal.append(score(i))
    maxi2=scoretotal[0]
    for k in scoretotal:
        if len(k)>len(maxi2):
            maxi2=k
    return maxi2
        
        
      