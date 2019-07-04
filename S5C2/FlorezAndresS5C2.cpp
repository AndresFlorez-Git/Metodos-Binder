#include <iostream>
#include <math.h>

double funcion(double);
double euler();
double RK();

int main(){
    
    euler();
    std::cout<<"-,-"<<std::endl;
    RK();
    
    return 0;
}


double funcion(double x)
{
 return -x;   
}

double euler()
{
    double h;
    double init;
    double finit;
    int puntos;
    
    
    h=0.01;
    init = 0.0;
    finit = 2.0;
    puntos = ((finit - init)/h);
    
    double x[puntos];
    double y[puntos];
    
    x[0] = init;
    y[0] = 1;
    
    for(int i = 1; i <puntos;i++)
    {
        x[i] = x[i-1] + h;
        y[i] = y[i-1] + h * funcion(y[i-1]);
        
    }
    
    for(int i = 0; i< puntos; i++)
    {
     std:: cout<<x[i]<<","<<y[i]<< std:: endl ;
    }
}

double RK ()
{
    double h;
    double init;
    double finit;
    int puntos;
    
    
    h=0.01;
    init = 0.0;
    finit = 2.0;
    puntos = ((finit - init)/h);
    
    double x[puntos];
    double y[puntos];
    
    x[0] = init;
    y[0] = 1;
    
    double k1;
    double k2;
    double k3;
    double k4;
    double prom;
    for (int i = 1; i< puntos; i++)
    {
    k1 = h * funcion(y[i-1]);
    k2 = h * funcion( y[i-1] + 0.5 * k1);
    k3 = h * funcion( y[i-1] + 0.5 * k2);
    k4 = h * funcion( y[i-1] + k3);
    
    
    prom = (1.0/6.0)*(k1 + 2.0*k2 + 2.0*k3 + k4);
    
    x[i] = x[i-1] + h;
    y[i] = y[i-1] + prom;
    }
    
    for(int i = 0; i< puntos; i++)
    {
     std:: cout<<x[i]<<","<<y[i]<< std:: endl ;
    }
    
}