import random
import networkx as nx

def createGraph(n,m):
    global adjList
    for i in range(n):
        for j in range(n):
            if i == j:
                adjList[i][j] = adjList[j][i] = 0
            else:



n = 19      # nodes are set to 19
for m in range(20, 168, 4):  # edges varies from 20 to 168 in steps of 4
    createGraph(n,m)
    nagamochiIbaraki(X,n)
