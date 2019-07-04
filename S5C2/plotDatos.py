import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("datos.dat",delimiter=",")

plt.figure(0,figsize=(10,10))
plt.plot(data[:,0],data[:,1], label='Función')
plt.title('Implementacion de Euler')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc = 0)
plt.grid()
plt.savefig('plotEuler.png')