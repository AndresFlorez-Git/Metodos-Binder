import numpy as np
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------------------------------
#Se Importan los datos
#------------------------------------------------------------------------------------------------------

Euler1 = np.genfromtxt("Euler1.dat",delimiter=",")
Euler2 = np.genfromtxt("Euler2.dat",delimiter=",")
Euler3 = np.genfromtxt("Euler3.dat",delimiter=",")

LeapFrog1 = np.genfromtxt("LeapFrog1.dat",delimiter=",")
LeapFrog2 = np.genfromtxt("LeapFrog2.dat",delimiter=",")
LeapFrog3 = np.genfromtxt("LeapFrog3.dat",delimiter=",")

RK1 = np.genfromtxt("RK1.dat",delimiter=",")
RK2 = np.genfromtxt("RK2.dat",delimiter=",")
RK3 = np.genfromtxt("RK3.dat",delimiter=",")

#------------------------------------------------------------------------------------------------------
#Figura de Posición Orbital
#------------------------------------------------------------------------------------------------------

plt.figure(0,figsize=(20,20))
plt.subplot(3,3,1)
plt.plot(Euler1[:,1],Euler1[:,2],c = 'blue', label ='Euler')
plt.title('Euler, Posición orbital dt = 0.01')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,2)
plt.plot(Euler2[:,1],Euler2[:,2],c = 'green', label ='Euler')
plt.title('Euler, Posición orbital dt = 0.001')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,3)
plt.plot(Euler3[:,1],Euler3[:,2],c = 'red', label ='Euler')
plt.title('Euler, Posición orbital dt = 0.0001')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)
#----------------------------------------------------
plt.subplot(3,3,4)
plt.plot(LeapFrog1[:,1],LeapFrog1[:,2],c = 'blue', label ='LeapFrog')
plt.title('LeapFrog , Posición orbital dt = 0.01')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,5)
plt.plot(LeapFrog2[:,1],LeapFrog2[:,2],c = 'green', label ='LeapFrog')
plt.title('LeapFrog, Posición orbital dt = 0.001')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,6)
plt.plot(LeapFrog3[:,1],LeapFrog3[:,2],c = 'red', label ='LeapFrog')
plt.title('LeapFrog, Posición orbital dt = 0.0001')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)
#----------------------------------------------------
plt.subplot(3,3,7)
plt.plot(RK1[:,1],RK1[:,2],c = 'blue', label ='Runge-Kutta')
plt.title('Runge-Kutta, Posición orbital dt = 0.01')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,8)
plt.plot(RK2[:,1],RK2[:,2],c = 'green', label ='Runge-Kutta')
plt.title('Runge-Kutta, Posición orbital dt = 0.001')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,9)
plt.plot(RK3[:,1],RK3[:,2],c = 'red', label ='Runge-Kutta')
plt.title('Runge-Kutta, Posición orbital dt = 0.0001')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)

plt.savefig('Posicion_Orbital.png')
#------------------------------------------------------------------------------------------------------
#Figura de velocidad orbital
#------------------------------------------------------------------------------------------------------
plt.figure(1,figsize=(20,20))
plt.subplot(3,3,1)
plt.plot(Euler1[:,3],Euler1[:,4],c = 'blue', label ='Euler')
plt.title('Euler, Velocidad orbital dt = 0.01')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,2)
plt.plot(Euler2[:,3],Euler2[:,4],c = 'green', label ='Euler')
plt.title('Euler, Velocidad orbital dt = 0.001')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,3)
plt.plot(Euler3[:,3],Euler3[:,4],c = 'red', label ='Euler')
plt.title('Euler, Velocidad orbital dt = 0.0001')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)
#----------------------------------------------------
plt.subplot(3,3,4)
plt.plot(LeapFrog1[:,3],LeapFrog1[:,4],c = 'blue', label ='LeapFrog')
plt.title('LeapFrog , Velocidad orbital dt = 0.01')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,5)
plt.plot(LeapFrog2[:,3],LeapFrog2[:,4],c = 'green', label ='LeapFrog')
plt.title('LeapFrog, Velocidad orbital dt = 0.001')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,6)
plt.plot(LeapFrog3[:,3],LeapFrog3[:,4],c = 'red', label ='LeapFrog')
plt.title('LeapFrog, Velocidad orbital dt = 0.0001')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)
#----------------------------------------------------
plt.subplot(3,3,7)
plt.plot(RK1[:,3],RK1[:,4],c = 'blue', label ='Runge-Kutta')
plt.title('Runge-Kutta, Velocidad orbital dt = 0.01')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,8)
plt.plot(RK2[:,3],RK2[:,4],c = 'green', label ='Runge-Kutta')
plt.title('Runge-Kutta, Velocidad orbital dt = 0.001')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,9)
plt.plot(RK3[:,3],RK3[:,4],c = 'red', label ='Runge-Kutta')
plt.title('Runge-Kutta, Velocidad orbital dt = 0.0001')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)

plt.savefig('Velocidad_Orbital.png')


#------------------------------------------------------------------------------------------------------
#Momentum Angular
#------------------------------------------------------------------------------------------------------






