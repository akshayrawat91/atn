import random as rd
from networkx import *
import matplotlib as mt
import matplotlib.pyplot as plt
#import scipy as sp
import numpy as np
'''
def getDegree(adj,n):
    return adj[n]

def createList(list):
    s = set(list)
    lastNode = list[len(list) - 1]
    row = np.argmax(adj,axis=1)
    nextNode = row[lastNode]
    if(nextNode in s):

    return nextNode

def calcMA(adj,n):
    v = rd.randint(0,n-1)
    list = [v]
    while(len(list) < n):
        list.append(createList(list))
    return list

    row = np.argmax(adj,axis=1)
    v2 = row[v1]


def nagamochiIbaraki(adj,n):
    if(n == 2):
        return getDegree(adj, 0)
    list = calcMA(adj,n)
    v1 = list[len(list) - 2]
    v2 = list[len(list) - 1]

'''

def createGraph(n,edge):
    global adjList
    adjList = [[0 for col in range(n)] for row in range(n)]
    numRange = list(range(0,n))
    count = 0
    for i in range(n):
        numRange = list(range(0,n))
        numRange.remove(i)
        j = rd.choice(numRange)
        while (adjList[i][j] == 1):
            numRange = list(range(0, n))
            numRange.remove(i)
            j = rd.choice(numRange)
        adjList[i][j] = adjList[j][i] = 1
        count = count + 1
    #print(count)
    while(count < edge):
        numRange = list(range(0,n))
        i = rd.choice(numRange)
        numRange.remove(i)
        j = rd.choice(numRange)
        while(adjList[i][j] == 1):
            numRange = list(range(0,n))
            i = rd.choice(numRange)
            numRange.remove(i)
            j = rd.choice(numRange)
        adjList[i][j] = adjList[j][i] = adjList[i][j] + 1
        count = count + 1
    #print(count)
    '''x = 0
    for i in range(n):
        for j in range(n):
            print(adjList[i][j],end=" ")
            if(adjList[i][j] == 1):
                x+=1
        print()
    print(x/2)'''
    #print(type(adjList))
    G = nx.from_numpy_matrix(np.array(adjList))
    print(is_connected(G),count)
    if(is_connected(G) == False):
        createGraph(n,edge)
    else:
        nx.draw(G,with_labels=True)
        plt.show()




n = 19      # nodes are set to 19
for m in range(20, 32, 4):  # edges varies from 20 to 168 in steps of 4
    createGraph(n,m)
    #nagamochiIbaraki(adj,n)
    '''for i in range(n):
        for j in range(n):
            print(adjList[i][j], end=" ")
        print()'''

