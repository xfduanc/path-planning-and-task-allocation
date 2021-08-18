import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Rectangle

import random_map
import a_star


#matplotlib.pyplot.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True, FigureClass=<class 'matplotlib.figure.Figure'>, clear=False, **kwargs)
plt.figure(figsize=(10, 10))

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
            rec = Rectangle((i, j), width=1, height=1, edgecolor='gray', facecolor='w')
            ax.add_patch(rec)

rec = Rectangle((0, 0), width = 1, height = 1, facecolor='b')
ax.add_patch(rec) 

rec = Rectangle((map.size-1, map.size-1), width = 1, height = 1, facecolor='r')
ax.add_patch(rec)



plt.axis('equal') 
plt.axis('off')
plt.tight_layout()
#plt.show()

a_star = a_star.AStar(map)
for i in range(2):
	a_star.SetWeight(i+1)
	plt.title("A_Star_1", y=-0.1, loc ="center", c ="red", pad = -10,fontsize =5)

	a_star.RunAndSaveImage(ax, plt)


'''
# 在右侧底部显示子图标题
plt.title("right bottom",y=0,loc='right')
# 在左侧顶部显示子图标题
plt.title("left top",y=1,loc='left')
# 显示默认子图标题
plt.title("default")
'''




