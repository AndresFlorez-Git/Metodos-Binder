#Ejercicio 1 Terminar lo que hizo en clase + dos preguntas adicionales (en mayusculas en el texto)

import numpy as np
import matplotlib.pylab as plt


# 1) lea los datos de resorte.dat y almacenelos.
# 
resorte = np.genfromtxt("resorte.dat")

plt.figure(0,figsize=(10,10))
plt.plot(resorte[:,0],resorte[:,1])
plt.grid()
plt.title('Datos Observacionales')
plt.ylabel('Amplitud')
plt.xlabel('tiempo')
plt.savefig('Inicial.pdf')

# Los datos corresponden a las posiciones en x de un oscilador (masa resorte) en funcion del tiempo. La ecuacion de movimiento esta dada por  
# xt=a*np.exp(-gamma*t)*np.cos(omega*t)
# Donde a, gamma, y omega son parametros.

# 2) Implemente un algoritmo que le permita, por medio de estimacion bayesiana de parametros, encontrar los parametros correspondientes a los datos d. Para esto debe:

# 2a.) definir una funcion que reciba los parametros que se busca estimar y los datos de tiempo y retorne el modelo  
def funcion(t, a, gamma, omega):
    return a*np.exp(-gamma*t)*np.cos(omega*t)

# 2b.) Definir una funcion que retorne la funcion de verosimilitud
def verosimilitud(yobs, ymod): 
    chi = sum(((yobs - ymod)**2))
    return np.exp(-0.5*chi)

# 2c.) Caminata
def Metropolis_Hasting(pasos,sigmaA ,sigmaGAMMA ,sigmaOMEGA, A_guess, Gamma_guess, Omega_guess):
    A = []
    Gamma = []
    Omega = []
    verosim = []
    cto = 0
    t = resorte[:,0]
    for i in range(0,pasos):
        A_new = np.random.normal(A_guess,sigmaA,1)[0]
        Gamma_new = np.random.normal(Gamma_guess,sigmaGAMMA,1)[0]
        Omega_new = np.random.normal(Omega_guess,sigmaOMEGA,1)[0]
        
        #y_guess = funcion(t, A_guess, Gamma_guess, Omega_guess)
        #y_new = funcion(t, A_new, Gamma_new, Omega_new)
        
        L_guess = verosimilitud(resorte[:,1],funcion(t, A_guess, Gamma_guess, Omega_guess))
        L_new = verosimilitud(resorte[:,1],funcion(t, A_new, Gamma_new, Omega_new))
        
        alpha = L_new/L_guess
        beta = np.random.uniform(0,1)
        
        if alpha > 1:
            A.append(A_new)
            Gamma.append(Gamma_new)
            Omega.append(Omega_new)
            verosim.append(L_new)
            A_guess = A_new
            Gamma_guess = Gamma_new
            Omega_guess = Omega_new
            L_guess = L_new
            
        else:
            if alpha > beta:
                A.append(A_new)
                Gamma.append(Gamma_new)
                Omega.append(Omega_new)
                verosim.append(L_new)
                A_guess = A_new
                Gamma_guess = Gamma_new
                Omega_guess = Omega_new
                L_guess = L_new
                
                
            else:
                A.append(A_guess)
                Gamma.append(Gamma_guess)
                Omega.append(Omega_guess)
                verosim.append(L_guess)
                cto = cto +1
    A = np.array(A)
    Gamma = np.array(Gamma)
    Omega = np.array(Omega)
    verosim = np.array(verosim)
    vero_max = max(verosim)
    for i in range(len(verosim)):
        if verosim[i] == vero_max:
            indexMax = i
        
        
    return A[indexMax], Gamma[indexMax], Omega[indexMax], verosim[indexMax]

#condiciones iniciales
aini=7.5
gammaini=0.6
omegaini=18.2

#numero de pasos
iteraciones=10000


resultados = Metropolis_Hasting(iteraciones,0.1 ,0.1 ,0.1, aini, gammaini, omegaini)


# 2d.) Seleccione los mejores parametros E IMPRIMA UN MENSAJE QUE DIGA: "LOS MEJORES PARAMETROS SON a=... gamma=... Y omgega=..."
print("LOS MEJORES PARAMETROS SON a=",resultados[0], "gamma=",resultados[1], "Y omgega=",resultados[2])
# 2f.) Grafique sus datos originales y su modelo con los mejores parametros. Guarde su grafica sin mostrarla en Resorte.pdf
t = resorte[:,0]
y = funcion(t, resultados[0], resultados[1], resultados[2])

plt.figure(0,figsize=(10,10))
plt.plot(resorte[:,0],resorte[:,1],label = 'datos observacionales', c = 'blue')
plt.plot(t,y,label='modelo',c='red')
plt.title('Datos Observacionales y datos modelo')
plt.ylabel('Amplitud')
plt.xlabel('tiempo')
plt.legend(loc=0)
plt.grid()
plt.savefig('Comparacion.pdf')
# 3) SABIENDO QUE omega=np.sqrt(k/m), IMPRIMA UN MENSAJE DONDE EXPLIQUE SI PUEDE O NO DETERMINAR k Y m DE MANERA INDIVIDUAL USANDO EL METODO ANTERIOR. JUSTIFIQUE BIEN SU RESPUESTA (PUEDE ADEMAS HACER PRUEBAS CON EL CODIGO PARA RESPONDER ESTA PREGUNTA).

print('No se puede dado que el valor de omega depende de de la relación de k/m, por lo que existen infinitas soluciones de k y m tal que cumpla omega=np.sqrt(k/m) dado el omega encontrado. Normalmente la masa es un valor conocido')

