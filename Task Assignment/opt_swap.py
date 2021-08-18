#coding: utf-8

import numpy as np 
import matplotlib.pyplot as plt 
import numpy.random as random
import time
import scatter
import multiprocessing
# 600*600的

# 2-opt算法 #                 
COUNT_MAX = 520

class OptSwap:
    #def __init__(self, count_max:int, path, cities, arr =[0, 500, 16, 2]):
    def __init__(self, max_loop:int, path, cities):
        self.COUNT_MAX = max_loop
        self.cities = cities
        self.path = path #随机路径
        self.paint =None
        
    # 因为自己造的输入数据可能是最佳路径，所以先获取一个随机的路线（任选一个可行解）
    def get_random_path(self, best_path):
        random.shuffle(best_path)
        path = np.append(best_path, best_path[0])
        return path

    # 计算两个点的距离
    def calculate_distance(self, from_index, to_index):
        return np.sqrt(np.sum(np.power(self.cities[from_index] - self.cities[to_index], 2)))

  # 计算整条路径的距离
    def calculate_path_distance(self, path):
        sum = 0.0
        for i in range(1, len(path)):
            sum += self.calculate_distance(path[i-1], path[i])
        return sum

  # 获取随机的起始点还有中间的反转后的路径
    def get_reverse_path(self, path):
        start = random.randint(1, len(path) - 1)
        while True:
            end = random.randint(1, len(path) - 1)
            if np.abs(start - end) > 1:
                break

        if start > end:
            path[end: start+1] = path[end: start+1][::-1]
            return path
        else:
            path[start: end+1] = path[start: end+1][::-1]
            return path

  # 比较两个路径的长短
    def compare_paths(self, path_one, path_two):
        dist_one = self.calculate_path_distance(path_one)
        dist_two = self.calculate_path_distance(path_two)
        self.dist = dist_one if dist_one <= dist_two else dist_two 
        return dist_one > dist_two
        #return self.calculate_path_distance(path_one) > self.calculate_path_distance(path_two)

  # 不断优化，得到一个最终的最短的路径
    def update_path(self, path):
        count = 0
        loop = 0
        self.paint = scatter.Scatter("Origin 2-opt", 0)
        while count < self.COUNT_MAX:
            reverse_path = self.get_reverse_path(path.copy())
            if self.compare_paths(path, reverse_path):
                count = 0
                path = reverse_path
            else:
                count += 1
                continue
            self.paint.append(loop, self.dist)
            loop +=1
        return path

    def run(self):
        start_time =time.time()
        print("------------------Original 2-opt-----------------")
        self.dist = self.calculate_path_distance( self.path.random_path )
        path = self.update_path(self.path.random_path)

        print("distance:", '{:.4f}'.format( self.calculate_path_distance(path) ) )
        print("time:", '{:.4f}'.format(time.time() - start_time) )

        func_list =[]
        p1 = multiprocessing.Process(target = self.show_three, args =(path,))
        p2 = multiprocessing.Process(target = self.paint.draw)
        func_list.append(p1)
        func_list.append(p2)
        for f in func_list:
            f.start()
    
    def show_three(self, bestPath):
        print("Befoed Finally Generated : ", bestPath.tolist())
        #fig = plt.figure(figsize=(10, 10), dpi=100)
        ax = plt.subplot(111, aspect='equal')
        ax.plot(self.cities[:, 0], self.cities[:, 1], 'x', color='blue')
        for i,city in enumerate(self.cities):
            ax.text(city[0], city[1], str(i))
        ax.plot(self.cities[bestPath, 0], self.cities[bestPath, 1], color='red', linewidth=0.8, linestyle=':')
        plt.title("Origin 2-opt")

        plt.xlabel("X -Value", fontsize=14)
        plt.ylabel("Y -Value", fontsize=14)
         
        plt.tick_params(axis='both', which='major', labelsize=14)
        plt.show()