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
plt.ylabel('VY [UA/yr]')
plt.xlabel('VX [UA/yr]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,2)
plt.plot(Euler2[:,3],Euler2[:,4],c = 'green', label ='Euler')
plt.title('Euler, Velocidad orbital dt = 0.001')
plt.ylabel('VY [UA/yr]')
plt.xlabel('VX [UA/yr]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,3)
plt.plot(Euler3[:,3],Euler3[:,4],c = 'red', label ='Euler')
plt.title('Euler, Velocidad orbital dt = 0.0001')
plt.ylabel('VY [UA/yr]')
plt.xlabel('VX [UA/yr]')
plt.grid()
plt.legend(loc=0)
#----------------------------------------------------
plt.subplot(3,3,4)
plt.plot(LeapFrog1[:,3],LeapFrog1[:,4],c = 'blue', label ='LeapFrog')
plt.title('LeapFrog , Velocidad orbital dt = 0.01')
plt.ylabel('VY [UA/yr]')
plt.xlabel('VX [UA/yr]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,5)
plt.plot(LeapFrog2[:,3],LeapFrog2[:,4],c = 'green', label ='LeapFrog')
plt.title('LeapFrog, Velocidad orbital dt = 0.001')
plt.ylabel('VY [UA/yr]')
plt.xlabel('VX [UA/yr]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,6)
plt.plot(LeapFrog3[:,3],LeapFrog3[:,4],c = 'red', label ='LeapFrog')
plt.title('LeapFrog, Velocidad orbital dt = 0.0001')
plt.ylabel('VY [UA/yr]')
plt.xlabel('VX [UA/yr]')
plt.grid()
plt.legend(loc=0)
#----------------------------------------------------
plt.subplot(3,3,7)
plt.plot(RK1[:,3],RK1[:,4],c = 'blue', label ='Runge-Kutta')
plt.title('Runge-Kutta, Velocidad orbital dt = 0.01')
plt.ylabel('VY [UA/yr]')
plt.xlabel('VX [UA/yr]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,8)
plt.plot(RK2[:,3],RK2[:,4],c = 'green', label ='Runge-Kutta')
plt.title('Runge-Kutta, Velocidad orbital dt = 0.001')
plt.ylabel('VY [UA/yr]')
plt.xlabel('VX [UA/yr]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,9)
plt.plot(RK3[:,3],RK3[:,4],c = 'red', label ='Runge-Kutta')
plt.title('Runge-Kutta, Velocidad orbital dt = 0.0001')
plt.ylabel('VY [UA/yr]')
plt.xlabel('VX [UA/yr]')
plt.grid()
plt.legend(loc=0)

plt.savefig('Velocidad_Orbital.png')


#------------------------------------------------------------------------------------------------------
#Momentum Angular
#------------------------------------------------------------------------------------------------------
M = 1.989*10**30 # Masa del sol [kg]
Mearth = 5.972*10**24 # Masa de la tierra [kg]
Mearth_sun = Mearth/M # Masa de la tierra [masas solares]

# Componente Z de la posicion tanto como de la velocidad
ZEuler1 = np.zeros(len(Euler1[:,1]))
ZEuler2 = np.zeros(len(Euler2[:,1]))
ZEuler3 = np.zeros(len(Euler3[:,1]))

ZLeapFrog1 = np.zeros(len(LeapFrog1[:,1]))
ZLeapFrog2 = np.zeros(len(LeapFrog2[:,1]))
ZLeapFrog3 = np.zeros(len(LeapFrog3[:,1]))

ZRK1 = np.zeros(len(RK1[:,1]))
ZRK2 = np.zeros(len(RK2[:,1]))
ZRK3 = np.zeros(len(RK3[:,1]))

# Vector r (x,y,z)

rEuler1 = np.array([Euler1[:,1],Euler1[:,2],ZEuler1]).T
rEuler2 = np.array([Euler2[:,1],Euler2[:,2],ZEuler2]).T
rEuler3 = np.array([Euler3[:,1],Euler3[:,2],ZEuler3]).T

rLeapFrog1 = np.array([LeapFrog1[:,1],LeapFrog1[:,2],ZLeapFrog1]).T
rLeapFrog2 = np.array([LeapFrog2[:,1],LeapFrog2[:,2],ZLeapFrog2]).T
rLeapFrog3 = np.array([LeapFrog3[:,1],LeapFrog3[:,2],ZLeapFrog3]).T

rRK1 = np.array([RK1[:,1],RK1[:,2],ZRK1]).T
rRK2 = np.array([RK2[:,1],RK2[:,2],ZRK2]).T
rRK3 = np.array([RK3[:,1],RK3[:,2],ZRK3]).T

# Vector v (vx, vy, vz)

vEuler1 = np.array([Euler1[:,3],Euler1[:,4],ZEuler1]).T
vEuler2 = np.array([Euler2[:,3],Euler2[:,4],ZEuler2]).T
vEuler3 = np.array([Euler3[:,3],Euler3[:,4],ZEuler3]).T

vLeapFrog1 = np.array([LeapFrog1[:,3],LeapFrog1[:,4],ZLeapFrog1]).T
vLeapFrog2 = np.array([LeapFrog2[:,3],LeapFrog2[:,4],ZLeapFrog2]).T
vLeapFrog3 = np.array([LeapFrog3[:,3],LeapFrog3[:,4],ZLeapFrog3]).T

vRK1 = np.array([RK1[:,3],RK1[:,4],ZRK1]).T
vRK2 = np.array([RK2[:,3],RK2[:,4],ZRK2]).T
vRK3 = np.array([RK3[:,3],RK3[:,4],ZRK3]).T

# momento angular L = r x v

Momentum_Angular_Euler1 = np.cross(rEuler1,vEuler1*Mearth_sun)
Momentum_Angular_Euler2 = np.cross(rEuler2,vEuler2*Mearth_sun)
Momentum_Angular_Euler3 = np.cross(rEuler3,vEuler3*Mearth_sun)

Momentum_Angular_LeapFrog1 = np.cross(rLeapFrog1,vLeapFrog1*Mearth_sun)
Momentum_Angular_LeapFrog2 = np.cross(rLeapFrog2,vLeapFrog2*Mearth_sun)
Momentum_Angular_LeapFrog3 = np.cross(rLeapFrog3,vLeapFrog3*Mearth_sun)

Momentum_Angular_RK1 = np.cross(rRK1,vRK1*Mearth_sun)
Momentum_Angular_RK2 = np.cross(rRK2,vRK2*Mearth_sun)
Momentum_Angular_RK3 = np.cross(rRK3,vRK3*Mearth_sun)


#------------------------------------------------------------------------------------------------------
#figura de Momentum Angular
#------------------------------------------------------------------------------------------------------

plt.figure(2,figsize=(30,30))
plt.subplot(3,3,1)
plt.plot(Euler1[:,0],Momentum_Angular_Euler1[:,2],c = 'blue', label ='Euler')
plt.title('Euler, Momentum Angular dt = 0.01')
plt.ylabel('Momentum Angular [$M_{solar}$$UA^{2}$/yr]')
plt.xlabel('t [yr]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,2)
plt.plot(Euler2[:,0],Momentum_Angular_Euler2[:,2],c = 'green', label ='Euler')
plt.title('Euler, Momentum Angular dt = 0.001')
plt.ylabel('Momentum Angular [$M_{solar}$$UA^{2}$/yr]')
plt.xlabel('t [yr]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,3)
plt.plot(Euler3[:,0],Momentum_Angular_Euler3[:,2],c = 'red', label ='Euler')
plt.title('Euler, Momentum Angular dt = 0.0001')
plt.ylabel('Momentum Angular [$M_{solar}$$UA^{2}$/yr]')
plt.xlabel('t [yr]')
plt.grid()
plt.legend(loc=0)
#----------------------------------------------------
plt.subplot(3,3,4)
plt.plot(LeapFrog1[:,0],Momentum_Angular_LeapFrog1[:,2],c = 'blue', label ='LeapFrog')
plt.title('LeapFrog, Momentum Angular dt = 0.01')
plt.ylabel('Momentum Angular [$M_{solar}$$UA^{2}$/yr]')
plt.xlabel('t [yr]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,5)
plt.plot(LeapFrog2[:,0],Momentum_Angular_LeapFrog2[:,2],c = 'green', label ='LeapFrog')
plt.title('LeapFrog, Momentum Angular dt = 0.001')
plt.ylabel('Momentum Angular [$M_{solar}$$UA^{2}$/yr]')
plt.xlabel('t [yr]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,6)
plt.plot(LeapFrog3[:,0],Momentum_Angular_LeapFrog3[:,2],c = 'red', label ='LeapFrog')
plt.title('LeapFrog, Momentum Angular dt = 0.0001')
plt.ylabel('Momentum Angular [$M_{solar}$$UA^{2}$/yr]')
plt.xlabel('t [yr]')
plt.grid()
plt.legend(loc=0)
#----------------------------------------------------
plt.subplot(3,3,7)
plt.plot(RK1[:,0],Momentum_Angular_RK1[:,2],c = 'blue', label ='RK')
plt.title('RK, Momentum Angular dt = 0.01')
plt.ylabel('Momentum Angular [$M_{solar}$$UA^{2}$/yr]')
plt.xlabel('t [yr]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,8)
plt.plot(RK2[:,0],Momentum_Angular_RK2[:,2],c = 'green', label ='RK')
plt.title('RK, Momentum Angular dt = 0.001')
plt.ylabel('Momentum Angular [$M_{solar}$$UA^{2}$/yr]')
plt.xlabel('t [yr]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,9)
plt.plot(RK3[:,0],Momentum_Angular_RK3[:,2],c = 'red', label ='RK')
plt.title('RK, Momentum Angular dt = 0.0001')
plt.ylabel('Momentum Angular [$M_{solar}$$UA^{2}$/yr]')
plt.xlabel('t [yr]')
plt.grid()
plt.legend(loc=0)

plt.savefig('Momentum_Angular.png')





