import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("datos.dat",delimiter=",")


plt.figure(0,figsize=(10,10))
plt.plot(data[0:1500,1],data[0:1500,2])
plt.title('Condicion inicial del Sistema')
plt.ylabel('Amplitud')
plt.xlabel('x en tiempo = 0')


plt.legend(loc = 0)
plt.grid()
plt.savefig('FlorezAndres.png')