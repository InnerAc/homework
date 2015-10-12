import numpy as np
import show
hardlims = lambda x: 1 if x >= 0 else -1

def training():
	p0 = np.matrix([-1,1,1,1,-1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, -1,1,1,1,-1])
	p1 = np.matrix([-1,1,1,-1,-1, -1,-1,1,-1,-1, -1,-1,1,-1,-1, -1,-1,1,-1,-1, -1,-1,1,-1,-1, -1,-1,1,-1,-1])
	p2 = np.matrix([1,1,1,-1,-1, -1,-1,-1,1,-1, -1,-1,-1,1,-1, -1,1,1,-1,-1, -1,1,-1,-1,-1, -1,1,1,1,1])
	W = p0.T * p0 + p1.T * p1 + p2.T * p2
	
	return W

def start(pt,W):
	pt = np.matrix(pt)
	
	n = pt * W

	n =  n.getA1()
	a = []
	for i in n:
		a.append(hardlims(i))
	return a

if __name__ == '__main__':
	
	W = training()	
	# print W
	test = [-1,1,1,1,-1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, -1,-1,-1,-1,-1, -1,-1,-1,-1,-1, -1,-1,-1,-1,-1]
	show.draw(test)
	pt = np.matrix(test)
	n = pt * W

	n =  n.getA1()
	a = []
	for i in n:
		a.append(hardlims(i))
	
	# a = np.matrix(a)
	
	show.draw(a)