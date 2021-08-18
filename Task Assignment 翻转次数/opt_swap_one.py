import numpy as np
import matplotlib.pyplot as plt
import time
import scatter
import multiprocessing

#在这里设置迭代停止条件，要多尝试一些不同数值，最好设置大一点
MAXCOUNT = None

#数据在这里输入，依次键入每个城市的坐标

class OptSwapOne:
    def __init__(self, MAX_LOOP:int, path, cities):
        self.MAXCOUNT = MAX_LOOP
        self.path = path
        self.cities = cities

    def calDist(self, xindex, yindex):
        return (np.sum(np.power(self.cities[xindex] - self.cities[yindex], 2))) ** 0.5

    def calPathDist(self, indexList):
        sum = 0.0
        for i in range(1, len(indexList)):
            sum += self.calDist(indexList[i], indexList[i - 1])
        return sum

    #path1长度比path2短则返回true
    def pathCompare(self, path1, path2):
        dist_one = self.calPathDist(path1)
        dist_two = self.calPathDist(path2)
        if dist_one > dist_two:
            #self.dist = dist_two
            return True
        return False

    def generateRandomPath(self, bestPath):
        a = np.random.randint(len(bestPath))
        while True:
            b = np.random.randint(len(bestPath))
            if np.abs(a - b) > 1:
                break
        if a > b:
            return b, a, bestPath[b:a+1]
        else:
            return a, b, bestPath[a:b+1]

    def reversePath(self, path):
        rePath = path.copy()
        rePath[1:-1] = rePath[-2:0:-1]
        return rePath
        
    def updateBestPath(self, bestPath):
        count = 0
        loop = 0
        self.paint = scatter.Scatter("General Algorithm Optimization", 1)
        while count < self.MAXCOUNT:
            
            start, end, path = self.generateRandomPath(bestPath)
            rePath = self.reversePath(path)
            if self.pathCompare(path, rePath):
                count = 0
                bestPath[start:end+1] = rePath
                self.dist = self.calPathDist(bestPath)
            else:
                count += 1
                continue
            self.paint.append(loop, self.dist)
            loop +=1
        return bestPath
        

    def draw(self, bestPath):
        print("Original Finally Generated : ", bestPath.tolist())
        #fig = plt.figure(figsize=(10, 10), dpi=100)
        ax = plt.subplot(111, aspect='equal')
        ax.plot(self.cities[:, 0], self.cities[:, 1], 'x', color='blue')
        for i,city in enumerate(self.cities):
            ax.text(city[0], city[1], str(i))

            ax.text(city[0], city[1], str(i))
        ax.plot(self.cities[bestPath, 0], self.cities[bestPath, 1], color='red', linewidth=0.8, linestyle=':')
        plt.title("General Algorithm Optimization")

        plt.xlabel("X -Value", fontsize=14)
        plt.ylabel("Y -Value", fontsize=14)
         
        plt.tick_params(axis='both', which='major', labelsize=14)
        plt.show()

        
    
    def run(self):
        #随便选择一条可行路径
        print("------------------Algorithm  Optimization-----------------")
        start_time = time.time()

        self.dist = self.calPathDist( self.path.random_path )
        path = self.updateBestPath(self.path.random_path)
        print("distance:", '{:.4f}'.format( self.calPathDist(path) ) )
        print("time:", '{:.4f}'.format(time.time() - start_time) )

        func_list =[]
        p1 = multiprocessing.Process(target = self.draw, args =(path,))
        p2 = multiprocessing.Process(target = self.paint.draw)
        func_list.append(p1)
        func_list.append(p2)
        for f in func_list:
            f.start()
        #self.draw(bestPath)

'''
        if self.calPathDist(path1) <= self.calPathDist(path2):
            return True
        return False
'''