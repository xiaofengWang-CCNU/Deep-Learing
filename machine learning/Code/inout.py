# -*- coding: utf-8 -*-
import pickle
import random
import sys
import numpy as np

with open ('file.txt','wb') as myfile:
    a = random.random()
    b = 'Hello,World'
    pickle.dump(a,myfile)
    pickle.dump(b,myfile)
    
    
with open ('file.txt','rb') as myfile:
    number = pickle.load(myfile)
    text = pickle.load(myfile)
    
    
print(number,'\n',text)

#print(sys.path)

#with errstate (invalid = 'ignore'):
#    print(np.sqrt(-1))
 