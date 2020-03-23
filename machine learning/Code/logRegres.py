#-*- coding :utf-8 -*-


from numpy import *;#导入numpy的库函数
import numpy as np; #这个方式使用numpy的函数时，需要以np.开头
import matplotlib.pyplot as plt
plt.rcParams['axes.unicode_minus'] = False #坐标轴显示负号

#打开文件并按行读取，提取x1,x2,x0默认为1.0，第三个值是类别标签
def loadDataSet():
	dataMat = [];labelMat = []  #定义列表
	fr = open('testSet.txt')   #打开文件
	for line in fr.readlines():  #按行读取
		lineArr = line.strip().split()
		dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])  #append是添加数组元素
		labelMat.append(int(lineArr[2]))
	return dataMat,labelMat

#sigmoid函数
def sigmoid(inX):
	return 1.0/(1 + exp(-inX))

#梯度上升优化算法
def gradAscent(dataMatIn,classLabels):
	dataMatrix = mat(dataMatIn)   #将一个二位列表转换为numpy矩阵
	labelMat = mat(classLabels).transpose()   #转换成矩阵然后转置
	m,n = shape(dataMatrix)  #矩阵大小
	alpha = 0.001   #初始化步长
	maxCycles = 500   #迭代次数
	weights = ones((n,1))   #生成一个n*1的元素全部为1的矩阵
	for k in range(maxCycles):  #迭代
		h = sigmoid(dataMatrix * weights)  #h是一个列向量  100*3   *   3*1   =   100*1
		error = (labelMat - h)
		weights = weights + alpha * dataMatrix.transpose() * error
	return weights



# dataArr,labelMat = loadDataSet()
# print(gradAscent(dataArr,labelMat))


#画决策边界
def plotBestFit(weights):
	dataMat,labelMat = loadDataSet()
	dataArr = array(dataMat)  #转换成数组，有三个值，x0 = 1.0,x1和x2
	n = shape(dataArr)[0]  #shape(dataArr)返回两个值（m,n），代表矩阵或者数组维数，这里n=100
	xcord1 = [];ycord1 = []
	xcord2 = [];ycord2 = []
	for i in range(n):  #提取x1,x2
		if int(labelMat[i]) == 1:#如果标签大于0.5，即取整后为1
			xcord1.append(dataArr[i,1]);ycord1.append(dataArr[i,2])  #添加dataArr数组
		else:
			xcord2.append(dataArr[i,1]);ycord2.append(dataArr[i,2])

	fig = plt.figure()  #画布层Figure（可指定画布属性，大小、清晰度等）
	ax = fig.add_subplot(111)  #subplot是子图，“111”表示“1×1网格，第一子图”，“234”表示“2×3网格，第四子图”
	ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')  #散点图
	ax.scatter(xcord2, ycord2, s=30, c='green')
	x = arange(-3.0, 3.0, 0.1)   #x坐标，arrange(start, end, step):起始值，结束值，步长
	y = (-weights[0]-weights[1]*x)/weights[2]  #y坐标
	ax.plot(x, y)
	plt.xlabel('X1'); plt.ylabel('X2');  #横纵坐标
	plt.show()


# dataArr,labelMat = loadDataSet()
# weights = gradAscent(dataArr,labelMat)
# print(plotBestFit(weights.getA()))


#随机梯度上升算法
def stocGradAscent(dataMatrix, classLabels, numIter=150):  #dataMatrix参数是numpy数组，classLabels是元组
	m,n = shape(dataMatrix) #返回数组的大小
	weights = ones(n) #生成[1,1,1]
	for j in range(numIter):
		dataIndex = list(range(m))  #必须加list()，m是实例的个数，dataIndex是实例的编号
		for i in range(m):
			alpha = 4/(1.0+j+i)+0.0001  #每次迭代步长都要变化
			randIndex = int(random.uniform(0,len(dataIndex)))  #在0——m中随机选取一个数，random.uniform（）返回的是浮点数，要加int强制转换 
			h = sigmoid(sum(dataMatrix[randIndex]*weights))   #在numpy数组中sum是求和，如sum([1,2,3]) = 6  具体介绍在https://www.cnblogs.com/rainsoul/p/11051827.html和https://blog.csdn.net/A1518643337/article/details/78223111
			error = classLabels[randIndex] - h  #h是一个数，classLabels[randIndex]也是数
			weights = weights + alpha * error * dataMatrix[randIndex]
			del(dataIndex[randIndex])  #删除已经遍历过的实例
	return weights



dataArr,labelMat = loadDataSet()
weights = stocGradAscent(array(dataArr),labelMat)
print(plotBestFit(weights))
