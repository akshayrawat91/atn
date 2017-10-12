import random as rd
import networkx as nx
import matplotlib as mt
import matplotlib.pyplot as plt
import tkinter

#def nagamochiIbaraki():

def createGraph(n,edge):
    global adjList
    G = nx.Graph()
    g = G.gnm_random_graph(n,edge)
    nx.draw(g)
    plt.show()
    '''for i in range(n):
        for j in range(n):
            if i == j:
                adjList[i][j] = adjList[j][i] = 0
            else:
                x = rd.randint(0,1)
                if(x == 1):
                    adjList[i][j] = adjList[j][i] = adjList[i][j] + 1
                    
    '''


n = 19      # nodes are set to 19
for m in range(20, 168, 4):  # edges varies from 20 to 168 in steps of 4
    createGraph(n,m)
    #nagamochiIbaraki(X,n)
