import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import imageio

data = np.genfromtxt("datos.dat",delimiter=",")


plt.figure(0,figsize=(10,10))
plt.plot(data[:,len(data[0,:])-2],data[:,0], label='Sistema')
plt.title('Condicion inicial del Sistema')
plt.ylabel('Amplitud')
plt.xlabel('x en tiempo = 0')


plt.legend(loc = 0)
plt.grid()
plt.savefig('FlorezAndres.png')


def plot_for_offset(i, data):
    # Data for plotting
    t = data[:,len(data[0,:])-2]
    s = data[:,i]

    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(t, s)
    ax.grid()
    ax.set(xlabel='X en el tiempo ={}'.format(i), ylabel='Amplitud',
           title='Evolución del Sitema')

    ax.set_ylim(0, 3)

    # Used to return the plot as an image rray
    fig.canvas.draw()       # draw the canvas, cache the renderer
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image  = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    return image

kwargs_write = {'fps':3.0, 'quantizer':'nq'}
imageio.mimsave('./Evolucion_Sistema.gif', [plot_for_offset(i, data) for i in range(len(data[0,:])-3)], fps=3)



