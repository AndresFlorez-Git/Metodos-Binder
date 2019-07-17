# Ejercicio 1

import numpy as np
import matplotlib.pylab as plt


# Use esta funcion que recibe un valor x y retorna un valor f(x) donde f es la forma funcional que debe seguir su distribucion. 
def mifun(x):
    x_0 = 3.0
    a = 0.01
    return (np.exp(-(x**2))/((x-x_0)**2 + a**2))*10000
    
x = np.linspace(-4,4,1000)
y = mifun(x)

plt.figure(0,figsize = (10,10 ))
plt.plot(x,y,label = 'función')
plt.title('Función')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend(loc = 0)
plt.savefig('Funcion_inicial.pdf')

# Dentro de una funcion que reciba como parametros el numero de pasos y el sigma de la distribucion gausiana que va a usar para calcular el paso de su caminata, implemente el algortimo de Metropolis-Hastings. Finalmente, haga un histograma de los datos obtenidos y grafique en la misma grafica, la funcion de distribucion de probabilidad fx (Ojo, aca debe normalizar). Guarde la grafica sin mostrarla en un pdf. Use plt.savefig("histograma_"+str(sigma)+"_"+str(pasos)+".pdf"), donde sigma y pasos son los parametros que recibe la funcion. 

def Metropolis_Hasting(pasos,sigma):
    puntos = []
    cto = 0
    x_guess = np.random.uniform(-4,4,1)[0]
    
    for i in range(0,pasos):
        x_new = np.random.normal(x_guess,sigma,1)[0]
        #print(x_guess,' ',mifun(x_guess),x_new,' ',mifun(x_new))
        alpha = mifun(x_new)/mifun(x_guess)
        beta = np.random.uniform(0,1)
        
        if alpha > 1:
            puntos.append(x_new)
            x_guess = x_new
        else:
            if alpha > beta:
                puntos.append(x_new)
                x_guess = x_new
                
            else:
                puntos.append(x_guess)
                cto = cto +1
        
        
    puntos = np.array(puntos)
    return puntos, (cto/len(puntos))*100


# Cuando haya verificado que su codigo funciona, use los siguientes parametros:
sigma = 5
pasos =100000
plt.figure(1,figsize = (10,10 ))
plt.hist(Metropolis_Hasting(pasos,sigma)[0],bins = 50,density = True)
plt.title("histograma, Porcentaje de rechazo: {}".format(Metropolis_Hasting(pasos,sigma)[1]))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.savefig("histograma_"+str(sigma)+"_"+str(pasos)+".pdf")
# sigma = 0.2, pasos =100000 

sigma = 0.2
pasos =100000 
plt.figure(2,figsize = (10,10 ))
plt.hist(Metropolis_Hasting(pasos,sigma)[0],bins = 100,density = True)
plt.title("histograma, Porcentaje de rechazo: {}".format(Metropolis_Hasting(pasos,sigma)[1]))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.savefig("histograma_"+str(sigma)+"_"+str(pasos)+".pdf")
# sigma = 0.01, pasos =100000 

sigma = 0.01
pasos =100000 
plt.figure(3,figsize = (10,10 ))
plt.hist(Metropolis_Hasting(pasos,sigma)[0],bins = 100,density = True)
plt.title("histograma, Porcentaje de rechazo: {}".format(Metropolis_Hasting(pasos,sigma)[1]))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.savefig("histograma_"+str(sigma)+"_"+str(pasos)+".pdf")
# sigma = 0.1, pasos =1000 

sigma = 0.1
pasos =1000 
plt.figure(4,figsize = (10,10 ))
plt.hist(Metropolis_Hasting(pasos,sigma)[0],bins = 100,density = True)
plt.title("histograma, Porcentaje de rechazo: {}".format(Metropolis_Hasting(pasos,sigma)[1]))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.savefig("histograma_"+str(sigma)+"_"+str(pasos)+".pdf")
# sigma = 0.1, pasos =100000 

sigma = 0.1
pasos =100000 
plt.figure(5,figsize = (10,10 ))
plt.hist(Metropolis_Hasting(pasos,sigma)[0],bins = 100,density = True)
plt.title("histograma, Porcentaje de rechazo: {}".format(Metropolis_Hasting(pasos,sigma)[1]))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.savefig("histograma_"+str(sigma)+"_"+str(pasos)+".pdf")
# este puede ser muy demorado dependiendo del computador: sigma = 0.1, pasos =500000 

# Al ejecutar el codigo, este debe generar 6 (o 5) graficas .pdf una para cada vez que se llama a la funcion.
