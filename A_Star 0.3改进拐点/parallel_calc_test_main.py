#-*- coding: UTF-8 -*-
import numpy as np

import matplotlib.pyplot as plt

#from matplotlib.patches import Rectangle
from matplotlib.patches import Rectangle
import random_map,pp,sys,time
import a_star
import point
import os
from matplotlib.patches import Rectangle
import point



#matplotlib.pyplot.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True, FigureClass=<class 'matplotlib.figure.Figure'>, clear=False, **kwargs)
plt.figure(figsize=(8, 8))

map = random_map.RandomMap() 


ax = plt.gca()
ax.set_xlim([0, map.size]) 
ax.set_ylim([0, map.size])

for i in range(map.size): 
    for j in range(map.size):
        if map.IsObstacle(i,j):
            rec = Rectangle((i, j), width=1, height=1, color='gray')
            ax.add_patch(rec)
        else:
            rec = Rectangle((i, j), width=1, height=1, edgecolor='gray',  facecolor='w')
            ax.add_patch(rec)

rec = Rectangle((0, 0), width = 1, height = 1, facecolor='#1d953f')
ax.add_patch(rec)

randx = ( map.size - np.random.randint(5, map.size//5) )
randy = ( map.size - np.random.randint(5, map.size//5) )

print("(", randx, ",", randy, ")")

rec = Rectangle((randx, randy), width = 1, height = 1, facecolor='#1d953f')#薄緑

ax.add_patch(rec)



plt.axis('equal') 
plt.axis('off')
plt.tight_layout()
#plt.show()



end_point = point.Point(randx, randy)
a_star = a_star.AStar(map, end_point)
a_star.GetFileSvaePath()
ppservers = ()
job_server = pp.Server(ppservers=ppservers)

start_time = time.time()



for i in range(2):
    a_star.SetWeight(2)#设置权重
    plt.title("A_Star_1", y=-0.1, loc ="center", c ="red", pad = -20,fontsize =10)
    a_star.RunAndSaveImage(ax, plt, i)
    
print( "多线程下执行耗时: ", (time.time() - start_time ) )
