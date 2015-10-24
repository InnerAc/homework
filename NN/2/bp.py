#coding:utf-8
#InnerAc
#bp.py
import numpy as np
from numpy import random

lhardlims = lambda x: 1 if x >= 0 else -1
lhardlim = lambda x: 1 if x >= 0 else 0

def hardlim(a,b):
	(x,y) = a.shape
	for k in range(x):
		for j in range(y):
			a[k,j] = lhardlim(a[k,j]-b)
	return a

# 第一层网络 计算出 a|b
# 输出[a,b,a|b]
def first(p):
	p = np.matrix(p).T
	W = np.matrix([[1,0],[0,1],[1,1]])
	a = W * p
	a = hardlim(a,1)
	return second(a)
# 第二层网络 计算出 a&b
# 输出 [a|b,a&b] 
def second(p):
	W = np.matrix([[1,1,0],[0,0,2]])
	a = W * p
	a = hardlim(a,2)
	return third(a)
# 第三层网络 计算出a^b
# 输出 a^b
def third(p):
	W = np.matrix([-1,1])
	a = W * p
	return a[0,0]
if __name__ == '__main__':
	p = [[0,0],[0,1],[1,0],[1,1]]
	for pi in p:
		print pi,first(pi)