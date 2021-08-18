#coding: utf-8

import numpy as np 
from matplotlib import pyplot as plt 
import numpy
import time
import LRU_Cache
import point
import opt_swap
import multiprocessing
import opt_swap_one
import scatter

# 600*600的



# 2-opt算法 #                 

# 因为自己造的输入数据可能是最佳路径，所以先获取一个随机的路线（任选一个可行解）

class Path:
    def __init__(self, size_t:int):
        self.random_path = self.get_random_path(size_t)

    def get_random_path(self, size_t:int):
        path = np.arange( size_t )
        np.random.shuffle(path)
        return np.append(path, path[0])


##############################################
class OptSwapTwo:
    #第一个参数为默认的循环次数，第二个参数列表为生成地图的大小和维度
    def __init__(self, count_max:int, path:list, cities):
        self.COUNT_MAX = count_max
        self.cities = cities #numpy.random.randint(arr[0], arr[1], (arr[2], arr[3]) )
        self.lru = LRU_Cache.LRUCache(len(path.random_path)*len(path.random_path)/2, self.cities)
        self.count = 0
        self.path = path
        self.tup = (0,)


    # 计算整条路径的距离
    def calc_two_distance(self, p1, p2, p3, p4)->bool:
        
        return (self.lru.get(p1) + self.lru.get(p2) ) > (self.lru.get(p3) +self.lru.get(p4) )
    
    def calc_one_distance(self, p1, p2)->bool:
        
        return self.lru.get(p1)  > self.lru.get(p2)
    
    def get_opt(self, len_t:int):
        loop = 100
        while loop >0:
            s = numpy.random.randint(1, len_t)#[low,high)
            ##选出一组可以随机reverse的start和end
            while True:
                e = numpy.random.randint(1, len_t)
                if numpy.abs(s - e) > 1:
                    break
            if s > e:
                tmp = s
                s = e
                e = tmp
            if s > max( self.tup )  or e < min( self.tup):
                my_tup =(s, e)
                self.tup +=my_tup
                return s, e
            else:
                loop -= 1
                continue
        return None,None


    def generateRandomPoint(self, max_index):
        s = numpy.random.randint(1, max_index)#[low,high)
        ##选出一组可以随机reverse的start和end
        while True:
            e = numpy.random.randint(1, max_index)
            if numpy.abs(s - e) > 1:
                break
        ##切片和[::-1]来实现逆序
        if s > e:
            tmp = s
            s = e
            e = tmp
        return s,e    ### s e的坐标

    # 不断优化，得到一个最终的最短的路径
    def update_path(self, path):
        loop = 0
        count = 0
        self.paint = scatter.Scatter("Used LRU Cache And 2-opt", 2)
        max_index = len(path)-1
        while count < self.COUNT_MAX:
            s, e = self.generateRandomPoint(max_index)
            p1 = point.Point(path[s-1], path[s])
            p2 = point.Point(path[e], path[e+1])

            p3 = point.Point(path[s-1], path[e])
            p4 = point.Point(path[s], path[e+1])

            if self.calc_two_distance(p1, p2, p3, p4):
                path[s:e+1] = path[s:e+1][::-1]
                count  = 0
                self.dist = self.calculate_path_distance(path)
            else:
                count += 1
                continue
            self.paint.append(loop, self.dist)
            loop +=1
        return path

    def run(self):
        print("------------------Used LRUCache And 2-opt-----------------")
        start_time =time.time()

        self.dist = self.calculate_path_distance( self.path.random_path )
        path = self.update_path(self.path.random_path)
        print("distance:", '{:.4f}'.format( self.calculate_path_distance(path) ) )
        #使用矩阵切片，画出原始 散点图 和 优化之后的 连线图
        print("time:", '{:.4f}'.format(time.time() - start_time) )

        func_list =[]
        #p1 = multiprocessing.Process(target = self.show, args =(path,))
        p2 = multiprocessing.Process(target = self.paint.draw)
        #func_list.append(p1)
        func_list.append(p2)
        

        self.show(path)
        for f in func_list:
            f.start()

        
    
    def show(self, bestPath):
        print("Used Finally Generated : ", bestPath.tolist())
        #fig = plt.figure(figsize=(10, 10), dpi=100)
        ax = plt.subplot(111, aspect='equal')
        ax.plot(self.cities[:, 0], self.cities[:, 1], 'x', color='blue')
        for i,city in enumerate(self.cities):
            ax.text(city[0], city[1], str(i))
        ax.plot(self.cities[bestPath, 0], self.cities[bestPath, 1], color='red', linewidth=0.8, linestyle=':')
        plt.title("Used LRU Cache And 2-opt")

        plt.xlabel("X -Value", fontsize=14)
        plt.ylabel("Y -Value", fontsize=14)
         
        plt.tick_params(axis='both', which='major', labelsize=14)
        plt.show()

    

        # 计算两个点的距离
    def calculate_distance(self, from_index, to_index):
        return np.sqrt(np.sum(np.power(self.cities[from_index] - self.cities[to_index], 2)))

    # 计算整条路径的距离
    def calculate_path_distance(self, path):
        sum = 0.0
        for i in range(1, len(path)):
            sum += self.calculate_distance(path[i-1], path[i])
        return sum


if __name__ == '__main__':
    
    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    cities = point.cities_list[0]
    my_path= Path(len(cities))
    max_loop = 2000

    opt_v0 = opt_swap.OptSwap(max_loop, my_path, cities)

    opt_v1 = opt_swap_one.OptSwapOne(max_loop, my_path, cities )
    
    #def __init__(self, count_max:int, path, cities, arr =[0, 500, 16, 2]):
    opt_v2 = OptSwapTwo(max_loop, my_path, cities)
    print("Started with :", my_path.random_path.tolist())

    func_list =[]
    p1 = multiprocessing.Process(target = opt_v0.run)
    p2 = multiprocessing.Process(target = opt_v1.run)
    p3 = multiprocessing.Process(target = opt_v2.run)
    func_list.append(p1)
    func_list.append(p2)
    func_list.append(p3)

    for f in func_list:
        f.start()