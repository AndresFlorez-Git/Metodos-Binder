import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, ifft


data = np.genfromtxt('Canal_ionico.txt')


#def verosimilitud(y_model,y_obs):
#    chi = sum((y_model-y_obs)**2)
#    L = np.exp(-chi**2 )
   

rCondicional = np.where(data[:,0]**2+data[:,1]**2< 0.1)
rmax = max(data[rCondicional,0]**2+data[rCondicional,1]**2)
def metropolis_Hasting(x,y, sigmax, sigmay):
    x_new = random.uniform(x,sigmax)
    y_new = random.uniform(y,sigmay)
    for i in range (1000):
        if x_new**2 + y_new**2 < rmax:
            x = x_new
            y = x_new
        
            
         
            
    
    
best_x = 1
best_y = 1
r_walk = [0,1]

plt.figure(0,figsize=(10,10))
plt.scatter(data[:,0],data[:,1])
fig, ax = plt.subplots()
plt.axis('equal')
circle1 = plt.Circle((best_x, best_y), np.max(r_walk), color='r',fill=False)
ax.add_artist(circle1)
plt.savefig("lalalalalalala.png")

