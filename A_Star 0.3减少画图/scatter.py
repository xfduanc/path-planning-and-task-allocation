import matplotlib.pyplot as plt
import numpy as np
import time

class Scatter:
    def __init__(self, path, i, dir):
        self.path = path
        self.x_values = []
        self.y_values = []
        self.index = i
        self.fileDir = dir
        pass
    def SaveImage(self, plt):
        millis = int(round(time.time() * 1000))
        
        filename = './' + self.fileDir+ "/" + str(millis) + '.png'
        plt.draw()
        plt.savefig(filename)
    def draw(self):
        for p in self.path:
            self.x_values.append(p.x)
            self.y_values.append(p.y)

        ax = plt.subplot(111)
        title = None
        color = None
        if self.index %2 == 0:
            ax.plot(self.x_values, self.y_values, color='#ed1941',marker='+',linestyle='dashed', linewidth=1, markersize = 5)#赤红
            title = 'Graph 1'
            color ='#ed1941'
        else:
            ax.plot(self.x_values, self.y_values, color='#f47920',marker='*',linestyle='dashed', linewidth=1, markersize = 5)#橙色
            title = 'Graph 2'
            color ='#f47920'
        plt.xlabel("X -Value", fontsize=14)
        plt.ylabel("Y -Value", fontsize=14)
        plt.title(title, y=-0.1, loc ="center", c =color, pad = -20,fontsize =10)#红
        self.SaveImage(plt)

