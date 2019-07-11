import numpy as np
import matplotlib
from matplotlib import cm
import matplotlib.pyplot as plt
import imageio
from mpl_toolkits.mplot3d import Axes3D

data = np.genfromtxt("Datos_inicio.dat",delimiter=",")
data = data[:,0:len(data[0,:])-1]

data_Evolucion = np.genfromtxt("Datos_Evolucion.dat",delimiter=",")
data_Evolucion = data_Evolucion[:,0:len(data[0,:])]

print(data_Evolucion[:,len(data[0,:])-1])

x = np.linspace(0,100,100)
y = np.linspace(0,100,100)

x,y = np.meshgrid(x,y)
print(np.shape(x))
z = data
print(np.shape(z))

z_evolucion = data_Evolucion[1901:2002,:] 
print(np.shape(z_evolucion))

#x = np.reshape(x, (10, 10))
#y = np.reshape(y, (10, 10))
#z = np.reshape(z, (10, 10))

fig = plt.figure(0,figsize=(10,10))
ax = fig.add_subplot(1,1,1,projection='3d')
ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.title('Sistema Térmico',fontsize = 22)
plt.xlabel('X [cm]',fontsize=15)
plt.ylabel('Y [cm]',fontsize=15)
ax.set_zlabel('T [°C]',fontsize=15)


plt.savefig('Condicion_inicial.png')


fig = plt.figure(1,figsize=(10,10))
ax = fig.add_subplot(1,1,1,projection='3d')
ax.plot_surface(x, y, z_evolucion, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.title('Sistema Térmico',fontsize = 22)
plt.xlabel('X [cm]',fontsize=15)
plt.ylabel('Y [cm]',fontsize=15)
ax.set_zlabel('T [°C]',fontsize=15)


plt.savefig('Evolucion_sistema.png')
