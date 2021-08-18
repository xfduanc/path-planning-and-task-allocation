import matplotlib.pyplot as plt
import numpy as np
import time

class Scatter:
    def __init__(self, path, i, map_size, group):
        self.path = path
        self.x_values = []
        self.y_values = []
        self.index = i
        self.map_size = map_size
        self.group = group
        pass
    def SaveImage(self, plt):
        millis = int(round(time.time() * 1000))
        filename = './' + "Figure" +"/" + '{} {} {} {:x<3d}'.format( str(self.map_size), str(self.group), str(self.index+1) ,   millis%1000) + '.png'
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

        plt.title(title, y=-0.1, loc ="center", c =color, pad = -20,fontsize =10)#红
        plt.draw()
        self.SaveImage(plt)
        plt.clf()

