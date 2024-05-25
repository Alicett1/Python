# -*- coding: utf-8 -*-
"""
Created on Wed May 22 09:50:50 2024

@author: Alice
"""
from tkinter import *
from tkinter import ttk
import random as rd


graph = [[2, 7], [3], [5, 8], [10], [3, 1], [], [3, 10, 4], [], [], [10, 1], [3, 1], [0]]

pos = ([131, 352], [464, 315], [254, 211], [393, 346], [381, 432],
[343, 98], [298, 326], [187, 475], [245, 407], [483, 212], [365, 216],
[149, 198])

COLORS = ['antiquewhite', 'aqua', 'aquamarine', 'bisque', 'black',
'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse',
'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan',
'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgrey',
'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen']


root=Tk()
window=Frame(root)
window.grid()

    
def draw(can, graph, pos, color):
    canvas.delete("all")
    for i in range(len(graph)):
        for j in graph[i]: # sucs de i a j
            can.create_line(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
        x, y = pos[i]
        can.create_oval(x-4,y-4,x+4,y+4,fill= color[i])
        can.create_text(x-8, y, text=f"{i}")

        
graph0 = [[2], [], [4], [1], [6], [3], [7], [5]]
pos0 = [[100, 200], [450, 200], [150, 200], [400, 200], [200, 200],
[350, 200], [250, 200], [300, 200]]

mini=0
        
def min_local(i, graph, composante, pos, can):
    global mini
    for h in graph[i]:
        mini=composante[i]
        if composante[h]< mini:
            mini=composante[h]
    for k in range(len(graph)):
        if i in graph[k] and composante[k]<mini: #ne reconnait pas mini car pas dans la même boucle donc doit déf globale
            mini=composante[k]
    for h in graph[i]:
        composante[h]=mini
    for k in range(len(graph)):
        if i in graph[k]:
            composante[k]=mini
    composante[i]=mini
    draw(can, graph, pos, composante)
        
        
            
            
#Q3 : On étend le principe de l'exo 2 à tous les sommets du graphe et s'ils ont tous la même couleur, on peut former un même groupe

def connexe(graph, composante, pos, can):
    for i in range(len(graph)):
        min_local(i, graph, composante, pos, can)
        
        
        
def color_generator():
    r, g, b = rd.randint(0,255), rd.randint(0,255), rd.randint(0,255)
    return f"#{r:02x}{g:02x}{b:02x}"
  
i=0
j=0

def listecolors():
    listcolors=[color_generator() for n in range(1600)]
    return listcolors


def creategraph(can):
    can.delete("all")
    D={}
    pos=[[] for n in range(1600)]
    G=[[] for n in range(1600)]
    global COLORS
    global i
    global j
    n=0
    for x in range(0, 800, 20):
        for y in range(0,800, 20):
            if i==40:
                i=0
                j+=1
            pos[n]=[x,y]
            n=n+1
            i+=1
            can.create_oval(x-4,y-4,x+4, y+4, fill= color_generator())
            D[(i,j)]=[]
    for (k,m) in D:
        l=rd.random()
        n=rd.random()
        if l > 0.6:
            D[(k,m)].append((k+1,m))
        if n > 0.6:
            D[(k,m)].append((k,m+1))
    print(D)
    h=0
    o=0
    for (k,m) in D:
        o+=1
        if (k+1,m) in D[(k,m)]:
                can.create_line(k*20, m*20, (k+1)*20, m*20)
                G[k*m].append((k+1)*m)
        elif (k,m+1) in D[(k,m)]:
            can.create_line(k*20, m*20, k*20, (m+1)*20)
            G[k*m].append((m+1)*k)
    connexe(G, listecolors(), pos, canvas)
            
    
            

canvas= Canvas(window, width=800, height=800, background ='white')
draw(canvas, graph, pos, COLORS) #q1
draw(canvas, graph0, pos0, COLORS) #q2
min_local(4, graph0, COLORS, pos0, canvas) #q2
connexe(graph, COLORS, pos, canvas) #q3
creategraph(canvas)
print(listecolors())





canvas.pack()

root.mainloop()