import numpy as np
import matplotlib
from matplotlib import cm
import matplotlib.pyplot as plt
import imageio
from mpl_toolkits.mplot3d import Axes3D

data = np.genfromtxt("Datos_inicio.dat",delimiter=",")
data = data[:,0:len(data[0,:])-1]


data_Evolucion_periodica = np.genfromtxt("Datos_Evolucion_Periodico.dat",delimiter=",")
data_Evolucion_periodica = data_Evolucion_periodica[:,0:len(data[0,:])]


Datos_Evolucion_FronteraFija = np.genfromtxt("Datos_Evolucion_FronteraFija.dat",delimiter=",")
Datos_Evolucion_FronteraFija = Datos_Evolucion_FronteraFija[:,0:len(data[0,:])]

x = np.linspace(0,100,100)
y = np.linspace(0,100,100)
x,y = np.meshgrid(x,y)

z = data


z_evolucion_periodica1 = data_Evolucion_periodica[101:201,:] 
z_evolucion_periodica2 = data_Evolucion_periodica[50*100+1*50:50*100+100+1*50,:] 
z_evolucion_periodica3 = data_Evolucion_periodica[100*100+1*100:100*100+100+1*100,:] 

z_evolucion_FronteraFija1 = Datos_Evolucion_FronteraFija[101:201,:] 
z_evolucion_FronteraFija2 = Datos_Evolucion_FronteraFija[50*100+1*50:50*100+100+1*50,:] 
z_evolucion_FronteraFija3 = Datos_Evolucion_FronteraFija[100*100+1*100:100*100+100+1*100,:] 



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
plt.title('Frontera periodica',fontsize = 22)
plt.xlabel('X [cm]',fontsize=15)
plt.ylabel('Y [cm]',fontsize=15)
ax.set_zlabel('T [°C]',fontsize=15)

ax = fig.add_subplot(2,2,2,projection='3d')
ax.plot_surface(x, y, z_evolucion_periodica1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.title('Frontera periodica',fontsize = 22)
plt.xlabel('X [cm]',fontsize=15)
plt.ylabel('Y [cm]',fontsize=15)
ax.set_zlabel('T [°C]',fontsize=15)

ax = fig.add_subplot(2,2,3,projection='3d')
ax.plot_surface(x, y, z_evolucion_periodica2, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.title('Frontera periodica',fontsize = 22)
plt.xlabel('X [cm]',fontsize=15)
plt.ylabel('Y [cm]',fontsize=15)
ax.set_zlabel('T [°C]',fontsize=15)

ax = fig.add_subplot(2,2,4,projection='3d')
ax.plot_surface(x, y, z_evolucion_periodica3, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.title('Frontera periodica',fontsize = 22)
plt.xlabel('X [cm]',fontsize=15)
plt.ylabel('Y [cm]',fontsize=15)
ax.set_zlabel('T [°C]',fontsize=15)


plt.savefig('Evolucion_sistema_periodica.png')


fig = plt.figure(2,figsize=(10,10))

ax = fig.add_subplot(2,2,1,projection='3d')
ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.title('Frontera fija',fontsize = 22)
plt.xlabel('X [cm]',fontsize=15)
plt.ylabel('Y [cm]',fontsize=15)
ax.set_zlabel('T [°C]',fontsize=15)

ax = fig.add_subplot(2,2,2,projection='3d')
ax.plot_surface(x, y, z_evolucion_FronteraFija1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.title('Frontera fija',fontsize = 22)
plt.xlabel('X [cm]',fontsize=15)
plt.ylabel('Y [cm]',fontsize=15)
ax.set_zlabel('T [°C]',fontsize=15)

ax = fig.add_subplot(2,2,3,projection='3d')
ax.plot_surface(x, y, z_evolucion_FronteraFija2, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.title('Frontera fija',fontsize = 22)
plt.xlabel('X [cm]',fontsize=15)
plt.ylabel('Y [cm]',fontsize=15)
ax.set_zlabel('T [°C]',fontsize=15)

ax = fig.add_subplot(2,2,4,projection='3d')
ax.plot_surface(x, y, z_evolucion_FronteraFija3, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.title('Frontera fija',fontsize = 22)
plt.xlabel('X [cm]',fontsize=15)
plt.ylabel('Y [cm]',fontsize=15)
ax.set_zlabel('T [°C]',fontsize=15)


plt.savefig('Evolucion_sistema_FronteraFija.png')


