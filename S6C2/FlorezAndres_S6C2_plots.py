import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import imageio

data = np.genfromtxt("datos.dat",delimiter=",")


plt.figure(0,figsize=(10,10))
plt.plot(data[:,0],data[:,1], label='Sistema')
plt.title('Condicion inicial del Sistema')
plt.ylabel('Amplitud')
plt.xlabel('x en tiempo = 0')


plt.legend(loc = 0)
plt.grid()
plt.savefig('FlorezAndres.png')