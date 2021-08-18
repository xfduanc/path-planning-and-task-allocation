import matplotlib.pyplot as plt
import numpy as np

class Scatter:
    def __init__(self, title, index):
        self.x_values = []
        self.y_values = []
        self.title = title
        self.index = index
        pass
    def append(self, x, y):
        self.x_values.append(x)
        self.y_values.append(y)

    def draw(self):
        ax = plt.subplot(111)
        title = None
        color = None
        mark = None
        if self.index == 0:
            color ='#ed1941'
            mark = '+'
        elif self.index == 1:
            color = '#f47920'
            mark = '*'
        else:
            color = '#145b7d'#青色黄
            mark = 'x'
        ax.plot(self.x_values, self.y_values, color=color, marker=mark, linestyle='dashed', linewidth=0.2, markersize = 1)#赤红
        plt.xlabel("Current Loop", fontsize=14)
        plt.ylabel("Total Distance", fontsize=14)

        plt.title(self.title, y= 1 , loc ="center", c =color, pad = 0,fontsize =10)#红
        plt.show()

