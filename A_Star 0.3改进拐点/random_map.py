import numpy as np

import point

class RandomMap:
    def __init__(self, size=40): 
        self.size = size
        self.obstacle = size//8#障碍
        self.obstacle_point = []
        self.GenerateVerticalBar()
        self.GenerateObstacle()
        
    
    def GenerateVerticalBar(self):
        
        h1 =self.size//4
        h2 = 2*(self.size//3)
        for k in range( h1, h1+8):
            self.obstacle_point.append(point.Point(h1, k))
            self.obstacle_point.append(point.Point(h2, k))
        
        for j in range(h2, h2+8):
            self.obstacle_point.append(point.Point(h1, j))
            self.obstacle_point.append(point.Point(h2, j))


    def GenerateObstacle(self):
        self.obstacle_point.append(point.Point(self.size//2, self.size//2))
        self.obstacle_point.append(point.Point(self.size//2, self.size//2-1))

        # Generate an obstacle in the middle
        for i in range(self.size//2-4, self.size//2): 
            self.obstacle_point.append(point.Point(i, self.size-i))
            self.obstacle_point.append(point.Point(i, self.size-i-1))
            self.obstacle_point.append(point.Point(self.size-i, i))
            self.obstacle_point.append(point.Point(self.size-i, i-1))
        
        for i in range(self.obstacle-1): 
            x = np.random.randint(0, self.size)
            y = np.random.randint(0, self.size)
            self.obstacle_point.append(point.Point(x, y))

            if (np.random.rand() > 0.5): # Random boolean 
                for l in range(self.size//4):
                    self.obstacle_point.append(point.Point(x, y+l))
                    pass
            else:
                for l in range(self.size//4):
                    self.obstacle_point.append(point.Point(x+l, y))
                    pass

    def IsObstacle(self, i ,j): 
        for p in self.obstacle_point:
            if i==p.x and j==p.y:
                return True
        return False