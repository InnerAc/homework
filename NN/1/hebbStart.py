import hebb
import show
import numpy as np
if __name__ == '__main__':
	p = [-1,1,1,1,-1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, -1,-1,-1,-1,-1, -1,-1,-1,-1,-1, -1,-1,-1,-1,-1]
	# a = [-1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, -1]
	W = hebb.training()
	a = hebb.start(p,W)
	
	show.drawTwo(p,a)