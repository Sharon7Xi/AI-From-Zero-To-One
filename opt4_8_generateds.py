#coding:utf-8
#0导入模块，生成数据集
import tensorflow as tf 
import matplotlib.pyplot as plt
import numpy as np
seed=2
def generateds():
	#基于seed产生随机数
	rdm=np.random.RandomState(seed)
	#随机数返回300行2列的矩阵，表示300组坐标点（x0,x1)作为输入数据集，randn表示X中的元素都是属于0到1之间 前闭后开符合正态分布的数值
	X=rdm.randn(300,2)
	#定义坐标平方和小于2的赋值1，其他赋值为0作为标准答案
	Y_=[int(x0*x0+x1*x1<2) for (x0,x1) in X]
	#遍历Y_中的每个元素，值为1的点标为红色，不为1标为蓝色，把颜色值赋值给Y_c
	Y_c=[['red' if y else 'blue'] for y in Y_]

	#对数据集X和标签Y_整理形状，把X整理为n行2列，两列分别表示横坐标和纵坐标，Y_的一列数分别表示每个点的横纵坐标是不是平方和小于2
	X=np.vstack(X).reshape(-1,2)
	Y_=np.vstack(Y_).reshape(-1,1)
	return X,Y_,Y_c

#print X
#print Y_
#print Y_c
#用plt.scatter画出数据集X各行中，第0个元素和第1个元素的点，即各行的（x0,x1),用各行Y_c对应的值表示颜色
#plt.scatter(X[:,o],X[:,1],c=np.squeeze(Y_c))
#plt.show()
