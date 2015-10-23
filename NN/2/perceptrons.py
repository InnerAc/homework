#coding:utf-8
#InnerAc
#perceptrons.py
import numpy as np
from numpy import random

hardlims = lambda x: 1 if x >= 0 else -1
hardlim = lambda x: 1 if x >= 0 else 0

def compareMatrix(a,b):
	(m,n) = a.shape
	for i in range(m):
		for j in range(n):
			e = a[i,j] - b[i,j]
			if(e > 0.01):
				print a[i,j], '-', b[i,j],'=',e
				return True
	return False

'''
n 神经元个数
i 输入维数
f 传输函数类型
p,t 训练集	（i*1, n*1）
W 权值	(n * i)
b 偏置值	(n * 1)
'''
def learning(n,i,f,p,t,W,b):
	W = np.matrix(W)
	b = np.matrix(b)
	num = len(p)
	W_tmp = W
	b_tmp = b
	i = 0
	while(i < num):
		pi = np.matrix(p[i]).T
		a = W * pi + b
		(x,y) = a.shape
		for k in range(x):
			for j in range(y):
				a[k,j] = hardlim(a[k,j])
		e = t[i] - a
		W = W + e * pi.T
		b = b + e
		i += 1
		if(i == num):
			# if(compareMatrix(W,W_tmp)):
			if(~(W==W_tmp).all()):
				i %= num
			# if(compareMatrix(b,b_tmp)):
			if ~(b==b_tmp).all():
				i %= num
		W_tmp = W
		b_tmp = b
	print W,b
		
	
if __name__ == '__main__':
	n = 1
	i = 3
	p = [[1,-1,-1],[1,1,-1]]
	t = [[0],[1]]
	f = 'hardlim'
	W = random.random(size=(n,i))
	b = random.random(size=(n,1))
	# W = [0.5, -1, -0.5]
	# b = [0.5]
	learning (n,i,f,p,t,W,b)