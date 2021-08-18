import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle


plt.figure(figsize=(15, 15))

    
size_t = 50
ax = plt.gca()
ax.set_xlim([0, size_t]) 
ax.set_ylim([0, size_t])

for i in range(0, size_t, 10): 
    for j in range(0, size_t, 20):
        if i%2 ==0:
            rec = Rectangle((i, j), width=1, height=1, color='gray')
            ax.add_patch(rec)
        else:
            rec = Rectangle((i, j), width=1, height=1, edgecolor='gray',  facecolor='w')
            ax.add_patch(rec)

# rec = Rectangle((0, 0), width = 1, height = 1, facecolor='#1d953f')
ax.add_patch(rec)
plt.axis('equal') 
plt.axis('off')
plt.tight_layout()

for i in range(1, 5):
    x = range(0, i)
    y = range(0, i) 
    y = np.array(y) * i
    patch_list=[]
    rec = Rectangle((i+1, i+4), width = 1, height = 1, facecolor='#1d953f')
    patch_list.append(rec)
    ax.add_patch(rec)
    plt.savefig("./test_%d.png" % i)
    [p.remove() for p in patch_list]

y_value =[i for i in range(10)]
i =0
for p in  y_value:
    if i %2 ==0:
        print(p)
    i=i+1
    # plt.cla()
    # plt.close()