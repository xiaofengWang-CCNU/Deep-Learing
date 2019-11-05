#-*- coding :utf-8 -*-
#pip更新python -m pip install --upgrade pip
#总得来说，Matplotlib绘图过程无非几步：
# 1. 准备数据
# 2. 创建画布
# 3. 绘制图像（根据不同图像类别调用不同方法）
# 4. 辅助绘制（刻度、图例等）
# 5. 图像显示/保存

import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']  #为了显示中文，调用系统字体

decisionNode = dict(boxstyle = "sawtooth",fc = "0.8")
leafNode = dict(boxstyle = "round4",fc = "0.8")
arrow_args = dict(arrowstyle = "<-")

def plotNode(nodeTxt,centerPt,parentPt,nodeType):
	createPlot.axl.annotate(nodeTxt,xy = parentPt,\
		xycoords = 'axes fraction',
		xytext = centerPt,textcoords = 'axes fraction',\
		va = "center",ha = "center",bbox = nodeType,arrowprops = arrow_args)

# def createPlot(inTree):
	
# 	fig = plt.figure(1,facecolor = 'white')
# 	fig.clf()
# 	axprops = dict(xticks=[],yticks=[])
# 	createPlot.axl = plt.subplot(111,frameon = False,**axprops)
# 	plotTree.totalW = float(getNumLeafs(inTree))
# 	plotTree.totalD = float(getTreeDepth(inTree))
# 	plotTree.xOff = -0.5/plotTree.totalW; plotTree.yOff = 1.0;
# 	plotTree(inTree, (0.5,1.0),'')
  
# 	# plotNode('决策节点',(0.5,0.1),(0.1,0.5),decisionNode)
# 	# plotNode('叶节点',(0.8,0.1),(0.3,0.8),leafNode)
# 	plt.show()



def getNumLeafs(myTree):
	numLeafs = 0 
	firstStr = list(myTree.keys())[0] 
	secondDict = myTree[firstStr] 
	for key in secondDict.keys():
		if type(secondDict[key]) == dict:
			numLeafs += getNumLeafs(secondDict[key])
		else:
			numLeafs +=1 
	return numLeafs
def getTreeDepth(myTree):
	maxDepth = 0 
	firstStr = list(myTree.keys())[0] 
	secondDict = myTree[firstStr] 
	for key in secondDict.keys():
		if type(secondDict[key]) == dict:
			thisDepth = 1 + getTreeDepth(secondDict[key])
		else:
			thisDepth = 1 
		if thisDepth > maxDepth:
			maxDepth = thisDepth 
	return maxDepth



def retrieveTree(i):
	listOfTrees =[{'no surfacing':{0:'no',1:{'flippers': \
	                {0:'no',1:'yes'}}}}, 
	              {'no surfacing':{0:'no',1:{'flippers': \
	                {0:{'head':{0:'no',1:'yes'}},1:'no'}}}} 
	              ]
	return listOfTrees[i] 



def plotMidText(cntrPt, parentPt, txtString):
	xMid = (parentPt[0] - cntrPt[0])/2.0 + cntrPt[0]
	yMid = (parentPt[1]-cntrPt[1])/2.0 + cntrPt[1] 
	createPlot.axl.text(xMid, yMid, txtString)

def plotTree(myTree, parentPt, nodeTxt):
	numLeafs = getNumLeafs (myTree) 
	depth = getTreeDepth(myTree) 
	firstStr = list(myTree.keys())[0]
	cntrPt = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW,\
	 plotTree.yOff)
	plotMidText(cntrPt, parentPt, nodeTxt) 
	plotNode(firstStr, cntrPt, parentPt, decisionNode) 
	secondDict = myTree[firstStr] 
	plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD 
	for key in secondDict.keys():
		if type(secondDict[key]) == dict:
			plotTree(secondDict[key],cntrPt,str(key)) 
		else:
			plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW 
			plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), \
				cntrPt, leafNode)
			plotMidText((plotTree.xOff, plotTree.yOff),cntrPt, str(key)) 
	plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD



def createPlot(inTree):
	
	fig = plt.figure(1,facecolor = 'white')
	fig.clf()
	axprops = dict(xticks=[],yticks=[])
	createPlot.axl = plt.subplot(111,frameon = False,**axprops)
	plotTree.totalW = float(getNumLeafs(inTree))
	plotTree.totalD = float(getTreeDepth(inTree))
	plotTree.xOff = -0.5/plotTree.totalW; plotTree.yOff = 1.0;
	plotTree(inTree, (0.5,1.0),'')
  
	# plotNode('决策节点',(0.5,0.1),(0.1,0.5),decisionNode)
	# plotNode('叶节点',(0.8,0.1),(0.3,0.8),leafNode)
	plt.show()
