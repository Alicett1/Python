# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:57:42 2024

@author: Alice
"""

from tkinter import *
from tkinter import ttk
from random import randrange as rd


root=Tk()
window=Frame(root)
window.grid()


def cercle():
    for i in range(7):
        L=canvas.create_oval(20+i*30, 20+30*i, 380-i*30, 380-i*30, outline='red', fill='ivory')
        if i==4:
            L=canvas.create_oval(20+i*30, 20+30*i, 380-i*30, 380-i*30, outline='red', fill='red')
    return L

def texte():
    for i in range(7):
        txt = canvas.create_text(190, 200-34*i, text=6-i, fill="red")
        if i==1:
            txt = canvas.create_text(190, 200-34*i, text=6-i, fill="ivory")
    return txt


total = 0
count=0  
        
            
def tir(canvas, n):
    global total
    global count  #permet de modifier un paramètre de façon globale
    shoots=n
    while count<5 and shoots>0:
        i=rd(0,400)
        j=rd(0,400)
        o=canvas.create_oval(i, j, i+20, j+20, fill='black')
        total+=score(i,j)
        count+=1
        shoots-=1
    label["text"] = f"Score: {total}" #permet de modifier directement le label
    if count==5:
         b["state"] = "disabled"



def score(x,y):
    scoretotal=0
    dist = ((x-200)**2 + (y - 200)**2)**0.5
    if dist<30:
        scoretotal+=6
    if dist>30 and dist<60:
        scoretotal+=5
    if dist<90 and dist>60:
        scoretotal+=4
    if dist<120 and dist>90:
        scoretotal+=3
    if dist<150 and dist>120:
        scoretotal+=2
    if dist<180 and dist>150:
        scoretotal+=1
    return scoretotal


def uniquetir(event, canvas):
    if event.char == "f":
        tir(canvas, 1)
    



    
    
    
if __name__ == "__main__":   

    #Trace la cible    
    canvas = Canvas(window, width=400, height=400, background='red')
    oval=cercle()
    nbres=texte()
    ligne1 = canvas.create_line(200, 0, 200, 400, fill='red')
    ligne2 = canvas.create_line(0, 200, 400, 200, fill='red')
    
    #Commande les boutons et les place
    b = Button(root, text='Feu!', command= lambda :tir(canvas, 5), name='fire_all')  # on utilise lambda pour appeler la fonction en précisant le paramètre
    b1 = Button(root, text='Quitter', command=window.destroy)
    canvas.grid(row=0, column=0, columnspan=3)
    b.grid(row=1, column=0, sticky=W)
    b1.grid(row=1, column=2, sticky=E)
    
    #Construit le score
    label = Label(window, text="Score: 0", name="score")
    label.grid(row=1, column=1, sticky=W) #permet d'afficher le label et de le placer
    
    
    #Construit le tir unique en appuyant sur 'f' par un event
    root.bind("<Key>",lambda event : uniquetir(event, canvas))
    root.mainloop() #comme j'ai mis root avant je suis obligée de mettre root ici pour relier les deux

