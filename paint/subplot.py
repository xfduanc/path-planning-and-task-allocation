#!/usr/bin/python
#coding=utf-8
import matplotlib.pyplot as plt
 
xdata=range(1,100)
ydata=[x*2+1 for x in xdata]
projections=["rectilinear","aitoff","hammer","lambert","mollweide","polar"]
fig=plt.figure(figsize=(10,8), dpi=100)
colsize=3
count=len(projections)
row=count//colsize + (count%colsize!=0 and 1 or 0 )
 
for i in range(count):
	#print row,colsize,i+1
	ax=plt.subplot(row,colsize,i+1,projection=projections[i])
	ax.plot(xdata,ydata)

plt.axis([0, 200, 0, 300])	
plt.show()