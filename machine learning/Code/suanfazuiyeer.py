# -*- coding: utf-8 -*-

import numpy as np

#动态规划算法最长编辑距离
#def distance(a,b):
#    m = len(a)
#    n = len(b)
#    c = np.zeros((m+1,n+1))
#    for i in range(m+1):
#        c[i][0] = i
#    for j in range(n+1):
#        c[0][j] = j
#        
#    for i in range(1,m+1):
#        for j in range(1,n+1):
#            if a[i-1] == b[j-1]:
#                delta = 0
#            else:
#                delta = 1
#            c[i][j] = min(c[i - 1][j - 1] + delta, min(c[i-1][j] + 1, c[i][j - 1] + 1))
#    print(c[m][n])
#            
#        
#distance("abddde","acdd")
#最长公共子序列
def LCS(a,b):
    m = len(a)
    n = len(b)
    res = [[0 for i in range(m+1)] for j in range(n+1)]#先是创建含有m+1个零的数组，然后在创建n+1个这样的数组
#    print(res)
    for i in range(1,n+1):
        for j in range(1,m+1):
            if b[i-1] == a[j-1]:
                res[i][j] = res[i-1][j-1]+1
            else:
                res[i][j] = max(res[i-1][j],res[i][j-1])
    print(res)
    return res[-1][-1]+ 
s1 = input("please input a string:")
s2 = input("please input a string:")
print(LCS(s1,s2))






