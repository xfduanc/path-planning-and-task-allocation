import sys
import time
import os
import numpy
import pp

#import matplotlib.patches import Rectangle
import matplotlib
import point
import random_map

class AStar:
    def __init__(self, map, end_point, 	fileDir):
        self.map=map
        self.patch_list =[]
        self.open_set = []
        self.close_set = []
        self.distance=None
        self.time =None
        ppservers = ()
        self.job_server = pp.Server(ppservers=ppservers)
        self.fileDir = fileDir 
        self.end_point = end_point
        self.drawlist =[]
    #设置权重比例
    def SetWeight(self, weight):
        self.weight_x = 1.0/(weight+1.0)
        self.weight_y = weight/(weight +1.0)

    # F()=G() + H()
    # 对角线距离
    
    def GetFileSvaePath(self):
        self.fileDir = time.strftime("Path-Img%m%d%H%M%S", time.localtime()) + " {:3d}".format( numpy.random.randint(100, 1000) )###有问题
        return self.fileDir
    def BaseCost(self, p):
        x_dis = p.x
        y_dis = p.y
        # Distance to start point
        return x_dis + y_dis## + ( numpy.sqrt(2) - 2) * min(x_dis, y_dis)

    #启发式距离
    def HeuristicCostDiagonal(self, p):
        x_dis = self.end_point.x - p.x
        y_dis = self.end_point.y - p.y
        # Distance to end point
        return x_dis + y_dis + (numpy.sqrt(2) - 2) * min(x_dis, y_dis)

    def HeuristicCostManhattan(self, node):
        dx = numpy.abs(self.end_point.x - node.x)
        dy = numpy.abs(self.end_point.y - node.y)
        # Distance to end point
        return dx+dy

    def TotalCost(self, p):
        return self.weight_x*self.BaseCost(p) + self.weight_y * self.HeuristicCostManhattan(p)

    def IsValidPoint(self, x, y):
        if x < 0 or y < 0:
            return False
        if x >= self.map.size or y >= self.map.size:
            return False
        return not self.map.IsObstacle(x, y)

    def IsInPointList(self, p, point_list):
        for point in point_list:
            if point.x == p.x and point.y == p.y:
                return True
        return False

    def IsInOpenList(self, p):
        return self.IsInPointList(p, self.open_set)

    def IsInCloseList(self, p):
        return self.IsInPointList(p, self.close_set)

    def IsStartPoint(self, p):
        return p.x == 0 and p.y ==0

    def IsEndPoint(self, p):
        return p.x == self.end_point.x and p.y == self.end_point.y

    def RunAndSaveImage(self, ax, plt, index):
        #self.SetWeight(index)
        self.index = index
        start_time = time.time()

        start_point = point.Point(0, 0)
        start_point.cost = 0
        self.open_set.append(start_point)

        #self.GetFileSvaePath()
        if False == os.access(self.fileDir, os.F_OK):
            os.mkdir(self.fileDir)
        # return self.SaveImage(plt)#### 测试地图
        loop =sys.maxsize
        while (loop >0):#True:
            index = self.SelectPointInOpenList()
            if index < 0:
                print('No path found, algorithm failed!!!')
                return
            p = self.open_set[index]
            rec=None
            if 0 == self.index%2:
                rec = matplotlib.patches.Rectangle((p.x, p.y), 1, 1, color='#f8aba6')#珊瑚色
            else:
                rec = matplotlib.patches.Rectangle((p.x, p.y), 1, 1, color='#f7acbc')#鸨色

            ax.add_patch(rec)
            self.patch_list.append(rec)
            #self.SaveImage(plt)
            if self.IsEndPoint(p):
                self.open_set = []
                self.close_set = []
                return self.BuildPath(p, ax, plt, start_time)

            del self.open_set[index]
            self.close_set.append(p)

            # Process all neighbors
            x = p.x
            y = p.y

            #处理周围8个点
            self.ProcessPoint(x-1, y+1, p)
            self.ProcessPoint(x-1, y, p)
            self.ProcessPoint(x-1, y-1, p)
            self.ProcessPoint(x, y-1, p)
            self.ProcessPoint(x+1, y-1, p)
            self.ProcessPoint(x+1, y, p)
            self.ProcessPoint(x+1, y+1, p)
            self.ProcessPoint(x, y+1, p)

            loop-=1
    def SaveImage(self, plt):
        millis = int(round(time.time() * 1000))

        filename = './' + self.fileDir+ "/" + '{} {} {:x<3d}'.format(str(self.map.size), str(self.index+1) , millis%1000) + '.png'
        plt.savefig(filename)
        [p.remove() for p in self.patch_list]
        self.patch_list=[]
        plt.rcParams.update({'figure.max_open_warning': 0})

    def ProcessPoint(self, x, y, parent):
        if not self.IsValidPoint(x, y):
            return # Do nothing for invalid point
        p = point.Point(x, y)
        if self.IsInCloseList(p):
            return # Do nothing for visited point
        #print('Process Point [', p.x, ',', p.y, ']', ', cost: ', p.cost)
        if not self.IsInOpenList(p):
            p.parent = parent
            p.cost = self.TotalCost(p)
            self.open_set.append(p)

    def SelectPointInOpenList(self):
        index = 0
        selected_index = -1
        min_cost = sys.maxsize
        for p in self.open_set:
            cost = self.TotalCost( p )
            if cost < min_cost:
                min_cost = cost
                selected_index = index
            index += 1
        return selected_index

    def BuildPath(self, p, ax, plt, start_time):
        path = []
        end = p

        while True:
            path.insert(0, p) # Insert first
            if self.IsStartPoint(p):
                p.parent = None
                break
            else:
                p = p.parent
        p = end

        if 0 == self.index%2:
            i = 0
            len_t = len(path)
            while i < len_t:
                headpath = path[:len_t -i]
                tailpath = path[len_t-i:]
                headpath = self.partial_opt(headpath[len(headpath)-1])
                path =[]
                path +=headpath
                path +=tailpath
                i +=1
                len_t = len(headpath)

        self.drawlist = path

        sum = self.calculate_path_distance(path)
        self.distance =sum
        print("distance:", '{:.4f}'.format(sum ) )
        plot_x =[]
        plot_y =[]
        for p in path:
            if 0 == self.index%2:
                rec = matplotlib.patches.Rectangle((p.x, p.y), 1, 1, color='#d71345')#红
            else:
                rec = matplotlib.patches.Rectangle((p.x, p.y), 1, 1, color='#6b473c')#焦茶
            ax.add_patch(rec)
            self.patch_list.append(rec)
        plt.draw()
        self.SaveImage(plt)
        plot_x.append(p.x)
        plot_y.append(p.y)
        '''
        if 0 == self.index%2:
            ax = plt.subplot(121)
            ax.plot(plot_x, plot_x,color='#900302',marker='*',linestyle='-')
        else:
            ax = plt.subplot(122)
            ax.plot(plot_x, plot_x,color='#900302',marker='*',linestyle='-')
        plt.show()'''
            ##[p.remove() for p in reversed(ax.patches)]
        end_time = time.time()
        self.time ='{:.4f}'.format(end_time-start_time)
        print('time : ', '{:.4f}'.format(end_time-start_time), ' seconds')

    def partial_opt(self,  end):
        last  = None
        first = True
        new  = []
        while end != None:
            new.insert(0, end)
            if not first:
                last.parent = end
            else:
                first = False
            last = end
            head = end.parent#self.getPP(end)
            cache_head = head
            while head !=None and end != None and True == self.SmoothPath(end, head):
                cache_head = head
                head = head.parent
            #print("while: ", head.x, head.y, " --> ", end.x, end.y)
            end = cache_head
        return new

    def getPP(self, end):
        if end != None:
            if end.parent !=None and end.parent.parent !=None:
                return end.parent.parent
            elif end.parent != None:
                return end.parent
        return None
    def SmoothPath(self, cur, pp):
        ret = True
        if self.IsStartPoint( pp ):
            return False
        if pp.x != cur.x:
            Slope = (cur.y - pp.y)/( cur.x -pp.x)
            #print(Slope)
            for a in range(pp.x +1, cur.x):
                p = point.Point(a, Slope*( a- cur.x)+cur.y )
                if self.IsObstacle(p.x, p.y):
                    ret = False
                    break
        else:
            for b in range(pp.y + 1, cur.y):
                p = point.Point(cur.x, b)
                if self.map.IsObstacle(p.x, p.y):
                    ret = False
                    break
        return ret

    # 计算两个点的距离
    def calculate_distance(self, a, b):
        return numpy.sqrt( numpy.power(a.x - b.x, 2) + numpy.power(a.y - b.y, 2) )

    # 计算整条路径的距离
    def calculate_path_distance(self, path):
        sum = 0.0
        for i in range(1, len(path)):
            sum += self.calculate_distance(path[i-1], path[i])
        return sum

    def IsObstacle(self, x, y):
        for p in self.map.obstacle_point:
            if x >= (p.x - 1.414) and x <= (p.x+ 1.414) and y >= (p.y - 1.414) and y <= (p.y + 1.414) :
                return True
        return False