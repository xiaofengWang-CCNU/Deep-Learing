# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
plt.rcParams['axes.unicode_minus'] = False #坐标轴显示负号
plt.rcParams['font.sans-serif'] = ['simhei']
from numpy import *
import numpy as np #linspace引用
#from math import pi, cos, sin#在这里不可用，会与numpy库的相冲突

#初识画图
#fig = plt.figure()
#sub = fig.add_subplot(111)#子图
#x = linspace(-2 *pi,2 * pi,200) #从-2*pi到2*pi中取200个返回的是数组
#sub.plot(x,sin(x))
#
#samples = x[::4]  #每隔4个取一个值
#sub.plot(samples,sin(samples),'r*')#r*表示红色星标，以星标代替直线
#
#plt.title('sin()函数及一些绘制的点')
#plt.xlabel('x')#横坐标
#plt.ylabel('sin(x)')
#plt.show()
#grid()#绘制网格线


#曲线拟合函数和求值函数，axis和legend函数
#x = range(5)
#y = [1,2,1,3,5]
#p2 = polyfit(x,y,2)#返回2次拟合后多项式系数，从高次到低次依次存放在p2中，函数的功能是将x和y拟合，就是将点连起来
#p4 = polyfit(x,y,4)#曲线拟合函数返回拟合4次后多项式系数，从高次到低次依次存放在p4中
#
#xx = linspace(-1,5,200)
#plt.plot(xx,polyval(p2,xx),label = 'fitting polynomial of degree 2')#求值函数返回当x = xx时的值
#plt.plot(xx,polyval(p4,xx),label = 'interpolating polynomial of degree 4')
#plt.plot(x,y,'r*')#绘制x和y以*
#
#plt.xlabel('x')#横坐标
#plt.ylabel('sin(x)')
#
#plt.axis([-1,5,0,6])#横纵坐标范围
#plt.legend(loc = 'upper left',fontsize = 'small')#标签位置



#散点图
#x1 = 2*np.random.standard_normal((2,100))#返回标准正太分布的随机样本的数组，由2个含100个元素的数组组成的二维数组
#x2 = 0.8*np.random.standard_normal((2,100)) + array([[6],[2]])#必须是元组的形式，才会返回多维数组
#x2 = numpy.random.rand()
#x2 = numpy.random.rand(2)
#print(x1)
#
#
#plt.scatter(x1[0],x1[1],s = 30,c = 'red',marker = 's')
#plt.scatter(x2[0],x2[1],s = 30,c = 'blue')
##plot(x1[0],x1[1],'r*')
##plot(x2[0],x2[1],'b*')


#loglog函数
#x = np.linspace(0,10,200)
#plt.loglog(x,2*x**2,label = 'quadratic polynomial',linestyle = '--',color = 'green',linewidth = 3)
#plt.loglog(x,4*x**4,label = '4th degree polynomial',linestyle = '-.',color = 'red',linewidth = 3)
#plt.loglog(x,5*exp(x),label = 'exponential function',color = 'blue',linewidth = 3)
#plt.legend(loc = 'best')
#plt.title('对数图')
#plt.show()


#绘图中重要变量
#k = 0.2
#x = [sin(2*n*k) for n in range(20)]
#plt.plot(x,linestyle = 'dashed',color = 'red',marker = 'o',markerfacecolor = 'blue'
#     ,markersize = 12,linewidth = 6)
#plt.plot(x,'ro-',markerfacecolor = 'blue'
#     ,markersize = 12,linewidth = 6)


#直方图
#sigma,mu = 2,10
#x = sigma*np.random.standard_normal(1000)+mu#返回1000个随机数存放在数组中
##print(x)
#plt.hist(x,50,normed = 10)#normed指条状图密度
#z = linspace(0,20,200)
#plt.plot(z,(1/sqrt(2*pi*s**2))*exp(-(z-mu)**2/(2*s**2)),'g')#正态分布
#plt.title(r'Hist with: $\mu = 10$,$\sigma = 2$')#r如何表示mu和sigma



#subplot子图
#def avg(x):
#    return (roll(x,1) + x + roll(x,-1))/3
#
#x = np.linspace(-2 * pi,2 * pi,200)
#y = sin(x) + 0.4 * np.random.rand(200)#使用方法与np.random.randn()函数相同  
#                                      #通过本函数可以返回一个或一组服从“0~1”均匀分布的随机样本值。随机样本取值范围是[0,1)，不包括1。
#
#for i in range(3):
#    plt.subplot(3,1,i+1)
#    plt.plot(x,y,label = '{:d} average{}'.format(i,'s' if i>1 else ''))
#    plt.yticks([])#xticks( arange(5), (‘Tom’, ‘Dick’, ‘Harry’, ‘Sally’, ‘Sue’) )
#                  #用’Tom’, ‘Dick’, ‘Harry’, ‘Sally’, 'Sue’作为[0,1,2,3,4]位置显示的label。
#    plt.legend(loc = 'lower left',frameon = False)
#    y = avg(y)
#    
#plt.subplots_adjust(hspace = 0.7)#调整两个子图之间的距离



#面向对象画图，即使用子图

fig = plt.figure(1,figsize = (10,6),dpi = 80)
ax = fig.add_subplot(111)
#x = linspace(-1 * pi,1 * pi,200,endpoint = True)#endpoint包含端点
#ax.plot(x,sin(x),linestyle = '-.',linewidth = '2',label = 'sin(x)',color = 'blue')
#ax.plot(x,cos(x),linestyle = '--',linewidth = '2',label = 'cos(x)',color = 'green')
#
#amod_sin = lambda x:(1.0-0.1*sin(25 * x))*sin(x)
#ax.plot(x,amod_sin(x),label = 'modsin',color = 'red')
#ax.legend(loc = 'upper left')
#
#plt.yticks([-1,1],[r'$-1$',r'$1$'])#两种方式
#ax.set_xticks([-pi,-pi/2,0,pi/2,pi])
#ax.set_xticklabels(('-$\pi$','$-\pi/2$','$0$','$\pi/2$','$\pi$'))


x = linspace(-10,10,500)
y = 1.0/(1+exp(-x))
ax.plot(x,y,label = 'sigmoid')
ax.legend('upper left')

ax.spines['right'].set_color('none')#调整坐标轴为无色或者移动位置
ax.spines['top'].set_color('none')#left   bottom
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))




    









