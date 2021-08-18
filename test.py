
'''import sys
#print (sys.path)
'''

import numpy as np
import numpy.random as random
'''
a = np.array(object = [[1,2,3],[],[121,21,21]], ndmin=4)

print(a)
'''
path = np.array(range(23))
def get_random_path(best_path):
    random.shuffle(best_path)
    path = np.append(best_path, best_path[0])
    return path
my_str ='time'
if my_str == 'time':
    print("10")
else:
    print("no")
# for i  in range(100):
# 	print(get_random_path(path))