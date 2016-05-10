#!/bin/python
import sys
L=[[9,1,8,5],[2,7,3,11],[6,4,5,14]]
G=list()
for i in xrange(len(L)):
	G.extend(L[i])
G.sort()
Final=list()
for i in xrange(0,len(G),len(L[0])):
	Final.append(G[i:i+len(L[0])])
print Final	
		
