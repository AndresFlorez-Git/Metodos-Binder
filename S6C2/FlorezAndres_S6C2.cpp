#include <iostream>
#include <math.h>

double Pi = 3.141592653589793238;
double recta(double, double, double);
double funCaso3(double ,double,  double, double);

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
    double dt = (dx/c)*0.25;
    int puntosTemporales = (t_finit-t_init)/dt;
      
    
    /* Declaración de arreglos*/
    double x[puntos];
    double amplitud[puntos];
    
    double pasado[puntos];
    double presente[puntos];
    double futuro[puntos];
    
   
    
    
    /* Casos de estudio */
    int caso = 3;
    
    //Caso 1:tome condiciones de frontera fijas
    if(caso == 1)
    {
     x[0] = 0;
     amplitud[puntos/2] = A0;
     amplitud[0] = 0;
     amplitud[puntos-1] = 0;
     presente[0] = 0;
     futuro[0] = 0;
    }
    
    //Caso 2:Repita lo anterior para un extremo fijo y un extremo libre
    if(caso == 2)
    {
     amplitud[puntos/2] = A0;
     amplitud[0] = 0;
     amplitud[puntos-1] = amplitud[puntos-2];
    }
  
    
    
    /* Condicion inicial -------------------------------------*/
    if (caso == 1 || caso == 2)
    {
    
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
        
            pasado[i] = amplitud[i];
            std::cout<<x[i]<<",";//<<amplitud[i]<< std::endl;
        }
        std:: cout<<std::endl;
    }
    
    if (caso == 3)
    {
        x[0] = 0;
        for(int i = 0; i<= puntos;i++)
        {
            if (i>=1)
            {
                 x[i] = x[i-1] + dx;
            }
            
            amplitud[i] = 0;
            pasado[i] = amplitud[i];
            std::cout<<x[i]<<",";//<<amplitud[i]<< std::endl;
        }
        std:: cout<<std::endl;
    }
    
        
    /* Evolución del sistema ----------------------------------- */
    
    
    // Paso inmediato al inicio
    for(int i = 1; i<= puntos; i++)
    {
       presente[i] = ((c*c*dt*dt)/(dx*dx*2)) * (pasado[i+1] + pasado[i-1] - 2*pasado[i]) + pasado[i];
       if(caso == 2)
       {
           presente[puntos] = presente[puntos-1];
       }
       if(caso == 3)
       {
            presente[puntos] =   funCaso3(A0, 1, c, Longitud);
       }
       }
        
    
    // Construimos el futuro
    int cto = 0;
    for (int t = 0; t<= puntosTemporales; t++)
    {
        
         if(cto == 0 || cto % 5 == 0)
        {
             for (int i = 0; i<=puntos;i++)
             {
              std:: cout<<presente[i]<<","; 
             }
         std:: cout<<std::endl; 
        }
        
        
        for (int i = 1; i<=puntos;i++ )
        {
            futuro[i] = ((c*c*dt*dt)/(dx*dx)) * (presente[i+1] + presente[i-1] - 2*presente[i])- pasado[i] + 2*presente[i];
            if (caso ==2)
            {
            futuro[puntos] = futuro[puntos-1];
            }
            if (caso ==3)
            {
            futuro[puntos] =  funCaso3(A0, t*dt , c, Longitud);
            }
        }
        
        for(int i = 0; i<=puntos; i++)
        {
            pasado[i] = presente[i];
            presente[i]= futuro[i];
        }
        
       cto = cto+1;
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

double funCaso3(double A0, double t, double c, double L)
{
 return A0 * cos(3.0 * c * t *Pi/L); 
}