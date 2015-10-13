#coding:utf-8
#InnerAc
import numpy as np
import show
hardlims = lambda x: 1 if x >= 0 else -1

# 开始训练，传入训练样本 list,返回权值矩阵
def training(inp,outp):
	# 初始化权值矩阵 W
	ze = np.zeros([30,30])
	W = np.matrix(ze)
	# 使用Hebb规则求权值矩阵
	n = len(inp)
	for i in range(n):
		pi = np.matrix(inp[i])
		po = np.matrix(outp[i])
		W += pi.T * po
	return W
# 开始测试，输入测试样例和权值矩阵,返回输出的矩阵并且转换为数组
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