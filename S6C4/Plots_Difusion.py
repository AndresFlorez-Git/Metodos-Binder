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



x = np.linspace(0,100,100)
y = np.linspace(0,100,100)
x,y = np.meshgrid(x,y)

z = data


z_evolucion1 = data_Evolucion[101:201,:] 
z_evolucion2 = data_Evolucion[1000:1100,:] 
z_evolucion3 = data_Evolucion[3000:3100,:] 




fig = plt.figure(0,figsize=(10,10))
ax = fig.add_subplot(1,1,1,projection='3d')
ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.title('Sistema Térmico',fontsize = 22)
plt.xlabel('X [cm]',fontsize=15)
plt.ylabel('Y [cm]',fontsize=15)
ax.set_zlabel('T [°C]',fontsize=15)


plt.savefig('Condicion_inicial.png')


fig = plt.figure(1,figsize=(10,10))

ax = fig.add_subplot(2,2,1,projection='3d')
ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.title('Sistema Térmico',fontsize = 22)
plt.xlabel('X [cm]',fontsize=15)
plt.ylabel('Y [cm]',fontsize=15)
ax.set_zlabel('T [°C]',fontsize=15)

ax = fig.add_subplot(2,2,2,projection='3d')
ax.plot_surface(x, y, z_evolucion1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.title('Sistema Térmico',fontsize = 22)
plt.xlabel('X [cm]',fontsize=15)
plt.ylabel('Y [cm]',fontsize=15)
ax.set_zlabel('T [°C]',fontsize=15)

ax = fig.add_subplot(2,2,3,projection='3d')
ax.plot_surface(x, y, z_evolucion2, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.title('Sistema Térmico',fontsize = 22)
plt.xlabel('X [cm]',fontsize=15)
plt.ylabel('Y [cm]',fontsize=15)
ax.set_zlabel('T [°C]',fontsize=15)

ax = fig.add_subplot(2,2,4,projection='3d')
ax.plot_surface(x, y, z_evolucion3, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.title('Sistema Térmico',fontsize = 22)
plt.xlabel('X [cm]',fontsize=15)
plt.ylabel('Y [cm]',fontsize=15)
ax.set_zlabel('T [°C]',fontsize=15)


plt.savefig('Evolucion_sistema.png')
