#-*- coding: UTF-8 -*-
import numpy as np

import matplotlib.pyplot as plt

import a_star
#from matplotlib.patches import Rectangle
from matplotlib.patches import Rectangle
import random_map,pp
import point
import scatter
import sys
import time
import os
import multiprocessing

#matplotlib.pyplot.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True, FigureClass=<class 'matplotlib.figure.Figure'>, clear=False, **kwargs)
def GetFileSvaePath():
    fileDir = time.strftime("Path-Img%m%d%H%M%S", time.localtime()) + " {:3d}".format( np.random.randint(100, 1000) )###有问题
    return fileDir

def fix_test(size_t, fileDir, group):
    if size_t >= 300:
        tpl =(20, 20)
    elif size_t >= 200:
        tpl =(15, 15)
    else:
        tpl =(8, 8)
    plt.figure(figsize=tpl)

    map = random_map.RandomMap( size_t) 
    print("Map size : ", size_t)

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
    b_star = a_star.AStar(map, end_point, fileDir)

    start_time = time.time()
    func_list =[]
    jobs = []

    for i in range(2):
        b_star.SetWeight(2)#设置权重
        if i %2 == 0:
            pass
            # b_star.SetWeight(0)#设置权重
            # plt.title("Graph 1", y=-0.1, loc ="center", c ="#d71345", pad = -20,fontsize =10)#红
        else:
            b_star.SetWeight(0)#设置权重
            plt.title("Graph 2", y=-0.1, loc ="center", c ="#6b473c", pad = -20,fontsize =10)#焦茶

        #a_star.RunAndSaveImage(ax, plt, i)

            b_star.RunAndSaveImage(ax, plt, i, group)
            tool = scatter.Scatter(b_star.drawlist, i, size_t, group)
            p = multiprocessing.Process(target = tool.draw)
            func_list.append(p)


    start_time = time.time()
    for f in func_list:
        f.start()
#########################################################
if __name__ == '__main__':
    # size_list = [50, 100, 200, 400]
    size_list = [50]
    fileDir = GetFileSvaePath()
    for size in size_list:
        for i in range(1):
            fix_test(size, fileDir, i)