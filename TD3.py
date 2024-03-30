# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:54:07 2024

@author: Alice
"""

class Tree:
    def __init__(self, label, *children):
        self._label=str(label)
        self._children=children
        
    def __label__(self):
        return self._label
    
    def __children__(self):
        return self._children
        
    def nb_children(self):
        return len(self._children)
    
    def child(self, i):
        if i ==0:
            return Tree(self)
        if i>0:
            return self._children[i-1]
        
    def is_leaf(self):
        if len(self._children)==0:
            return True
        
    def __str__(self):
        L=''
        for child in self._children:
            if child.is_leaf==True:
                L+=f"{child._label()}"
            else:
                L+=child.__str__()  #Appel récursif sur l'arbre   
        return f"{self._label,L}"
    
    def depth(self):
        L=[1]
        p=1
        if self.is_leaf()==True:
            return p-1
        else:
            for child  in self._children:
                p=1
                p+=child.depth()
                L.append(p)
            return(max(L))
    
    def strexo4(self):
        L=[]
        T=0
        for child1 in self._children:
            v=child1.__label__()    
            L.append(v)
            T=tuple(L)
        return f"{self._label}{T}"
    
    
    def __eq__(self, value):
        L=[]
        L2=[]
        if self.__label__() == value.__label__():
            for child1 in self._children:
                v=child1.__label__()
                w=int(v)
                L.append(w)
                T=tuple(L)
            for child2 in value._children:
                v2=child2.__label__()
                w2=int(v)
                L2.append(w)
                T2=tuple(L2)
            for i in T:
                if i in T2:
                    return True
        return False
    
    def deriv(self, r):
        if self.is_leaf()==True:
            if self.__label__()==r:
                return Tree('1')
            return Tree('0')
        else :
            if self.__label__()== '+':
                if self.nb_children()==2:
                    return Tree('+', (self.child(0)).deriv(r), (self.child(1)).deriv(r))
                else:
                    return Tree('+', (self.child(0)).deriv(r), Tree('+', *(self.children()[1,:]).deriv(r)))
            if self.__label__()=='*':
                if self.nb_children()==2:
                    return Tree('+', Tree('*', self.child(0).deriv(r), self.child(1)), Tree('*', self.child(0), self.child(1).deriv(r)))
                else:
                    return Tree('*', self.child(0), Tree('*', *(self.children()[1,:]).deriv(r)))
        return Tree('0')
                
if __name__ == "__main__":
    tree=Tree('*', Tree('1'), Tree('2'), Tree('5'))
    compare=Tree('3', Tree('2'), Tree('1'), Tree('5'))
    teste=Tree('+', Tree('X'), Tree('1'))
    test2=Tree('*', Tree('X'), Tree('5'))
    print(type(tree.__label__())==str)
    print(tree.__str__())
    print(tree.nb_children())
    print(tree.depth())
    print(tree.strexo4())
    print(tree.__eq__(compare))
    print((teste.deriv('X')).strexo4())
    print((test2.deriv('X')).strexo4())
    
    

        
        


    


        
            
            
        
    
