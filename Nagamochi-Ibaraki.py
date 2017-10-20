# @author akshayrawat91
# finds the connectivity for a pseudo-random connected graph
# reference GUHAN1990 "Nagamochi-Ibaraki-Algorithm-Implementation" github

import random as rd
from networkx import *
import matplotlib.pyplot as plt
import numpy as np

# calculate the degree of node
def getDegree(adjList,n):
    return sum(adjList[n])

# helper function for MA to find the next node
def createList(adjList,list,n):
    s = set(list)
    sum2 = 0
    for i in range(n):
        sum1 = 0
        if(i in s): # ignore the node already in the set
            continue
        for j in s: # find the connected nodes to the set
            sum1 += adjList[i][j]
        if(sum2 < sum1):
            sum2 = sum1
            nextNode = i
    return nextNode # node with maximum adjacency to the set

# create a Maximum Adjacency list
def calcMA(adjList,n):
    v = rd.randint(0,n-1)   # select the first node at random
    list = [v]
    while(len(list) < n):
        list.append(createList(adjList,list,n)) # find the next node
    return list

# merge the nodes Vn-1 and Vn from the MA list in the original graph
def mergeNode(adjList,x,y,n):
    if(x < y):
        adjList = np.delete(adjList, y, 0)    # n terms
        adjList = np.delete(adjList, x, 0)
        ycol = adjList[:, y]
        xcol = adjList[:, x]
        adjList = np.delete(adjList, y, 1)    # n-2 terms
        adjList = np.delete(adjList, x, 1)
    else:
        adjList = np.delete(adjList, x, 0)    # n terms
        adjList = np.delete(adjList, y, 0)
        ycol = adjList[:, y]
        xcol = adjList[:, x]
        adjList = np.delete(adjList, x, 1)    # n-2 terms
        adjList = np.delete(adjList, y, 1)
    zcol = xcol + ycol  # resultant column with n-2 terms
    zcol = np.reshape(zcol,(1,n-2))
    adjList = np.concatenate((adjList,zcol.T),1)    # add the row by column transpose
    zcol = np.insert(zcol,n-2,0)    # insert a zero padding for n-1 terms
    zcol = np.reshape(zcol, (1, n-1))
    adjList = np.concatenate((adjList,zcol),0)  # add the column
    #print(adjList)
    return adjList

def nagamochiIbaraki(adjList,n):
    if(n == 2): # for n=2 calculate degree for x and y
        return getDegree(adjList, 0)
    list = calcMA(adjList,n)    # find the MA for adjacency list
    x = list[len(list) - 2]
    y = list[len(list) - 1]
    deg = getDegree(adjList,y)
    adjList_new = mergeNode(adjList,x,y,n)  # merge the nodes x and y
    return min(deg,nagamochiIbaraki(adjList_new,n-1))

# create a random connected graph using nodes and edges
def createGraph(n,edge):
    global adjList# adjacency List
    adjList = [[0 for col in range(n)] for row in range(n)] # creating a zero matrix of n*n
    gp = nx.dense_gnm_random_graph(n,edge)
    nx.draw(gp,with_labels=True)
    adjList = np.array(nx.to_numpy_matrix(gp))
    #print(adjList)
    return is_connected(gp)

    '''
    numRange = list(range(0,n))
    count = 0   # count the number of edgesNagamochi-Ibaraki.py:79
    for i in range(n):  # assign an edge for each node
        numRange = list(range(0,n))
        numRange.remove(i)
        j = rd.choice(numRange) # prevent self edges
        while (adjList[i][j] == 1): # prevent parallel edges
            numRange = list(range(0, n))
            numRange.remove(i)
            j = rd.choice(numRange)
        adjList[i][j] = adjList[j][i] = 1
        count = count + 1
    #print(count)
    while(count < edge):    # assign remaining edges at random till it reaches the limit
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
    '''
    '''x = 0
    for i in range(n):
        for j in range(n):
            print(adjList[i][j],end=" ")
            if(adjList[i][j] == 1):
                x+=1
        print()
    print(x/2)'''
    '''
    #print(type(adjList))
    adjList = np.array(adjList)
    G = nx.from_numpy_matrix(adjList) # create a graph from adjacency List
    #lt = adjList.T
    #sym = np.allclose(adjList,lt)
    #print(sym)
    #print(is_connected(G),count)
    if(is_connected(G) == False):   # checks if the graph is connected
        createGraph(n,edge)
    else:
        nx.draw(G,with_labels=True) # if connected draw and show the graph
        #plt.show()
        '''

# main method starting here
n = 19      # nodes are set to 19
lg = []     # array to store lambda
ed = []     # array to store edges
for m in range(20, 168, 4):  # edges varies from 20 to 168 in steps of 4
    i = 0
    avg = 0
    sm = 0
    while(i < 5):
        adjList = [[0 for col in range(n)] for row in range(n)]
        state = createGraph(n,m)
        if(state == False): # if the graph is disconnected lamdaG is zero and skip to next iteration
            i+=1
            sm+=0
            continue
        lambdaG = nagamochiIbaraki(adjList,n)
        sm+=lambdaG
        i+=1
    avg = int(sm/5)      # calculate the average
    lg.append(avg)  # add the average to the lg array
    ed.append(m)    # add the edge value to ed array
    print(avg)

#print(lg)
#print(ed)
plt.clf()
plt.plot(ed,lg,color = "purple", lw = 1, ls = '-',marker = 'o',markerfacecolor = 'red')
plt.xlabel('edges')
plt.ylabel('lamda(G)')
plt.show()

lgUnique = np.array(np.unique(lg)) # take unique values of lambda to calculate stability
st = []

for i in range(lgUnique.size):  # calculate stability for all lambda
    min1 = np.size(lg)
    max1 = 0
    for j in range(np.array(lg).size):
        if(lg[j] == lgUnique[i]):
            if(max1 < j):
                max1 = j
            if(min1 > j):
                min1 = j
    s = ed[max1]- ed[min1]
    st.append(s)

print(st)
print(lgUnique)

plt.clf()
plt.plot(lgUnique,st,color = "green", lw = 1, ls = '-',marker = 'o',markerfacecolor = 'red')
plt.xlabel('lambda(G)')
plt.ylabel('s(lambda)')
plt.show()
'''for i in range(n):zcol = np.reshape(zcol,(1,n-2))
        for j in range(n): 
            print(adjList[i][j], end=" ")
        print()'''

