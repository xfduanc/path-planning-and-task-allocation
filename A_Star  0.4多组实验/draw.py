import matplotlib.pyplot as plt
import numpy as np
import time

class Draw:
    def __init__(self, map_size, typeinfo, x_value, y_value):
        self.map_size = map_size
        self.type = typeinfo
        self.y_values=[]
        self.x_values =np.array(x_value)
        for p in y_value:
            self.y_values.append(float(p))
        pass
    def SaveImage(self, plt):
        millis = int(round(time.time() * 1000))
        filename = './' + "Figure" +"/" + '{} {} {:x<3d}'.format( "draw_", str(self.map_size), millis%1000) + '.png'
        plt.savefig(filename)


    def draw(self):

        ax = plt.subplot(111)
        title = None
        color = None

        # plt.scatter(self.x_values, self.y_values, c="red", edgecolor ='none', s=1)
        ax.plot(self.x_values, self.y_values, color='#ed1941',marker='+',linestyle='dashed', linewidth=1, markersize = 5)#赤红
        title = 'Graph 1'
        color ='#ed1941'
        if self.type =='time':
            plt.ylabel('time', fontsize = 10) # 横坐标轴的标题
        else:
            plt.ylabel('distance', fontsize = 10) # 横坐标轴的标题
        plt.xlabel('index', fontsize = 18) # 纵坐标轴的标题
        plt.title(title, y=-0.1, loc ="center", c =color, pad = -20,fontsize =10)#红
        plt.draw()
        self.SaveImage(plt)
        plt.clf()

