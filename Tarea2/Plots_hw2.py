import numpy as np
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------------------------------
#Constantes Globales Necesarias
#------------------------------------------------------------------------------------------------------
G1 = 6.674e-11 #Constante de gravitacion universal [N m**2/ kg**2]
UA = 149597870700 #unidad astronomica en metros
yr = 31536000 # segundos al año
M = 1.989*10**30 # Masa del sol [kg]
G = G1*(1/(UA*UA*UA))*(M)*(yr*yr) # Constante de gravitacion universal [UA^3 /(Masa_Solar yr^2)]
Mearth = 5.972*10**24 # Masa de la tierra [kg]
Mearth_sun = Mearth/M # Masa de la tierra [masas solares]

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
plt.plot(Euler2[:,1],Euler2[:,2],c = 'blue', label ='Euler')
plt.title('Euler, Posición orbital dt = 0.001')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,3)
plt.plot(Euler3[:,1],Euler3[:,2],c = 'blue', label ='Euler')
plt.title('Euler, Posición orbital dt = 0.0001')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)
#----------------------------------------------------
plt.subplot(3,3,4)
plt.plot(LeapFrog1[:,1],LeapFrog1[:,2],c = 'green', label ='LeapFrog')
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
plt.plot(LeapFrog3[:,1],LeapFrog3[:,2],c = 'green', label ='LeapFrog')
plt.title('LeapFrog, Posición orbital dt = 0.0001')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)
#----------------------------------------------------
plt.subplot(3,3,7)
plt.plot(RK1[:,1],RK1[:,2],c = 'red', label ='Runge-Kutta')
plt.title('Runge-Kutta, Posición orbital dt = 0.01')
plt.ylabel('Y [UA]')
plt.xlabel('X [UA]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,8)
plt.plot(RK2[:,1],RK2[:,2],c = 'red', label ='Runge-Kutta')
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
plt.plot(Euler2[:,3],Euler2[:,4],c = 'blue', label ='Euler')
plt.title('Euler, Velocidad orbital dt = 0.001')
plt.ylabel('VY [UA/yr]')
plt.xlabel('VX [UA/yr]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,3)
plt.plot(Euler3[:,3],Euler3[:,4],c = 'blue', label ='Euler')
plt.title('Euler, Velocidad orbital dt = 0.0001')
plt.ylabel('VY [UA/yr]')
plt.xlabel('VX [UA/yr]')
plt.grid()
plt.legend(loc=0)
#----------------------------------------------------
plt.subplot(3,3,4)
plt.plot(LeapFrog1[:,3],LeapFrog1[:,4],c = 'green', label ='LeapFrog')
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
plt.plot(LeapFrog3[:,3],LeapFrog3[:,4],c = 'green', label ='LeapFrog')
plt.title('LeapFrog, Velocidad orbital dt = 0.0001')
plt.ylabel('VY [UA/yr]')
plt.xlabel('VX [UA/yr]')
plt.grid()
plt.legend(loc=0)
#----------------------------------------------------
plt.subplot(3,3,7)
plt.plot(RK1[:,3],RK1[:,4],c = 'red', label ='Runge-Kutta')
plt.title('Runge-Kutta, Velocidad orbital dt = 0.01')
plt.ylabel('VY [UA/yr]')
plt.xlabel('VX [UA/yr]')
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,8)
plt.plot(RK2[:,3],RK2[:,4],c = 'red', label ='Runge-Kutta')
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
plt.title('Euler, Momentum Angular dt = 0.01',fontsize = 20)
plt.ylabel('Momentum Angular [$M_{solar}$$UA^{2}$/yr]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,2)
plt.plot(Euler2[:,0],Momentum_Angular_Euler2[:,2],c = 'blue', label ='Euler')
plt.title('Euler, Momentum Angular dt = 0.001',fontsize = 20)
plt.ylabel('Momentum Angular [$M_{solar}$$UA^{2}$/yr]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,3)
plt.plot(Euler3[:,0],Momentum_Angular_Euler3[:,2],c = 'blue', label ='Euler')
plt.title('Euler, Momentum Angular dt = 0.0001',fontsize = 20)
plt.ylabel('Momentum Angular [$M_{solar}$$UA^{2}$/yr]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()
plt.legend(loc=0)
#----------------------------------------------------
plt.subplot(3,3,4)
plt.plot(LeapFrog1[:,0],Momentum_Angular_LeapFrog1[:,2],c = 'green', label ='LeapFrog')
plt.title('LeapFrog, Momentum Angular dt = 0.01',fontsize = 20)
plt.ylabel('Momentum Angular [$M_{solar}$$UA^{2}$/yr]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,5)
plt.plot(LeapFrog2[:,0],Momentum_Angular_LeapFrog2[:,2],c = 'green', label ='LeapFrog')
plt.title('LeapFrog, Momentum Angular dt = 0.001',fontsize = 20)
plt.ylabel('Momentum Angular [$M_{solar}$$UA^{2}$/yr]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,6)
plt.plot(LeapFrog3[:,0],Momentum_Angular_LeapFrog3[:,2],c = 'green', label ='LeapFrog')
plt.title('LeapFrog, Momentum Angular dt = 0.0001',fontsize = 20)
plt.ylabel('Momentum Angular [$M_{solar}$$UA^{2}$/yr]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()
plt.legend(loc=0)
#----------------------------------------------------
plt.subplot(3,3,7)
plt.plot(RK1[:,0],Momentum_Angular_RK1[:,2],c = 'red', label ='RK')
plt.title('RK, Momentum Angular dt = 0.01',fontsize = 20)
plt.ylabel('Momentum Angular [$M_{solar}$$UA^{2}$/yr]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,8)
plt.plot(RK2[:,0],Momentum_Angular_RK2[:,2],c = 'red', label ='RK')
plt.title('RK, Momentum Angular dt = 0.001',fontsize = 20)
plt.ylabel('Momentum Angular [$M_{solar}$$UA^{2}$/yr]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()
plt.legend(loc=0)

plt.subplot(3,3,9)
plt.plot(RK3[:,0],Momentum_Angular_RK3[:,2],c = 'red', label ='RK')
plt.title('RK, Momentum Angular dt = 0.0001',fontsize = 20)
plt.ylabel('Momentum Angular [$M_{solar}$$UA^{2}$/yr]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()
plt.legend(loc=0)

plt.savefig('Momentum_Angular.png')


#------------------------------------------------------------------------------------------------------
# Energía:
#------------------------------------------------------------------------------------------------------

# Energía Cinetica:
 
UcinEuler1 = (1.0/2.0)*Mearth_sun*((vEuler1[:,0]**2+vEuler1[:,1]**2)**0.5)**2
UcinEuler2 = (1.0/2.0)*Mearth_sun*((vEuler2[:,0]**2+vEuler2[:,1]**2)**0.5)**2
UcinEuler3 = (1.0/2.0)*Mearth_sun*((vEuler3[:,0]**2+vEuler3[:,1]**2)**0.5)**2

UcinLeapFrog1 = (1.0/2.0)*Mearth_sun*((vLeapFrog1[:,0]**2+vLeapFrog1[:,1]**2)**0.5)**2
UcinLeapFrog2 = (1.0/2.0)*Mearth_sun*((vLeapFrog2[:,0]**2+vLeapFrog2[:,1]**2)**0.5)**2
UcinLeapFrog3 = (1.0/2.0)*Mearth_sun*((vLeapFrog3[:,0]**2+vLeapFrog3[:,1]**2)**0.5)**2

UcinRK1 = (1.0/2.0)*Mearth_sun*((vRK1[:,0]**2+vRK1[:,1]**2)**0.5)**2
UcinRK2 = (1.0/2.0)*Mearth_sun*((vRK2[:,0]**2+vRK2[:,1]**2)**0.5)**2
UcinRK3 = (1.0/2.0)*Mearth_sun*((vRK3[:,0]**2+vRK3[:,1]**2)**0.5)**2

# Energía Potencial Gravitacional: U(r)= -G M m/r

UpotEuler1 = -G*Mearth_sun/((rEuler1[:,0]**2+rEuler1[:,1]**2)**0.5)
UpotEuler2 = -G*Mearth_sun/((rEuler2[:,0]**2+rEuler2[:,1]**2)**0.5)
UpotEuler3 = -G*Mearth_sun/((rEuler3[:,0]**2+rEuler3[:,1]**2)**0.5)

UpotLeapFrog1 = -G*Mearth_sun/((rLeapFrog1[:,0]**2+rLeapFrog1[:,1]**2)**0.5)
UpotLeapFrog2 = -G*Mearth_sun/((rLeapFrog2[:,0]**2+rLeapFrog2[:,1]**2)**0.5)
UpotLeapFrog3 = -G*Mearth_sun/((rLeapFrog3[:,0]**2+rLeapFrog3[:,1]**2)**0.5)

UpotRK1 = -G*Mearth_sun/((rRK1[:,0]**2+rRK1[:,1]**2)**0.5)
UpotRK2 = -G*Mearth_sun/((rRK2[:,0]**2+rRK2[:,1]**2)**0.5)
UpotRK3 = -G*Mearth_sun/((rRK3[:,0]**2+rRK3[:,1]**2)**0.5)

# Energia Total

UtotalEuler1 = UcinEuler1 + UpotEuler1
UtotalEuler2 = UcinEuler2 + UpotEuler2
UtotalEuler3 = UcinEuler3 + UpotEuler3

UtotalLeapFrog1 = UcinLeapFrog1 + UpotLeapFrog1
UtotalLeapFrog2 = UcinLeapFrog2 + UpotLeapFrog2
UtotalLeapFrog3 = UcinLeapFrog3 + UpotLeapFrog3

UtotalRK1 = UcinRK1 + UpotRK1
UtotalRK2 = UcinRK2 + UpotRK2
UtotalRK3 = UcinRK3 + UpotRK3


#------------------------------------------------------------------------------------------------------
#figuras de Energía
#------------------------------------------------------------------------------------------------------
#Euler
plt.figure(3,figsize = (30,30))
plt.subplot(3,3,1)
plt.plot(Euler1[:,0],UcinEuler1,c = 'blue')
plt.title('Euler, Energía Cinética dt = 0.01', fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]', fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.subplot(3,3,2)
plt.plot(Euler2[:,0],UcinEuler2,c = 'blue')
plt.title('Euler, Energía Cinética dt = 0.001',fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.subplot(3,3,3)
plt.plot(Euler3[:,0],UcinEuler3,c = 'blue')
plt.title('Euler, Energía Cinética dt = 0.0001',fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.subplot(3,3,4)
plt.plot(Euler1[:,0],UpotEuler1,c = 'blue')
plt.title('Euler, Energía Potencial dt = 0.01',fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.subplot(3,3,5)
plt.plot(Euler2[:,0],UpotEuler2,c = 'blue')
plt.title('Euler, Energía Potencial dt = 0.001',fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.subplot(3,3,6)
plt.plot(Euler3[:,0],UpotEuler3,c = 'blue')
plt.title('Euler, Energía Potencial dt = 0.0001',fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.subplot(3,3,7)
plt.plot(Euler1[:,0],UtotalEuler1,c = 'blue')
plt.title('Euler, Energía Total dt = 0.01',fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.subplot(3,3,8)
plt.plot(Euler2[:,0],UtotalEuler2,c = 'blue')
plt.title('Euler, Energía Total dt = 0.001',fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.subplot(3,3,9)
plt.plot(Euler3[:,0],UtotalEuler3,c = 'blue')
plt.title('Euler, Energía Total dt = 0.0001',fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.savefig('Energia_Euler.png')


#LeapFrog
plt.figure(4,figsize = (30,30))
plt.subplot(3,3,1)
plt.plot(LeapFrog1[:,0],UcinLeapFrog1,c = 'green')
plt.title('LeapFrog, Energía Cinética dt = 0.01', fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]', fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.subplot(3,3,2)
plt.plot(LeapFrog2[:,0],UcinLeapFrog2,c = 'green')
plt.title('LeapFrog, Energía Cinética dt = 0.001',fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.subplot(3,3,3)
plt.plot(LeapFrog3[:,0],UcinLeapFrog3,c = 'green')
plt.title('LeapFrog, Energía Cinética dt = 0.0001',fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.subplot(3,3,4)
plt.plot(LeapFrog1[:,0],UpotLeapFrog1,c = 'green')
plt.title('LeapFrog, Energía Potencial dt = 0.01',fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.subplot(3,3,5)
plt.plot(LeapFrog2[:,0],UpotLeapFrog2,c = 'green')
plt.title('LeapFrog, Energía Potencial dt = 0.001',fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.subplot(3,3,6)
plt.plot(LeapFrog3[:,0],UpotLeapFrog3,c = 'green')
plt.title('LeapFrog, Energía Potencial dt = 0.0001',fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.subplot(3,3,7)
plt.plot(LeapFrog1[:,0],UtotalLeapFrog1,c = 'green')
plt.title('LeapFrog, Energía Total dt = 0.01',fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.subplot(3,3,8)
plt.plot(LeapFrog2[:,0],UtotalLeapFrog2,c = 'green')
plt.title('LeapFrog, Energía Total dt = 0.001',fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.subplot(3,3,9)
plt.plot(LeapFrog3[:,0],UtotalLeapFrog3,c = 'green')
plt.title('LeapFrog, Energía Total dt = 0.0001',fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.savefig('Energia_LeapFrog.png')

#Runge-Kutta
plt.figure(5,figsize = (30,30))
plt.subplot(3,3,1)
plt.plot(RK1[:,0],UcinRK1,c = 'red')
plt.title('Runge-Kutta, Energía Cinética dt = 0.01', fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]', fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.subplot(3,3,2)
plt.plot(RK2[:,0],UcinRK2,c = 'red')
plt.title('Runge-Kutta, Energía Cinética dt = 0.001',fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.subplot(3,3,3)
plt.plot(RK3[:,0],UcinRK3,c = 'red')
plt.title('Runge-Kutta, Energía Cinética dt = 0.0001',fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.subplot(3,3,4)
plt.plot(RK1[:,0],UpotRK1,c = 'red')
plt.title('Runge-Kutta, Energía Potencial dt = 0.01',fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.subplot(3,3,5)
plt.plot(RK2[:,0],UpotRK2,c = 'red')
plt.title('Runge-Kutta, Energía Potencial dt = 0.001',fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.subplot(3,3,6)
plt.plot(RK3[:,0],UpotRK3,c = 'red')
plt.title('Runge-Kutta, Energía Potencial dt = 0.0001',fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.subplot(3,3,7)
plt.plot(RK1[:,0],UtotalRK1,c = 'red')
plt.title('Runge-Kutta, Energía Total dt = 0.01',fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.subplot(3,3,8)
plt.plot(RK2[:,0],UtotalRK2,c = 'red')
plt.title('Runge-Kutta, Energía Total dt = 0.001',fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.subplot(3,3,9)
plt.plot(RK3[:,0],UtotalRK3,c = 'red')
plt.title('Runge-Kutta, Energía Total dt = 0.0001',fontsize = 20)
plt.ylabel('Energía [$M_{solar}$$UA^{2}$/$yr^{2}$]',fontsize = 20)
plt.xlabel('t [yr]',fontsize = 20)
plt.grid()

plt.savefig('Energia_RK.png')






















