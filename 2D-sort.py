#!/bin/python

def sort_2D(L):
	G=list()
	for i in xrange(len(L)):
		G.extend(L[i])		# Store as 1-D
	G.sort()			
	Final=list()
	for i in xrange(0,len(G),len(L[0])):
		Final.append(G[i:i+len(L[0])])		# Store back as 2-D
	return Final	
		
