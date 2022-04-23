import numpy as np
import matplotlib.pyplot as plt
def f(x):
  return 5-x
xlist=np.linspace(-1,6,1000)
ylist=f(xlist)
plt.plot(xlist,ylist)
plt.plot(5,0,marker="o",markeredgecolor="red",markerfacecolor="green")
plt.plot(3,2,marker="o",markeredgecolor="red",markerfacecolor="green")
plt.plot(0,5,marker="o",markeredgecolor="red",markerfacecolor="green")
plt.grid(b=True,axis="both")
plt.show()