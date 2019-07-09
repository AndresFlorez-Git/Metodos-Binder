#include <iostream>
#include <math.h>

double recta(double, double, double);

int main()
{
    /* Constantes iniciales del problema*/
    double Longitud = 1;
    double dx = 0.005;
    double c = 300;
    double t_init = 0;
    double t_finit = 0.1;
    int puntos = Longitud/dx;
    double A0 = 0.01;
    
      
    
    /* Declaración de arreglos*/
    double x[puntos];
    double amplitud[puntos];
    
   
    
    
    /* Casos de estudio */
    int caso = 1;
    
    //Caso 1:tome condiciones de frontera fijas
    if(caso = 1)
    {
     x[0] = 0;
     amplitud[puntos/2] = A0;
     amplitud[0] = 0;
     amplitud[puntos-1] = 0;
     
    }
    
    //Caso 2:Repita lo anterior para un extremo fijo y un extremo libre
    if(caso = 2)
    {
     amplitud[puntos/2] = A0;
     amplitud[0] = 0;
     amplitud[puntos-1] = amplitud[puntos-2];
    }
  
    
    
    /* Condicion inicial*/
    
    for(int i = 0; i<= puntos;i++)
    {
        if (i>=1)
        {
             x[i] = x[i-1] + dx;
        }
       
        if (i<puntos/2)
        {
            amplitud[i] = recta(2*A0/Longitud, x[i],0);
        }
        
        if (i>puntos /2)
        {
            amplitud[i] = recta(-2*A0/Longitud, x[i],2*A0);
        }
        
        std::cout<<x[i]<<","<<amplitud[i]<< std::endl;
    }
    
    
    
    
 
    
    return 0;
}
/*
double Onda(double x,double t)
{
    
    
}
*/

double recta(double m, double x, double b)
{
   return m*x+b; 
}