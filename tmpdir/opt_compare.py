#coding: utf-8

import numpy as np 
import matplotlib.pyplot as plt 
import numpy.random as random 

# 600*600的
cities = np.array([[300,0],
                  [400, 50],
                  [450, 100],
                  [500, 200],
                  [550, 300],
                  [600, 400],
                  [500, 500],
                  [400, 500],
                  [300, 400],
                  [200, 500],
                  [100, 500],
                  [0, 400],
                  [50, 300],
                  [100, 200],
                  [150, 100],
                  [200, 50]])

# 2-opt算法 #                 
COUNT_MAX = 520

# 因为自己造的输入数据可能是最佳路径，所以先获取一个随机的路线（任选一个可行解）
def get_random_path(best_path):
    random.shuffle(best_path)
    path = np.append(best_path, best_path[0])
    return path

# 计算两个点的距离
def calculate_distance(from_index, to_index):
    return np.sqrt(np.sum(np.power(cities[from_index] - cities[to_index], 2)))

# 计算整条路径的距离
def calculate_path_distance(path):
    sum = 0.0
    for i in range(1, len(path)):
        sum += calculate_distance(path[i-1], path[i])
    return sum

# 获取随机的起始点还有中间的反转后的路径
def get_reverse_path(path):
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
def compare_paths(path_one, path_two):
    return calculate_path_distance(path_one) > calculate_path_distance(path_two)

# 不断优化，得到一个最终的最短的路径
def update_path(path):
    count = 0
    while count < COUNT_MAX:
        reverse_path = get_reverse_path(path.copy())
        if compare_paths(path, reverse_path):
            count = 0
            path = reverse_path
        else:
            count += 1
    return path

def opt_2():
    best_path = np.arange(len(cities))
    best_path = get_random_path(best_path)
    path = update_path(best_path)

    print(calculate_path_distance(path))
    show(path)

def show(path):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(cities[:, 0], cities[:, 1], 'o', color='red')
    ax.plot(cities[path, 0], cities[path, 1], color='red')
    plt.show()

opt_2()