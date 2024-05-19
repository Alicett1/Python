# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:53:18 2024

@author: Alice
"""

from tkinter import *
from tkinter import ttk
import numpy as np
import random as rd


root=Tk()
window=Frame(root)
window.grid()

    
def draw(can, graph, pos):
    for i in range(len(graph)):
        for j in graph[i]: # sucs de i a j
            can.create_line(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
    for (x, y) in pos:
        can.create_oval(x-4,y-4,x+4,y+4,fill="#f3e1d4")
        
'''def vect(pos1, pos2):
    module=np.sqrt((pos1[0]-pos2[0])^2+(pos1[1]-pos2[1])^2)
    vecteur=(abs(pos1[0]-pos2[0]), abs(pos1[1]-pos2[1]))
    return module, vecteur'''
    

'''def deplacement(event):
    
    
    if event.char == "f":
        draw(canvas, graph, bouger(graph, pos, k, tau))'''
        
        
def bouger(event):
    vit = np.array([((rd.random()-0.5)*10, (rd.random()-0.5)*10) for i in range(len(graph))])
    tau=0.1
    k=1
    t=10
    cx=200  #position du centre de la fenêtre
    cy=200
    if event.char == "f":
        canvas.delete("all")
        for i in range(len(graph)):
            cx+=pos[i][0]
            cy+=pos[i][1]
            c=(cx/len(graph), cy/len(graph))
            for j in graph[i]:
                Fx=-k*abs(pos[i][0]-pos[j][0])+t*c[0]
                Fy=-k*abs(pos[i][1]-pos[j][1])+t*c[1]
                vit[i][0]+=tau*Fx
                vit[i][1]+=tau*Fy
                pos[i][0]+=vit[i][0]*tau
                pos[i][1]+=vit[i][1]*tau
                
    draw(canvas, graph, pos)
                     

    
    
    
#Trace les sommets
graph = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0],
[3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]

width= 400
height= 400
pos = np.array([(rd.uniform(0, width), rd.uniform(0, height)) for i in range(len(graph))])

canvas= Canvas(window, width=400, height=400, background ='white')
draw(canvas, graph, pos)

canvas.pack()

root.bind("<Key>",lambda event : bouger(event))

root.mainloop()