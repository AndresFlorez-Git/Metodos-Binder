import numpy as np
import matplotlib.pyplot as plt

#Ejercicio 0
#Lean el capitulo 5 del Landau (ver el programa del curso).

#Ejercicio 1
# Usando los generadores de numeros aleatorios de numpy (https://docs.scipy.org/doc/numpy-1.15.1/reference/routines.random.html):
# a) Genere 1000 numeros aleatorios que sigan una distribucion uniforme y esten entre -10 y 10. Haga un histograma y guardelo sin mostrarlo en un archivo llamado uniforme.pdf
uniforme = np.random.uniform(-10,10,1000)
plt.figure(0,figsize = (10,10))
plt.hist(uniforme, bins = 100)
plt.title('Histograma de la distribución uniforme')
plt.xlabel('x')
plt.ylabel('frecuencia de repetición')
plt.savefig('uniforme.pdf')


# a) Genere 1000 numeros aleatorios que sigan una distribucion gausiana centrada en 17 y de sigma 5. Haga un histograma y guardelo sin mostrarlo en un archivo llamado gausiana.pdf
normal = np.random.normal(17,5,1000)
plt.figure(1,figsize = (10,10))
plt.hist(normal, bins = 100)
plt.title('Histograma de la distribución Gausiana')
plt.xlabel('x')
plt.ylabel('frecuencia de repetición')
plt.savefig('gausiana.pdf')

# Ejercicio 2
# Escriba un programa en Python que: 
# Genere puntos aleatorios distribuidos uniformemente dentro de un cuadrado de lado 30.5. Grafique sus puntos y guarde la grafica sin mostrarla en un archivo llamado cuadrado.pdf. 
unifomreX = np.random.uniform(0,30.5,1000)
unifomreY = np.random.uniform(0,30.5,1000)
x = [0,30.5]
y = [0,0]
superior = [30.5,30.5]
plt.figure(2,figsize = (10,10))
plt.scatter(unifomreX,unifomreY)
plt.plot(x,superior,c='black')
plt.plot(x,y,c='black')
plt.plot(superior,x,c='black')
plt.plot(y,x,c='black')
plt.title('Puntos dentro de cuadrado por distribución uniforme')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('cuadrado.png')

# Genere puntos aleatorios distribuidos uniformemente dentro de circulo de radio 23. Grafique sus puntos y guarde la grafica sin mostrarla en un archivo llamado circulo.pdf. 
x = np.linspace(-23*0.5,23*0.5,1000)


unifomreX = np.random.uniform(-23*0.5,23*0.5,10000)
unifomreY = np.random.uniform(-23*0.5,23*0.5,10000)
i = np.where(unifomreX**2+unifomreY**2<=23)

plt.figure(3,figsize = (10,10))
plt.scatter(unifomreX[i],unifomreY[i])
plt.title('Puntos dentro de circulo por distribución uniforme')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('circulo.png')
# Ejercicio 3 
# Lean sobre caminatas aleatorias.


# Ejercicio 4
# Tome los puntos distribuidos aleatoriamente dentro del cuadrado y haga que cada punto siga una caminata aleatoria de 100 pasos. 
# La magnitud de los pasos de esta caminata debe seguir una distribucion gaussiana centrada en el punto y de sigma igual a 0.25
# Implemente condiciones de frontera periodicas: si un punto se "sale" de cuadrado por un lado, "entra" por el otro  

unifomreX = np.random.uniform(0,30.5,1000)
unifomreY = np.random.uniform(0,30.5,1000)
x = [0,30.5]
y = [0,0]
superior = [30.5,30.5]

plt.figure(2,figsize = (10,10))
plt.subplot(2,1,1)
plt.scatter(unifomreX,unifomreY, s=1)
plt.plot(x,superior,c='black')
plt.plot(x,y,c='black')
plt.plot(superior,x,c='black')
plt.plot(y,x,c='black')
plt.title('Puntos dentro de cuadrado por distribución uniforme')
plt.xlabel('x')
plt.ylabel('y')
# ---------------------------------------------------------------
#caminata aleatoria de los puntos
for i in range(0,100):    
    for j in range(0,1000):
        pasox = np.random.normal(0,0.25,1)
        pasoy = np.random.normal(0,0.25,1)
        if abs(unifomreX[j] + pasox) <= 30.5:
            unifomreX[j] = unifomreX[j] + pasox     
        else:
            if unifomreX[j]*pasox>0:
                unifomreX[j] = unifomreX[j] + pasox - 30.5
            else:
                unifomreX[j] = abs(unifomreX[j] + pasox)
        if abs(unifomreY[j] + pasoy) <= 30.5:
            unifomreY[j] = unifomreY[j] + pasoy          
        else:
            if unifomreY[j]*pasoy>0:
                unifomreY[j] = unifomreY[j] + pasoy - 30.5
            else:
                unifomreY[j] = abs(unifomreY[j] + pasoy)
        if unifomreX[j]<0:
            unifomreX[j] = abs(unifomreX[j])
        if unifomreY[j]<0:
            unifomreY[j] = abs(unifomreY[j])
           
        #print(unifomreX[j],pasox,'',unifomreY[j],pasoy)
