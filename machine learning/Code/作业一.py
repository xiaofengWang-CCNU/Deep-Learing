#-*- coding: utf-8 -*-


#分别用递归法和非递归法求Fibonacci数列的前50位，并比较计算时间的差异.
#王小丰
#2019/10/21


# #递归方法
# def fibonacci(n):
# 	if n<=1:
# 		return 1
# 	else:
# 		return fibonacci(n-1)+fibonacci(n-2)

# for i,x in enumerate(list(range(50))):
# 	print(i,fibonacci(x))



# 非递归方法
# fib0,fib1 = 1,1
# for x in range(2,50):
# 	print(fib0, fib1)
# 	fib0 += fib1
# 	fib1 += fib0




#输入一个自然数(<90000),  分别用递归法和非递归法求其二机制表示.
#王小丰
#2019/10/21


# 递归方法
# n=int(input("please input a number(<90000):"))  #input输出的是字符
# def function(n):
# 	result = '1'
# 	if n==1:
# 		return result
# 	else:
# 		result=function(n//2)  #取整
# 		return result+str(n%2)   #字符串相连
# print(function(n))


# 非递归方法
# def function(n):
# 	s=''
# 	while n>0:
# 		s=str(n%2)+s
# 		n=n//2
# 	return s
# n=int(input("please input a number(<90000):"))
# print(function(n))


#一个射击运动员打靶，靶一共有10环，连开6枪打中45环的可能性有多少种
#王小丰
#2019/10/21

# times=0
# def function(n,sum):
# 	global times
# 	if n<0:
# 		return
# 	elif n==0 and sum==45:    #不可用&&
# 		times+=1
# 		return 
# 	elif (45-sum)>(10*(n)):
# 		return
# 	for x in range(11):
# 		function(n-1,sum+x)
# 	return times

# function(6,0)
# print('一共有%d种'%times)


#在8×8格的国际象棋上摆放八个皇后，使其不能互相攻击，即任意两个皇后都不能处于同一行、同一列或同一斜线上，输出所有摆法。
#state[i] 表示列     nextx  表示下一个皇后的列     nexty   表示行或者是已经有几个皇后
#王小丰
#2019/10/21

# 递归
# 冲突条件判断
# def conflict(state,nextX):
# 	nextY=len(state)
# 	for i in range(nextY):
# 		if abs(state[i]-nextX) in (0,nextY-i):#state[i]-nextX=0在同一列  and abs(state[i]-nextX)=nextY-i在斜线上
# 			return True
# 	return False


# def queens(num=8,state=()):
# 	for position in range(0,num):#range(0.num)
# 		if not conflict(state,position):
# 			if len(state)==num-1:#只剩一个皇后
# 				yield(position,)#只含一个元素的元组
# 			else:#前七个皇后
# 				for result in queens(num,state+(position,)):
# 					yield(position,)+result#元组相加

# for i in list(queens(8)):
# 	print(i)
#元组转化为列表输出
# for i,x in enumerate(list(queens(8))):
#  	print(i,x)



#递归第二种解法
# def queen(A, cur=0):
#     if cur == len(A):
#         print(A)
#         return 0
#     for col in range(len(A)):
#         A[cur], flag = col, True
#         for row in range(cur):
#             if A[row] == col or abs(col - A[row]) == cur - row:
#                 flag = False
#                 break
#         if flag:
#             queen(A, cur+1)

# queen([None]*8)




#翻牌问题
#王小丰
#2019/10/21

# c=[0]*52
# def card(n):
# 	if n>=52:
# 		return
# 	else:
# 		for x in range(n,52):
# 			if (x+1)%(n+1)==0:
# 				if c[x]==0:
# 					c[x]=1
# 				else:
# 					c[x]=0
# 	card(n+1)

# card(1)

# card=[x+1 for x in range(52) if c[x]==0]
# print(card)








#迷宫回溯算法  
#https://www.cnblogs.com/hhh5460/p/6919320.html

#输入迷宫
# maze = [[0,0,0,0,0,0,1,0],
#         [1,0,1,1,1,1,1,0],
#         [0,1,0,0,1,0,0,1],
#         [0,0,1,1,0,1,0,1],
#         [0,1,0,0,0,1,1,0],
#         [0,1,1,1,1,1,0,1],
#         [0,0,1,1,1,0,1,1],
#         [1,1,0,0,1,0,0,0]]

# m,n = 8,8    #八行八列
# entry=(0,0)  #迷宫入口
# out=(7,7)
# path = [entry] #一个解（路径）
# paths = []  #一组解

# #移动的方向
# directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]


# #冲突检测
# def conflict(nx,ny):
# 	global m,n,maze

# 	#是否在迷宫中以及是否可以通行
# 	if 0<=nx<m and 0<=ny<n and maze[nx][ny]==0:
# 		return False

# 	return True

# #回溯
# def function(x,y):
# 	global m,n,maze,entry,path,paths,directions

# 	if (x,y)==out:
# 		paths.append(path[:])
# 	else:
# 		for d in directions:
# 			nx,ny=x+d[0],y+d[1]
# 			path.append((nx,ny))
# 			if not conflict(nx,ny):
# 				maze[nx][ny]='Y'
# 				function(nx,ny)
# 				maze[nx][ny]=0
# 			path.pop()



#输出
# function(0,0)
# print(paths[-1],'\n')

# for i in range(0,200):
# 	print(paths[i],'\n')


#八皇后回溯算法
#https://blog.csdn.net/moqsien/article/details/79588052
#

# 设置棋盘的大小规模
max_coordinate = 8
# 构建数据结构
# 初始化坐标列表，
# 列表的value为纵坐标值（即棋盘上行数的标记值）
# 列表的index为横坐标值（即棋盘列数标记值）
queen_list = [None]*8
 
 
def show():
    column = 0
    # 对列进行遍历，打印坐标
    while column < max_coordinate:
        print("(%d, %d)" % (column, queen_list[column]), end=" ")
        column += 1
    print("")
 
 
# 对第棋盘上第column列的情况进行检查，看看是否能够放置皇后
def check(column):
    column_2 = 0
    # 对比column小的列进行遍历
    while column_2 < column:
        # 如果比column小的列中有和column对应的queen_list的值相等（即在同一行），
        # 或者有二者的行标记之差的绝对值等于列标记之差的情况（即在其对角线上），
        # 则不能放置该皇后
        if (queen_list[column_2] == queen_list[column]) or (abs(queen_list[column_2] - queen_list[column]) == column - column_2):
            return False
        column_2 += 1
    # 否则，可以放置该皇后
    return True
 
 
# 回溯算法的递归函数主体
# 传入一个初始的横坐标值（即对应棋盘上的列数的标记值）
def put_queen(column):
    row = 0
    # 
    # 对棋盘的行进行遍历：0~7行
    while row < max_coordinate:
        # 假设该皇后可以放置在棋盘的第row行，第column列上
        queen_list[column] = row
        # 对第棋盘的column列进行检查，如果满足条件则进行下一列的放置
        if check(column):
            # 如果已至最后一列，则调用显示方法，打印结果，跳出递归
            if column == max_coordinate - 1:
                show()
            else:
                # 如果未至最后一列，则递归调用自身，实现在下一列中放置另一个皇后
                put_queen(column + 1)
        row += 1
 
 
def main():
    put_queen(0)
    print("="*10)
 
 
if __name__ == '__main__':
    main()




			