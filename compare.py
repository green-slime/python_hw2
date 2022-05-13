import numpy as np
from torch import flatten

with open("pred.txt",'r') as f1:
    line=f1.readline()
    line=line[:-1]
    data1=line.split(',')
    data1=np.array(data1)
    while line:
        line=f1.readline()[:-1]       
        data1=np.append(data1,np.array(line.split(',')))

np.ndarray.flatten(data1)

with open("pred2.txt",'r') as f2:
    line=f2.readline()
    line=line[:-1]
    data2=line.split(',')
    data2=np.array(data2)
    while line:
        line=f2.readline()[:-1]       
        data2=np.append(data2,np.array(line.split(',')))

np.ndarray.flatten(data2)

counter=0
for i in range(0,100):    
    if data1[i]!=data2[i]:
        counter=counter+1
        print(i)
print("counter="+str(counter))