#----------------------------------------------------------------
plt.subplot(2,1,2)
plt.scatter(unifomreX,unifomreY, s=1)
plt.plot(x,superior,c='black')
plt.plot(x,y,c='black')
plt.plot(superior,x,c='black')
plt.plot(y,x,c='black')
plt.title('Puntos despues de la camitata aleatoria')
plt.xlabel('x')
plt.ylabel('y')


plt.savefig('DistCaminata.png')


# Grafique la distribucion final de puntos y guarde dicha grafica sin mostrarla en un archivo llamado DistCaminata.pdf
# Grafique la caminata de UNO de sus puntos y guarde dicha grafica sin mostrarla en un archivo llamado puntoCaminata.pdf

# Repita el proceso para sigma = 0.00025 y sigma= 2.5. Grafique la caminata de UNO de sus puntos para los distintos sigmas y guardela sin mostrarla en sigmaCaminata.pdf

# Repita el proceso para condiciones abiertas: si un punto se "sale" del cuadrado deja de ser considerado en la simulacion.

# Si le queda tiempo puede:

##################################################################################################################################################################
############################################################ Ejercicio  ##########################################################################
##################################################################################################################################################################

#difusion: una gota de crema en un Cafe.
#
#Condiciones iniciales:
#Cafe: 10000 particulas distribuidas uniformemente dentro de un circulo de radio igual a raiz de 230
#Crema: 100 particulas distribuidas uniformemente dentro de un circulo de radio igual a raiz de 2
#
#Nota: si su codigo se esta demorando mucho en correr, puede usar 1000 particulas de cafe en vez de 10000.
#
# 1) Haga una grafica de las condiciones iniciales donde los dos tipos de particulas tengan distintos colores. Guarde dicha grafica sin mostrarla en CafeLecheIni.pdf
#
#2) Todas las particulas deben hacer una caminata aleatoria de 1000 pasos. Los pasos en las coordenadas x y deben seguir una distribucion gausiana de sigma 2.5. Si va a usar coordenadas polares elija un sigma apropiado.
#
#3) Condiciones de frontera: implemente unas condiciones tales que si la particulas "sale" del circulo, usted vuelva a dar el paso. Si no puede implementar solo las condiciones antes descritas, debe al menos escribir comentarios explicando que hace cada linea de codigo de las condiciones propuestas (comentado abajo)
#
# 4) Haga una grafica de las posiciones finales de las particulas despues de la caminata donde los dos tipos de particulas tengan distintos colores. Guarde dicha grafica sin mostrarla en CafeLecheFin.pdf
#

import numpy as np
import matplotlib.pylab as plt


#Una posible implementacion de condiciones de frontera. Trate de hacer la suya propia sin usar esta. 
#Si usa esta (obtiene menos puntos) debe comentar cada una de las lineas explicando en palabras que hace el codigo. Debe tambien naturalmente usar los nombres de variables que uso en el resto de su codigo propio.
#indexcafe=np.where((xcafenuevo*xcafenuevo+ycafenuevo*ycafenuevo)>230)
#indexcrema=np.where((xcremanuevo*xcremanuevo+ycremanuevo*ycremanuevo)>230)
#while(len(indexcafe[0])>1):
#	xcafenuevo[indexcafe]=xcafe[indexcafe] + np.random.normal(0,sigma)
#	ycafenuevo[indexcafe]=ycafe[indexcafe] + np.random.normal(0,sigma)
#	indexcafe=np.where((xcafenuevo*xcafenuevo+ycafenuevo*ycafenuevo)>=230)
#while(len(indexcrema[0])>1):
#	xcremanuevo[indexcrema]=xcrema[indexcrema] + np.random.normal(0,sigma)
#	ycremanuevo[indexcrema]=ycrema[indexcrema] + np.random.normal(0,sigma)
#	indexcrema=np.where((xcremanuevo*xcremanuevo+ycremanuevo*ycremanuevo)>=230) 



	
