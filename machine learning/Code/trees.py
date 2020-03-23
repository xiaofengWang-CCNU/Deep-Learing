#-*- coding : utf-8 -*-

#reload是要这样  ：import importlib
#import trees
#importlib. reload('trees')
#独立窗口输出 %matplotlib qt5

from math import log
import operator
import treePlotter


#计算信息熵
def calcShannonEnt(dataSet):
	numEntries = len(dataSet)  #数据集中样本实例个数
	labelCounts = {}
	for featVec in dataSet:  #提取数据集中的每一条实例
		currentLabel = featVec[-1]  #取最后的决策结果，就是yes or no
		if currentLabel not in labelCounts:  #不可写为labelCount.key()
			labelCounts[currentLabel] = 0  #添加键并赋值value为0
		labelCounts[currentLabel] +=1   #value加一
	shannonEnt = 0.0  #初始化
	for key in labelCounts:
		prob = float(labelCounts[key])/numEntries  #求p
		shannonEnt -= prob * log(prob,2)   #求信息熵
	return shannonEnt



#创建数据集
def creatDataSet():
	dataSet = [[1,1,'yes'],
	           [1,1,'yes'],
	           [1,0,'no'],
	           [0,1,'no'],
	           [0,1,'no']]
	labels = ['no surfacing','flippers']

	return dataSet,labels


#划分数据集  axis为特征
def splitDataSet(dataSet,axis,value):
	retDataSet = []   #创建列表
	for featVec in dataSet:
		if featVec[axis] == value:  #如果特征值等于value
			reducedFeatVec = featVec[:axis]  #提取axis之前的所有元素
			reducedFeatVec.extend(featVec[axis+1:])  #提取axis之前的所有元素，不包括axis，注意extend与append区别
			retDataSet.append(reducedFeatVec)   #将提取出的列表加入到retDataSet列表中，作为一个元素

	return retDataSet


#选择最佳划分属性
def chooseBestFeatureToSplit(dataSet):
	numFeatures = len(dataSet[0])-1   #最后一列为决策结果
	baseEntropy = calcShannonEnt(dataSet)  #划分前信息熵
	bestInfoGain = 0.0;bestFeature = -1
	for i in range(numFeatures):  #一列就代表一个特征
		featList = [example[i] for example in dataSet]  #取出数据集中的每一个实例中第i个特征的特征值
		uniqueVals = set(featList)  #集合中每个值互不相同，集合中存储的是第i个特征的所有互不相同的特征值
		newEntropy = 0.0
		for value in uniqueVals:
			subDataSet = splitDataSet(dataSet,i,value)  #将特征值为value的划分出来，以便计算划分后的信息熵
			prob = len(subDataSet)/float(len(dataSet))
			newEntropy += prob * calcShannonEnt(subDataSet)

		infoGain = baseEntropy - newEntropy
		if infoGain >bestInfoGain:
			bestInfoGain = infoGain
			bestFeature = i

	return bestFeature

#取出最多的
def majorityCnt(classList):
	classCount = {}
	for vote in classList:
		if vote not in classCount:
			classCount[vote] = 0
		classCount[vote] += 1

	sortedClassCount = sorted(classCount.items(),\
		key = operator.itemgetter(1),reverse = True)  #items() 方法是把dict对象转换成了包含tuple的list

	return sortedClassCount[0][0]

#创建树
def createTree(dataSet,labels):
	classList = [example[-1] for example in dataSet]  #取出所有的决策结果
	if classList.count(classList[0]) == len(classList):  #如果决策结果都一样，停止划分
		return classList[0]
	if len(dataSet[0]) == 1:  #遍历完所有的特征返回次数出现最多的结果
		return majorityCnt(classList)
	bestFeat = chooseBestFeatureToSplit(dataSet)  #最好的划分特征
	bestFaetLabel = labels[bestFeat]  #数字特征转换为文字特征
	myTree = {bestFaetLabel:{}}  #用字典存储决策树
	del(labels[bestFeat])  #删除已经分类过的特征
	featValues = [example[bestFeat] for example in dataSet] #提取最好划分特征的所有属性值
	uniqueVals = set(featValues)  #用集合存储属性值，不会重复
	for value in uniqueVals:
		subLabels = labels[:]  #复制特征标签，已经不是原始标签了，删除了已经划分过的特征
		myTree[bestFaetLabel][value] = createTree(splitDataSet\
			(dataSet,bestFeat,value),subLabels)  #递归，第一个参数是已经划分过的实例集

	return myTree



#使用决策树的分类函数,即测试,也是一个递归
def classify(inputTree,featLabels,testVec):
	firstStr = list(inputTree.keys())[0]
	secondDict = inputTree[firstStr]
	featIndex = featLabels.index(firstStr)
	for key in secondDict.keys():
		if testVec[featIndex] == key:
			if type(secondDict[key]) == dict:
				classLabel = classify(secondDict[key],featLabels,testVec)
			else:
				classLabel = secondDict[key]
	return classLabel



#存储决策树
def storeTree(inputTree,filename):
	import pickle
	fw = open(filename,'W')
	pickle.dump(inputTree,fw)
	fw.close()
#读取决策树
def gradTree(filename):
	import pickle
	fr = open(filename)
	return pickle.load(fr)

#读取文本
def file2matrix(filename):
    fr=open(filename)
    lists=fr.readlines()
    listnum=[]
    for k in lists:
        listnum.append(k.strip().split(','))  
    return listnum

#测试函数
def test():
    lenses=file2matrix('lenses1.txt')  #lenses.txt    car.data
    lensesLabels = ['age','prescript','astigmatic','tearRate']
#    lensesLabels = ['buying','maint','doors','persons','lug_boot','safety ']
    lensesTree=createTree(lenses,lensesLabels)
    return lensesTree


#treePlotter.createPlot(test())



#import importlib
#import trees
#import treePlotter
#lensesLabels = ['age','prescript','astigmatic','tearRate']
lensesLabels = ['buying','maint','doors','persons','lug_boot','safety ']
lenses = file2matrix('car.data')
lensesTree = createTree(lenses,lensesLabels)
treePlotter.createPlot(lensesTree)