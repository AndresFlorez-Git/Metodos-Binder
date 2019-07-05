import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("datos.dat",delimiter=",")

plt.figure(0,figsize=(10,10))
plt.plot(data[:,0],data[:,2], label='Posición')

plt.title('Posición de la masa en función del tiempo')
plt.xlabel('tiempo [s]')
plt.ylabel('Posición [m]')
plt.legend(loc = 0)
plt.grid()
plt.savefig('FlorezAndresResorte.png')