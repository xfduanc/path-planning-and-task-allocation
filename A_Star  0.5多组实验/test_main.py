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
import draw

func_list =[]
draw_list =[]
#matplotlib.pyplot.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True, FigureClass=<class 'matplotlib.figure.Figure'>, clear=False, **kwargs)
def GetFileSvaePath():
	fileDir = time.strftime("Path-Img%m%d%H%M%S", time.localtime()) + " {:3d}".format( np.random.randint(100, 1000) )###有问题
	return fileDir
def init_env(size_t):
	if size_t >= 100:
		tpl =(15, 15)
	else:
		tpl =(8, 8)
	# plt.cla()
	plt.figure(figsize=tpl)

	map = random_map.RandomMap( size_t ) 

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
	plt.axis('equal') 
	plt.axis('off')
	plt.tight_layout()

	return ax,plt,map

def fix_test(size_t, randx, randy, fileDir, group, ax, plt,map):
	
	rec = Rectangle((randx, randy), width = 1, height = 1, facecolor='#1d953f')#薄緑
	ax.add_patch(rec)

	end_point = point.Point(randx, randy)
	b_star = a_star.AStar(map, end_point, fileDir)

	b_star.SetWeight(2)#设置权重
	plt.title("Graph", y=-0.1, loc ="center", c ="#d71345", pad = -20,fontsize =10)#红

	b_star.RunAndSaveImage(ax, plt, group)
	tool = scatter.Scatter(b_star.drawlist, size_t, group)
	p = multiprocessing.Process(target = tool.draw)
	func_list.append(p)
	return b_star.time, b_star.distance

#########################################################
if __name__ == '__main__':
	time_list =[]
	distance_list =[]
	size_list = [200]
	fileDir = GetFileSvaePath()
	for size in size_list:
		randx =None
		randy =None
		ax, plt,map= init_env(size)
		for group in range(14):
			if group%2 == 0:
				randx = ( size - np.random.randint(5, size//5) )
				randy = ( size - np.random.randint(5, size//5) )
				print("(", randx, ",", randy, ")")
			time_, distance_ =fix_test(size, randx, randy, fileDir, group, ax, plt,map)
			time_list.append(time_)
			distance_list.append(distance_)

	draw_dist = draw.Draw(size_list[0], "dist", [i for i in range(0, 7)], distance_list)
	draw_time = draw.Draw(size_list[0], "time", [i for i in range(0, 7)], time_list)
	dist = multiprocessing.Process(target = draw_dist.draw)
	time_ = multiprocessing.Process(target = draw_time.draw)
	draw_list.append(dist)
	draw_list.append(time_)

	for f in func_list:
		f.start()
		pass
	for f in draw_list:
		f.start()
		pass