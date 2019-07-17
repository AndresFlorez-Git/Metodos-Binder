import numpy as np
import matplotlib.pyplot as plt

Euler1 = np.genfromtxt("Euler1.dat",delimiter=",")
Euler2 = np.genfromtxt("Euler2.dat",delimiter=",")
Euler3 = np.genfromtxt("Euler3.dat",delimiter=",")



RK1 = np.genfromtxt("RK1.dat",delimiter=",")
RK2 = np.genfromtxt("RK2.dat",delimiter=",")
RK3 = np.genfromtxt("RK3.dat",delimiter=",")



plt.figure(0,figsize=(20,20))
plt.subplot(3,3,1)
plt.plot(Euler1[:,0],Euler1[:,1],c = 'blue', label ='Euler')
plt.title('Euler, Posición orbital dt = 0.001')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,2)
plt.plot(Euler2[:,0],Euler2[:,1],c = 'green', label ='Euler')
plt.title('Euler, Posición orbital dt = 0.0001')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,3)
plt.plot(Euler3[:,0],Euler3[:,1],c = 'red', label ='Euler')
plt.title('Euler, Posición orbital dt = 0.00001')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)
#----------------------------------------------------
plt.subplot(3,3,7)
plt.plot(RK1[:,1],RK1[:,2],c = 'blue', label ='Runge-Kutta')
plt.title('Runge-Kutta, Posición orbital dt = 0.001')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,8)
plt.plot(RK2[:,1],RK2[:,2],c = 'green', label ='Runge-Kutta')
plt.title('Runge-Kutta, Posición orbital dt = 0.0001')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,9)
plt.plot(RK3[:,1],RK3[:,2],c = 'red', label ='Runge-Kutta')
plt.title('Runge-Kutta, Posición orbital dt = 0.00001')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)

plt.savefig('FlorezAndres.png')