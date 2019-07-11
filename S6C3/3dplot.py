import numpy as np
import matplotlib
from matplotlib import cm
import matplotlib.pyplot as plt
import imageio
from mpl_toolkits.mplot3d import Axes3D

data = np.genfromtxt("datos.dat",delimiter=",")
x = data[0,0:len(data[0,:])-2]
y = data[1,0:len(data[0,:])-2]
z = data[2,0:len(data[0,:])-2]


x = np.reshape(x, (10, 10))
y = np.reshape(y, (10, 10))
z = np.reshape(z, (10, 10))

fig = plt.figure(0,figsize=(10,10))
ax = fig.add_subplot(1,1,1,projection='3d')
ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.title('Orbits X-Y-Z',fontsize = 22)
plt.xlabel('Lenght X [AU]',fontsize=15)
plt.ylabel('Lenght y [AU]',fontsize=15)
ax.set_zlabel('Lenght z [AU]',fontsize=15)


plt.savefig('Tambor.png')
