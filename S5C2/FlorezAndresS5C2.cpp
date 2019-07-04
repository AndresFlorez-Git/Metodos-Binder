#include <iostream>
#include <math.h>

double funcion(double);
double euler();

int main(){
    
    euler();
    
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
