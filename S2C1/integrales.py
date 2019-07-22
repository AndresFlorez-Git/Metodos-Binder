
#########################################################################################
################### preparacion S2C1 integracion numerica ###############################
#########################################################################################

#Este ejercicio preparatorio busca que usted implemente correctamente tres metodos de integracion numerica. Haga este ejercicio despues de haber leido y entendido los algoritmos correspondientes a los distintos metodos. Si quiere complementar este ejercicio, puede repetir el proceso para el metodo de Monte Carlo y el metodo del valor medio.

# Ejercicio: Integrales

import numpy as np
import matplotlib.pylab as plt

# Funcion a integrar
def funcion(x1):
	return np.cos(x1)

a = 0
b = 3*(np.pi/2)
M = 1000
#El intervalo de integracion es de 0 a 3pi/2. Divida el intervalo de integracion en M secciones para calcular sus integrales.

# 1a). Usando el metodo de suma de rectangulos, calcule la integral de la funcion. Compare su valor obtenido numericamente con el valor analitico e imprima ambos valores.
def rectangulos(a,b,M):
    Espacio = np.linspace(a,b,M)
    h = (b-a)/(M-1)
    return sum(h*funcion(Espacio))
# 1b). Usando el metodo de trapezoide, calcule la integral de la funcion. Compare su valor obtenido numericamente con el valor analitico e imprima ambos valores.
def trapezoide(a,b,M):
    Espacio = np.linspace(a,b,M)
    h = (b-a)/(M-1)
    Espacio = h*funcion(Espacio)
    Espacio[0] = Espacio[0]/2
    Espacio[len(Espacio)-1] = Espacio[len(Espacio)-1]/2
    return sum(Espacio)

# 1c). Usando el metodo de Simpson, calcule la integral de la funcion. Compare su valor obtenido numericamente con el valor analitico e imprima ambos valores.
def Simpson(a,b,N):
    if N%2 ==0:
        N = N+1
    Espacio = np.linspace(a,b,N)
    h = (b-a)/(N-1)
    Espacio[1:len(Espacio)-1:2]=funcion(Espacio[1:len(Espacio)-1:2])*4*h/3
    Espacio[2:len(Espacio)-1:2]=funcion(Espacio[2:len(Espacio)-1:2])*2*h/3
    Espacio[0]=funcion(Espacio[0])*h/3
    Espacio[N-1]=funcion(Espacio[N-1])*h/3
    return sum(Espacio)

print('rectangulos = ',rectangulos(a,b,M))
print('Trapezoides = ',trapezoide(a,b,M))
print('Trapezoides = ',Simpson(a,b,M))
