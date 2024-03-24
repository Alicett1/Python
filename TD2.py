# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:51:46 2024

@author: Alice
"""
from math import gcd

#%% Exo1

class Fraction:
    def __init__(self, nbre1, nbre2):
        '''Prend deux entiers comme informations et le service offert est de renvoyer un affichage divisé'''
        self.num=nbre1
        self.den=nbre2
        
    def __str__(self):
        return f"my value is {self.num} / {self.den}"
    
    
c=Fraction(3,4)
print(c.__str__())

#%% Exo2

class Fraction:
    def __init__(self, n1, d1):
        '''Prend deux entiers comme informations et le service offert est de renvoyer un affichage divisé'''
        self._num=n1
        self._den=d1
        
        
    def __add__(self, other):
        n= self._num*other._den+other._num*self._den
        d=self._den*other._den
        return Fraction(n,d)
    
    def __multiply__(self, other):
        return f"my value is {self._num*other._num}/{self._den*other._den}"
    
    def __simplify__(self):
        p=gcd(self._num, self._den)
        num1=self._num/p
        den1=self._den/p
        return f"my value is {num1}/{den1}"
    
    def __str__(self):
        return f"my value is {self._num} / {self._den}"
        
    
c=Fraction(3,4)
d=Fraction(1,4)
print(c.__add__(d))
print(c.__multiply__(d))
print(c.__simplify__())

#%% Exo3

def somme(n):
    S=Fraction(1,1)
    for i in range(2,n+1):
        a=Fraction(1,i)
        S=S.__add__(a)
    return S.__str__()

#%% Exo4

def leibniz(n):
    k=0
    S=Fraction(0,1)
    for i in range(n+1):
        if k%2==0:
            a=Fraction(1,2*i+1)
        else:
            a=Fraction(-1,2*i+1)
        S=S.__add__(a)
        k=k+1
    return S.__str__()
        
#%% Exo5

class Polynomial:
    def __init__(self, L):
        '''Prend une liste comme information et le service offert est de renvoyer un affichage sous forme de polynome'''
        self.maxi=len(L)
        self.coeffs=L
        
        
    def __str__(self):
        S=f"{self.coeffs[0]}"
        for i in range(self.maxi,1,-1):
            S=S+f"+{self.coeffs[i-1]}X**{i-1}"
        return f"my value is {S}"
#On met le self.maxi jusqu'à 1 car le décompte va de 4 à 1 et après on utilise i-1 en indice car la liste ne va que jusqu'à 3   
 
    def __add__(self, other):
        S=f"{self.coeffs[0]+other.coeffs[0]}"
        for i in range(self.maxi,1, -1):
            S=S+f"+{self.coeffs[i-1]+other.coeffs[i-1]}X**{i-1}"
        return f"my value is {S}"
    
    def __deriv__(self):
        S=f"{self.coeffs[1]}"
        for i in range(self.maxi,2, -1):
            S=S+f"+{self.coeffs[i-1]*(i-1)}X**{i-2}"
        return f"my value is {S}"
    
    def __integ__(self, c):
        S=f"{c}"
        for i in range(self.maxi,0, -1):
            S=S+f"+{self.coeffs[i-1]*1/i}X**{i}"
        return f"my value is {S}"

c=Polynomial([1,2,3,3])
d=Polynomial([5,2,4,3])
print(c.__str__())
print(c.__add__(d))
print(d.__deriv__())
print(d.__integ__(4))
#%%Exo6

#cf fin exo5




        
    
