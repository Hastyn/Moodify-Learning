# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 19:40:29 2021

@author: Doshi
"""
import random
import matplotlib.pyplot as plt
import numpy as np

x=np.zeros([100,150])

x[49][74]=1


n=0

num_ones=[]
diff=[]

def swap():
    for i in range(8):
        r1=random.randint(0,99)
        c1=random.randint(0,149)
        r2=random.randint(0,99)
        c2=random.randint(0,149)
        p = x[r1][c1]
        x[r1][c1] = x[r2][c2]      
        x[r2][c2] = p
    
def first_neighbour(x1,y1):
    
    list=[]
    for i in range(x1-1,x1+2):
        if i>=0 and i<=99 and (y1-1)>=0 and (y1-1)<=149 :
           list.append([i,y1-1]) 
        if i>=0 and i<=99 and (y1+1)>=0 and (y1+1)<=149 :   
           list.append([i,y1+1])
    if y1-1>=0:
        list.append([x1,y1-1])
    if y1+1<=149 :
        list.append([x1,y1+1])
            
    return list 

def second_neighbour(x1,y1):
    
    
    list=[]
    for i in range(x1-2,x1+3):
        if i>=0 and i<=99 and (y1-1)>=0 and (y1-2)<=149 :
           list.append([i,y1-2]) 
        if i>=0 and i<=99 and (y1+1)>=0 and (y1+2)<=149 :   
           list.append([i,y1+2])
    
    for i in range(x1-2,x1+3,4):
        if i>=0 and i<=99 and (y1-1)>=0 and (y1-1)<=149 :
           list.append([i,y1-1]) 
        if i>=0 and i<=99 :
           list.append([i,y1])
        if i>=0 and i<=99 and (y1+1)>=0 and (y1+1)<=149 :   
           list.append([i,y1+1])
    
    return list 


def modify(x1,y1):
    firstneighbour=first_neighbour(x1,y1)
    for i in firstneighbour :
        if random.random()<0.25 :
            x[i[0]][i[1]]=1
    
    secondneighbour=second_neighbour(x1, y1)
    for i in secondneighbour :
        if random.random()<0.08 :
            x[i[0]][i[1]]=1
            
            
while 1<2 :
    swap()
    k=0
    s=set()
    for i in range(0,100) :
        for j in range(0,150) :
            if(x[i][j]==1) :
                s.add((i,j))
                k=k+1
    num_ones.append(k);            
    for q in s:
        modify(q[0],q[1])
    k=0    
    s2=set()
    for i in range(0,100) :
        for j in range(0,150) :
            if(x[i][j]==1) :
                s2.add((i,j))
                k=k+1  
    diff.append(k-num_ones[n])  
    n=n+1
    
    if num_ones[n-1]==15000:
        break

plt.plot(num_ones)
plt.xlabel("No of iterations")
plt.ylabel("Number of ones")
plt.show()

plt.plot(diff)
plt.xlabel("No of iterations")
plt.ylabel("change in number of ones")
plt.show()







