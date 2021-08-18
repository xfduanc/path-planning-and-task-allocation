import matplotlib.pyplot as plt  
import numpy as np
'''read file 
fin=open("para.txt")
a=[]
for i in fin:
  a.append(float(i.stripsubplotsa=np.array(a)
a=a.reshape(9,3)
'''
a=np.random.random((9,3)) #随机生成数字为0-1 9行3列
'''
matrix = np.random.randint(10000, 100000, (1, 100))
print( matrix[[0],[0]])
'''
print(a)
##切片
y1=a[0:,0]
y2=a[0:,1]
y3=a[0:,2]

print(y3)
x=np.arange(1,10)

#为当前图像添加一个子图
#pyplot.subplot(nrows, ncols, index, **kwargs)
width=10
hight=3
#ax.arrow(0,0,0,hight,width=0.01,head_width=0.1, head_length=0.3,length_includes_head=True,fc='k',ec='k')
#ax.arrow(0,0,width,0,width=0.01,head_width=0.1, head_length=0.3,length_includes_head=True,fc='k',ec='k')
 
#ax.axes.set_xlim([-0.5,width+0.2])
#ax.axes.set_ylim([-0.5,hight+0.2] )
 
#plotdict = { 'dx': x, 'dy': y1 }
#ax.plot('dx','dy','bD-',data=plotdict)
 
#ax.plot(x,y2,'r^-')
ax = plt.subplot(111)
ax.plot(x, y3, color='#900302',marker='*',linestyle='-')
 
plt.show()
