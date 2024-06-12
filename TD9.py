# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 09:48:31 2024

@author: Alice
"""

class Polynome:
    def __init__(self, n, q, coeffs):
        self._modcoeffs=q
        self._ordre=len(coeffs)
        self._modulo=n
        self._coeffs=coeffs
        self._quot=[0 for i in range(self._ordre)]
        for i in range(self._ordre):
            if self._modulo<=i:
                self._coeffs[i%self._modulo]+=((-1)**(i//self._modulo))*self._coeffs[i]
                self._coeffs[i]=0   #ne jamais mettre de return dans la def de la classe
        for j in range(self._ordre):
            if self._modcoeffs<=self._coeffs[j] or -self._coeffs[j]>=-self._modcoeffs:
                self._quot[j]=self._coeffs[j]//self._modcoeffs
                self._coeffs[j]=self._coeffs[j]%self._modcoeffs
    
    
    def affiche(self):
            return self._coeffs
        
        
    def __add__(self, other):
        if other._modulo==self._modulo and self._ordre == other._ordre:
            Result=[0 for k in range(self._ordre)]
            for i in range(self._ordre):
                Result[i]+=self._coeffs[i]+other._coeffs[i]
        if self._ordre != other._ordre:
            return 'Pb de dimension'
        return Polynome(self._modulo, self._modcoeffs, Result).affiche()
    
    
    def mul(self, other):
        Mul=[0 for i in range(other._ordre+self._ordre)]
        if other._modulo==self._modulo and self._ordre == other._ordre:
            for i in range(self._ordre):
                for j in range(other._ordre):
                    Mul[i+j]+=self._coeffs[i]*other._coeffs[j]
        return Polynome(self._modulo, self._modcoeffs, Mul).affiche()
    
    
    def scalar(self, c):
        scal=[0 for k in range(len(self._coeffs))]
        for k in range(len(self._coeffs)):
            scal[k]=c*self._coeffs[k]
        return Polynome(self._modulo, self._modcoeffs,scal).affiche()
    
    def rescale(self, r):
        L=[0 for i in range(self._ordre)]
        for i in range(len(L)):
            L[i]= self._quot[i]*self._modcoeffs+self._coeffs[i]
            self._coeffs[i]=L[i]%r
        return Polynome(self._modulo, self._modcoeffs, self._coeffs).affiche()
    
    def fscalar(self, r, alpha):
        othercoeffs=[0 for i in range(self._ordre)]
        for k in range(self._ordre):
            othercoeffs[k]= round(self._coeffs[k]*alpha)%r
        return Polynome(self._modulo, self._modcoeffs, othercoeffs).affiche()
        
        
       
        
poly=Polynome(2, 5, [2,3,4,8])
poly3=Polynome(2, 2, [2,3,4,8])
poly2=Polynome(2, 4, [4,5,8,6])
print(poly.affiche())
print(poly.__add__(poly2))
print(poly.mul(poly2))
print(poly.scalar(3))
print(poly.rescale(2))
print(poly.affiche())
print(poly.fscalar(2, 1.6))
