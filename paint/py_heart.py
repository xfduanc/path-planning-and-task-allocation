import matplotlib.pyplot as plt
import numpy as np
import math
pi = math.pi
t = np.arange(0,2*pi,0.001)
r = np.frompyfunc(round,1,1)
sin = np.frompyfunc(math.sin,1,1)
cos = np.frompyfunc(math.cos,1,1)
#y = sin(x)*(abs(cos(x)))**0.5/(sin(x)+1.4)-2*sin(x)+2
'''
y = 2*cos(t)-cos(2*t)
x = 2*sin(t)-sin(2*t)
'''
x=sin(t)
c=cos(t)
p=x**2
y=c+p**(1/3)
print(x, y)
plt.plot(x, y,color='r', linewidth=9)
plt.fill(x,y,color='r')
plt.title("mu zi ke ren")
ax = plt.subplot(111)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
plt.xlim(-1.2,1.2),plt.xticks([])
plt.yticks([])
plt.show()