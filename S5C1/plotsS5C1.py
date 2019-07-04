import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("data.dat",delimiter=",")

plt.figure(0,figsize=(10,10))
plt.plot(data[:,0],data[:,1],label ="función")
plt.plot(data[:,0],data[:,2],label ="derivada")
plt.title('Función y derivada')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(loc = 0)
plt.grid()
plt.savefig('S5C1PLOT.png')