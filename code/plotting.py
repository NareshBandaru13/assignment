import numpy as np
import matplotlib.pyplot as plt
def f(x):
  return 5-x
xlist=np.linspace(-1,6,1000)
ylist=f(xlist)
plt.plot(xlist,ylist)
plt.show()