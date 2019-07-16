# Punto 2:  Transformada de Fourier: Imágenes híbridas.

import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq, ifft, fft2
from matplotlib.colors import LogNorm


# Se almacena la información de las imagenes:

FotoFeliz = plt.imread("cara_03_grisesMF.png")
FotoSeria = plt.imread("cara_02_grisesMF.png")

# Ser realiza la transformada de fourier para las fotos:

fourieFotoFeliz = np.fft.fft2(FotoFeliz)

fourieFotoSeria = np.fft.fft2(FotoSeria)

# Se realiza el filtro para las imagenes:

def filtroPasaBajas(fourieFoto,amplCorte):
    index = np.where(fourieFoto > amplCorte)
    fourieFoto[index] = 0
    return fourieFoto

def filtroPasaAltas(fourieFoto,amplCorte):
    index = np.where(fourieFoto < amplCorte)
    fourieFoto[index] = 0
    return fourieFoto

# Se Filtran las imagenes:




plt.figure(0,figsize=(15,30))
plt.subplot(6,2,1)
plt.imshow(abs(FotoFeliz),cmap = 'gray')
plt.title('Foto Feliz')
#plt.colorbar()
plt.subplot(6,2,2)
plt.imshow(abs(FotoSeria),cmap = 'gray')
plt.title('Foto Seria')
#plt.colorbar()
plt.subplot(6,2,3)
plt.imshow(abs(fourieFotoFeliz),cmap = 'plasma',norm = LogNorm())
plt.title('Espectro de fourie Foto Feliz')
plt.colorbar()
plt.subplot(6,2,4)
plt.imshow(abs(fourieFotoSeria),cmap = 'plasma',norm = LogNorm())
plt.title('Espectro de fourie Foto Seria')
plt.colorbar()
#-------------------------------------------------------------------
# Se visualiza el rango de frecuencias del dominio de fourier:
FiltrofourieFotoFeliz = np.fft.fftshift(fourieFotoFeliz)


FiltrofourieFotoSeria = np.fft.fftshift(fourieFotoSeria)

#---------------------------------------------------------------------
plt.subplot(6,2,5)
plt.imshow(abs(FiltrofourieFotoFeliz),cmap = 'plasma',norm = LogNorm())
plt.title('Espectro de fourie Foto Feliz Frecuencias')
plt.colorbar()
plt.subplot(6,2,6)
plt.imshow(abs(FiltrofourieFotoSeria),cmap = 'plasma',norm = LogNorm())
plt.title('Espectro de fourie Foto Seria Frecuencias')
plt.colorbar()
#-------------------------------------------------------------------
# Se aplica el filtro:

FiltrofourieFotoFeliz = filtroPasaAltas(FiltrofourieFotoFeliz,50)


FiltrofourieFotoSeria = filtroPasaBajas(FiltrofourieFotoSeria,50)
#---------------------------------------------------------------------
plt.subplot(6,2,7)
plt.imshow(abs(FiltrofourieFotoFeliz),cmap = 'plasma',norm = LogNorm())
plt.title('Frecuencias de fourie Foto Feliz Frecuencias Filtradas')
plt.colorbar()
plt.subplot(6,2,8)
plt.imshow(abs(FiltrofourieFotoSeria),cmap = 'plasma',norm = LogNorm())
plt.title('Frecuencias de fourie Foto Seria Frecuencias Filtradas')
plt.colorbar()
#-------------------------------------------------------------------
# Se visualiza la el espectro de furier con frecuencias filtradas:

fourieFotoFelizFiltrada = np.fft.ifftshift(FiltrofourieFotoFeliz)


fourieFotoSeriaFiltrada = np.fft.ifftshift(FiltrofourieFotoSeria)
#---------------------------------------------------------------------
plt.subplot(6,2,9)
plt.imshow(abs(fourieFotoFelizFiltrada),cmap = 'plasma',norm = LogNorm())
plt.title('Espectro de fourie Foto Feliz Filtradas')
plt.colorbar()
plt.subplot(6,2,10)
plt.imshow(abs(fourieFotoSeriaFiltrada),cmap = 'plasma',norm = LogNorm())
plt.title('Espectro de fourie Foto Seria Filtradas')
plt.colorbar()

#-------------------------------------------------------------------
# Se visualiza la el espectro de furier con frecuencias filtradas:

fourierCombinada = fourieFotoFelizFiltrada + fourieFotoSeriaFiltrada


FotoReultado = np.fft.ifft2(fourierCombinada)
#---------------------------------------------------------------------
plt.subplot(6,2,(11,12))
plt.imshow(abs(FotoReultado),cmap = 'gray')
plt.title('Foto Híbrida')

plt.savefig('FFT2D.png')