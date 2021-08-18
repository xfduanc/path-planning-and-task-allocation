import sys
import numpy as np
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        if( x > y):
            self.x = y
            self.y = x
        else:
            self.x = x
            self.y = y



cities1 = np.array([[300,0],
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


cities2 = np.array ([[6734, 1453],
[2233, 10],
 [5530, 1424],
 [401, 841],
 [3082, 1644],
 [7608 ,4458],
 [7573 ,3716],
 [7265, 1268],
 [6898, 1885],
 [1112, 2049],
 [5468 ,2606],
 [5989 ,2873],
 [4706 ,2674],
 [4612 ,2035],
 [6347 ,2683],
 [6107 ,669],
 [7611, 5184],
 [7462 ,3590],
 [7732 ,4723],
 [5900 ,3561],
 [4483, 3369],
 [6101 ,1110],
 [5199 ,2182],
 [1633 ,2809],
 [4307 ,2322],
 [675, 1006],
 [7555, 4819],
 [7541, 3981],
 [3177 ,756],
 [7352 ,4506],
 [7545, 2801],
 [3245 ,3305],
 [6426, 3173],
 [4608 ,1198],
 [23, 2216],
 [7248, 3779],
 [7762 ,4595],
 [7392 ,2244],
 [3484, 2829],
 [6271, 2135],
 [4985, 140],
 [1916, 1569],
 [7280 ,4899],
 [7509, 3239],
 [10 ,2676],
 [6807 ,2993],
 [5185 ,3258],
 [3023 ,1942]])


cities0 = np.array([
        [256, 121], 
        [264, 715], 
        [225, 605],
        [168, 538],
        [210, 455],
        [120, 400],
        [96, 304],
        [10,451],
        [162, 660],
        [110, 561],
        [105, 473]
        ])

cities_list =[]
cities_list.append(cities0)
cities_list.append(cities1)
cities_list.append(cities2)


if __name__ == '__main__':
    print(cities_list[1][:,0])
    plt.title('Graph C')
    plt.scatter(cities_list[2][:,0], cities_list[2][:,1], color='#900302',marker='*',linestyle='-')
    plt.show()

    
    ax1 = plt.subplot(121)
    ax1.plot(cities_list[0][:,0], cities_list[0][:,1], color='red',marker='*',linestyle='-')
    plt.title("A")
    ax2 = plt.subplot(122)
    ax2.plot(cities_list[1][:,0], cities_list[1][:,1], color='green',marker='*',linestyle='-')
    plt.title("B")
    plt.suptitle("Circuit Graph")
    plt.show()


