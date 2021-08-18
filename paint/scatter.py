import matplotlib.pyplot as plt
import numpy as np

'''
plt.scatter(np.arange(100), np.arange(100))
 
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
 
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()
'''


''' 
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, s=100)
 
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
 
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()
'''

'''
x^2+y^2+a*x=a*sqrt(x^2+y^2)

x^2+y^2-a*x=a*sqrt(x^2+y^2)
'''
import point

class Scatter:
    def __init__(self, path):
        self.path = path
        self.x_values = []
        self.y_values = []
        pass
    def draw(self):
        for p in self.path:
            self.x_values.append(p.x)
            self.y_values.append(p.y)
        plt.scatter(self.x_values, self.y_values, c="red", edgecolor ='none', s=1)

        #plt.title("Square Numbers", fontsize=24)
        #plt.xlabel("Value", fontsize=14)
        #plt.ylabel("Square of Value", fontsize=14)

        #plt.tick_params(axis='both', which='major', labelsize=14)

        #plt.axis([0, 1100, 0, 1100000])##设置坐标
        plt.show()


if __name__ == '__main__':
    cities = point.cities_list[0]
    p = Scatter(cities)
    p.draw()

