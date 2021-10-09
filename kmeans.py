import numpy as np
import math
from matplotlib import pyplot as plt
import matplotlib

points=[(1,1),(100,100),(1,0),(98,100),(1,2),(100,98),(2,1),(2,2),(98,98),(0,1),(-200,98),(-198,100),(-200,100),(198,98)]

X=[]
Y=[]
for x,y in points:
    X.append(x)
    Y.append(y)


#Initialize random mean points, dist and label as 0
mean=[(10,14),(67,80),(-10,100)]
dist=np.zeros([len(points),3])
labels=np.zeros([len(points),1],dtype=int)

def dist_(x,y):
    a=x[0]-y[0]
    b=x[1]-y[1]
    return math.sqrt((a*a)+(b*b))
def min_(x,y,z):
    if x<=y and x<=z:
        return 1
    if y<=x and y<=z:
        return 2
    if z<=x and z<=y:
        return 3

for k in range(1,4):
    print("in ",k, "iteration:")
    for i in range(0,len(points)):
        dist[i][0]=dist_(points[i],mean[0])
        dist[i][1]=dist_(points[i],mean[1])
        dist[i][2]=dist_(points[i],mean[2])
        labels[i]=min_(dist[i][0],dist[i][1],dist[i][2])
    print(dist)
    print(labels)
    mean1=0
    mean2=0
    mean3=0
    x1=0
    x2=0
    x3=0
    y1=0
    y2=0
    y3=0
    for j in range(0,len(labels)):
        if labels[j]==1:
            mean1+=1
            x1+=points[j][0]
            y1+=points[j][1]
        if labels[j]==2:
            mean2+=1
            x2+=points[j][0]
            y2+=points[j][1]
        if labels[j]==3:
            mean3+=1
            x3+=points[j][0]
            y3+=points[j][1]

    #print(mean1,mean2,mean3)
    mean.clear()
    mean.append(((x1/mean1),(y1/mean1)))
    mean.append(((x2/mean2),(y2/mean2)))
    mean.append(((x3/mean3),(y3/mean3)))

    print("new means s:")
    print(mean)

plt.scatter(X,Y,c=labels, cmap=matplotlib.colors.ListedColormap(['green','blue','yellow']))

xx=[]
yy=[]
for x,y in mean:
    xx.append(x)
    yy.append(y)
plt.scatter(xx,yy,color='r',marker='*')
plt.show()
