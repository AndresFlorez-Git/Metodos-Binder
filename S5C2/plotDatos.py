import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("datos.dat",delimiter=",")

plt.figure(0,figsize=(10,10))
plt.plot(data[1:200,0],data[1:200,1], label='Método Euler')
plt.plot(data[202:401,0],data[202:401,1], label='Método RK')
plt.title('Implementacion numerica de ecuaciones diferenciales')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc = 0)
plt.grid()
plt.savefig('plotEuler.png')