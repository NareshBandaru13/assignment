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
plt.text(5,0,'M')
plt.text(3,2,'P')
plt.text(0,5,'N')
plt.grid(b=True,axis="both")
plt.show()