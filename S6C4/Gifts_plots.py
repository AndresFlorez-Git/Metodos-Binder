import numpy as np
import matplotlib
from matplotlib import cm
import matplotlib.pyplot as plt
import imageio
from mpl_toolkits.mplot3d import Axes3D

data = np.genfromtxt("Datos_inicio.dat",delimiter=",")
data = data[:,0:len(data[0,:])-1]


Datos_Evolucion_Periodico = np.genfromtxt("Datos_Evolucion_Periodico.dat",delimiter=",")
Datos_Evolucion_Periodico = Datos_Evolucion_Periodico[:,0:len(data[0,:])]


def plot_for_offset(i, data):
    # Data for plotting
    x = np.linspace(0,100,100)
    y = np.linspace(0,100,100)
    x,y = np.meshgrid(x,y)
    
    z_evolucion1 = Datos_Evolucion_Periodico[i*100+1*i:i*100+100+1*i,:]
    
    fig, ax = plt.subplots(figsize=(10,10))
    ax = fig.add_subplot(1,1,1,projection='3d')
    ax.plot_surface(x, y, z_evolucion1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    plt.title('Sistema Térmico, Frontera Periódica',fontsize = 22)
    plt.xlabel('X [cm]',fontsize=15)
    plt.ylabel('Y [cm]',fontsize=15)
    ax.set_zlabel('T [°C]',fontsize=15)

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_zlim(0, 100)

    # Used to return the plot as an image rray
    fig.canvas.draw()       # draw the canvas, cache the renderer
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image  = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    return image

kwargs_write = {'fps':20.0, 'quantizer':'nq'}
imageio.mimsave('./Evolucion_Sistema_Frontera_Periodica.gif', [plot_for_offset(i, Datos_Evolucion_Periodico) for i in range(0,60)], fps=20)