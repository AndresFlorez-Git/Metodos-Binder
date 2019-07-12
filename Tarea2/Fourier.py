# Punto 2:  Transformada de Fourier: Imágenes híbridas.

import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq
from matplotlib.colors import LogNorm


# Se almacena la información de las imagenes:

FotoFeliz = plt.imread("cara_03_grisesMF.png")
FotoSeria = plt.imread("cara_02_grisesMF.png")

# Ser realiza la transformada de fourier para las fotos:

fourieFotoFeliz = np.fft.fft2(FotoFeliz)

fourieFotoSeria = np.fft.fft2(FotoSeria)

# Se realiza el filtro para las imagenes:

plt.figure(0,figsize=(20,20))
plt.subplot(2,2,1)
plt.imshow(abs(FotoFeliz),cmap = 'gray',vmin = 100,vmax = 3000)
plt.title('Espectro de fourie Foto')
#plt.colorbar()
plt.subplot(2,2,2)
plt.imshow(abs(FotoSeria),cmap = 'gray',vmin = 100,vmax = 3000)
plt.title('Espectro de fourie Foto')
#plt.colorbar()
plt.subplot(2,2,3)
plt.imshow(abs(fourieFotoFeliz),cmap = 'plasma',vmin = 100,vmax = 3000)
plt.title('Espectro de fourie Foto')
#plt.colorbar()
plt.subplot(2,2,1)
plt.imshow(abs(fourieFotoSeria),cmap = 'plasma',vmin = 100,vmax = 3000)
plt.title('Espectro de fourie Foto')
#plt.colorbar()

plt.savefig('FFT2D.png')