# expressions=[]
# with open('test.txt', 'rt',encoding='UTF-8') as f:
#     expressions = f.read().replace('\n','').split('；')[:-1]
# with open('output.txt', 'wt') as f:
#     for item in expressions:
#         print(eval(item), file=f)   #eval() 函数用来执行一个字符串表达式，并返回表达式的值。






#-*- coding :utf-8 -*-
#https://www.cnblogs.com/once-again/p/9562594.html


outfile = 'C:/Users/王小丰/Desktop/output.txt'
def grad(file):
    f =  open(outfile,'w',encoding='UTF-8')
    with open(file,'r', encoding='UTF-8' ) as fr:    
        for line in fr:
            #print(line)
            li = line.split('；')
            #print(li)
            for li_ in li:
                #print(li_)
                if len(li_) > 1:
                    for j in li_: 
                        if j == '+':
                            res = int(li_[0:li_.index(j)]) + int(li_[li_.index(j)+1:])
                        elif j == '-':
                            res = int(li_[0:li_.index(j)]) - int(li_[li_.index(j)+1:])
                        elif j == '*':
                            res = int(li_[0:li_.index(j)]) * int(li_[li_.index(j)+1:])
                        else:
                            continue
                        print(res)
                        f.writelines(str(res)+'\n')
                            


       
grad('1.txt')

    
    

