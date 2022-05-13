import os
import shutil

path="./imagenet"
wnidsdir=os.path.join(path,'wnids.txt')

with open (wnidsdir,'r') as f:
    lines=f.readlines()
    data=[]
    for line in lines:
        line=line.strip('\n')
        data.append(line)

vardir=os.path.join(path,'val')
imagedir=os.path.join(vardir,'images')

with open (os.path.join(vardir,'val_annotations.txt'),'r') as fv:
    lines=fv.readlines()
    imgdata=[]
    for line in lines:
        line=line.strip('\n')
        line=line.split()[1]
        imgdata.append(line)


imglist=os.listdir(imagedir)
imglist.sort(key=lambda x:int(x[4:-5]))

for i in range(0,200):
    finalpath=os.path.join(imagedir,data[i])
    if not os.path.exists(finalpath):
        os.makedirs(finalpath)

for i in range(0,10000):
    id=imgdata[i]
    f1=os.path.join(imagedir,imglist[i])
    f2=os.path.join(imagedir,id)
    shutil.move(f1,f2)

print("succeed!")

