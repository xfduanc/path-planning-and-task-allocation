#coding: utf-8

import numpy as np 
import matplotlib.pyplot as plt 
import numpy
import pp,time
import LRU_Cache
import point
import opt_swap_one
import multiprocessing
import opt_swap

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
        s = numpy.random.randint(1, len_t)#[low,high)
        ##选出一组可以随机reverse的start和end
        while True:
            e = numpy.random.randint(1, len_t)
            if numpy.abs(s - e) >= 1:
                break
        if s > e:
            tmp = s
            s = e
            e = tmp
        return s,e
    ##########################################
    def get_reverse_path_and_compare(self, path):
        path_origin = path.copy()
        max_index = len(path) -1
        s_last =None
        e_last =None
        loop = 100
        first, second =False,False
        for i in range(2):
            s,e = self.get_opt(max_index)
            if( i == 0):
                s_last, e_last = s,e
            else:
                while(loop > 0):
                    if( e <= s_last or s >=e_last ):
                        break
                    s,e = self.get_opt(max_index)
                    loop -= 1
                if( loop == 0 ):
                    return path
            p1, p2, p3, p4 = self.set_point(s, e, path)
        
            if self.calc_two_distance(p1, p2, p3, p4):
                path[s:e+1] = path[s:e+1][::-1]
                self.count  = 0
            else:
                if( i == 0):
                    first = True
                else:
                    second = True
            if (first and second ):
                self.count += 1 
        return path

    def set_point(self, s, e, path):
        p1 = point.Point(path[s-1], path[s])
        p2 = point.Point(path[e], path[e+1])

        p3 = point.Point(path[s-1], path[e])
        p4 = point.Point(path[s], path[e+1])
        return p1, p2 ,p3, p4
    

    # 不断优化，得到一个最终的最短的路径
    def update_path(self, path):
        while self.count < self.COUNT_MAX:
            path = self.get_reverse_path_and_compare(path.copy())
        return path

    def run(self):
        print("------------------Used LRUCache And K-opt-----------------")
        start_time =time.time()
        path = self.update_path(self.path.random_path)
        print("distance:", '{:.4f}'.format( self.calculate_path_distance(path) ) )
        #使用矩阵切片，画出原始 散点图 和 优化之后的 连线图
        print("time:", '{:.4f}'.format(time.time() - start_time) )
        #show_two =multiprocessing.Process(target = plt.show, args=(path,))
        #show_two()
        self.show(path)

        
    
    def show(self, bestPath):
        # print("Used Finally Generated : ", bestPath.tolist())
        #fig = plt.figure(figsize=(10, 10), dpi=100)
        ax = plt.subplot(111, aspect='equal')
        ax.plot(self.cities[:, 0], self.cities[:, 1], 'x', color='blue')
        for i,city in enumerate(self.cities):
            ax.text(city[0], city[1], str(i))
        ax.plot(self.cities[bestPath, 0], self.cities[bestPath, 1], color='red', linewidth=0.8, linestyle=':')
        plt.title("Used LRU Cache And K-opt")#Hamiltonian circuit
        #Used LRU Cache And K-opt



        # plt.xlabel("X -Value", fontsize=14)
        # plt.ylabel("Y -Value", fontsize=14)
         
        plt.tick_params(axis='both', which='major', labelsize=14)
        plt.show()

    

        # 计算两个点的距离
    def calculate_distance(self, from_index, to_index):
        return np.sqrt( np.sum( np.power(self.cities[from_index] - self.cities[to_index], 2) ) )

    # 计算整条路径的距离
    def calculate_path_distance(self, path):
        sum = 0.0
        for i in range(1, len(path)):
            sum += self.calculate_distance(path[i-1], path[i])
        return sum
# 获取随机的起始点还有中间的反转后的路径
    def get_reverse_path_and_compare1(self, path):
        path_origin = path.copy()
        max_index = len(path) -1
        s = numpy.random.randint(1, max_index)#[low,high)
        ##选出一组可以随机reverse的start和end
        while True:
            e = numpy.random.randint(1, max_index)
            if numpy.abs(s - e) >= 1:
                break
        ##切片和[::-1]来实现逆序
        if s > e:
            tmp = s
            s = e
            e = tmp
        ### s e的坐标
        p1 = None
        p2 = None
        #if s in range(1, max_index) and e in range(1, max_index):
        p1 = point.Point(path[s-1], path[s])
        p2 = point.Point(path[e], path[e+1])

        p3 = point.Point(path[s-1], path[e])
        p4 = point.Point(path[s], path[e+1])

        if self.calc_two_distance(p1, p2, p3, p4):

            path[s:e+1] = path[s:e+1][::-1]
            self.count  = 0
            return path
        else:
            self.count += 1
            return path_origin



if __name__ == '__main__':
    
    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    cities = point.cities_list[2]
    my_path= Path(len(cities))
    loop_size = 1000
    opt_v0 = opt_swap.OptSwap(loop_size, my_path, cities)

    opt_v1 = opt_swap_one.OptSwapOne(loop_size, my_path, cities )
    
    #def __init__(self, count_max:int, path, cities, arr =[0, 500, 16, 2]):
    opt_v2 = OptSwapTwo(loop_size, my_path, cities)
    # print("Started with :", my_path.random_path.tolist())

    func_list =[]
    p1 = multiprocessing.Process(target = opt_v0.run)
    p2 = multiprocessing.Process(target = opt_v1.run)
    p3 = multiprocessing.Process(target = opt_v2.run)
    func_list.append(p1)
    func_list.append(p2)
    func_list.append(p3)
    for f in func_list:
        pass
        f.start()



