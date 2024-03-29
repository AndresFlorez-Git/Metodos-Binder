import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, ifft
# Tiene una serie de tiempo, donde los datos de tiempo estan almacenados en un arreglo t y los datos de amplitud en un arreglo amp.
#1) Usando los paquetes de scipy de la transformada de Fourier, haga un FILTRO de la senial que elimine las frecuencias mayores a 1000Hz en las senial original
data = np.genfromtxt('Canal_ionico.txt')
dt = data[1,0] - data[0,0]
fourier = np.fft.fft(data[:,1])
frec = np.fft.fftfreq(len(fourier),dt)
fc = 1000
def filtro(datos, fc):
    index = np.where(abs(datos)>fc)
    datos[index] = 0
    return datos

#2) Haga una grafica de la senial original y la senial filtarada y guardela SIN MOSTRARLA en filtro.pdf



n = 1280 # number of point in the whole interval
f = 200.0 #  frequency in Hz
dt = 1 / (f * 320 ) #320 samples per unit frequency
t = np.linspace( 0, (n-1)*dt, n)
amp = np.cos(2 * np.pi * f * t) - 0.4 * np.sin(2 * np.pi * (2*f) * t ) + np.random.random(n)

# SU FILTRO

# SU GRAFICA
plt.figure(1,figsize = (10,10))
plt.plot(t,amp)
fourier = np.fft.fft(amp)
frec = np.fft.fftfreq(len(fourier),dt)
fc = 1000
frecFiltro = filtro(frec,fc)
index = np.where(frecFiltro !=0)
new_data = np.fft.ifft(fourier[index])
plt.plot(t[index],new_data)
plt.savefig('filtro.pdf')

# Puede usar los siguientes paquetes:
#from scipy.fftpack import fft, fftfreq, ifft
