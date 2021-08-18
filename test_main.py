
import numpy as np
import matplotlib.pyplot as plt
import time
import os


randomint = np.random.randint(10, 20,(2,2))
print(randomint)

print( time.strftime("Path-Img%m%d%H%M%S", time.localtime()) + " {:3d}".format( np.random.randint(100, 1000) ))
fig, axes = plt.subplots(2, 2)


#os.mkdir("tmpdir")
plt.title("A-Star")
ax1=axes[0, 0]
ax2=axes[0, 1]
ax3=axes[1, 0]
ax4=axes[1, 1]

ax2.plot(np.arange(4),color="red", linestyle="-")

plt.scatter(np.arange(4), np.arange(4))
# 在右侧底部显示子图标题
plt.title("right bottom",y=0,loc='right', pad = 30)
# 在左侧顶部显示子图标题
plt.title("left top",y=1,loc='left',c ="red")
# 显示默认子图标题
plt.title("default")
plt.show()


'''
import matplotlib.pyplot as plt

import sys
import numpy as np
from A_Star.point import Point

size = 50
for i in range(size//2):
	#print( np.random.rand(i+1) )
	print( np.random.randint(0, i+1000) )

import time

localtime = time.asctime( time.localtime( time.time()) )
print ("本地时间为 :", localtime)

fileName = time.strftime("%Y-%m-%d %H %M %S", time.localtime()) + "-{:2d}".format( np.random.randint(10, 100) )
print(  fileName)

print("{name}:{value}".format(name="duanxianfeng",value="huawei"))


import os
os.mkdir(fileName)
'''