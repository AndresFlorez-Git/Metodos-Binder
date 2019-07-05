#include <iostream>
#include <math.h>

double Dx(double);
double Dv(double);
double RK(double, double, double, int);

int main(){
    /* Declaración de constantes */
    double m = 2;
    double k = 300;
    
    /* Tiempo inicial y final*/
    
    double temp_init = 0;
    double temp_final = 5;
    double h = 0.001;
    int puntos = ((temp_final - temp_init)/h);
    /* llamada a la función de Runge Kutta */
    
    RK(m, k, h, puntos);

    return 0;
    
}

double Dx(double v)
{
    return v;
}

double Dv(double x, double k, double m)
{
    return -k*x/m;
}

double RK (double m, double k, double h, int puntos)
{
    
    
    /* Espacio, temporal, movimiento  declarados */
    
    double t[puntos];
    double x[puntos];
    double v[puntos];
         
    /* Condiciones iniciales del problema:*/
    
    t[0] = 0;
    x[0] = 0.1;
    v[0] = 0;
    
    /* Declaración de variable auxiliares*/

    
    double k1;
    double k2;
    double k3;
    double k4;
    double prom1;
    
    double k11;
    double k22;
    double k33;
    double k44;
    double prom2;
    
    double x_1;
    double x_2;
    double x_3;
    
    double v_1;
    double v_2;
    double v_3;
    
    for(int i = 1 ; i< puntos;  i++)
    {
    k1 = Dx(v[i-1]);
    k11 = Dv(x[i-1],k, m);
    
    
   
    x_1 = x[i-1] + (h/2.0) * k1;
    v_1 = v[i-1] + (h/2.0) * k11;
    k2 = Dx(v_1);
    k22 = Dv(x_1 ,k, m);
    
    
   
    x_2 = x[i-1] + (h/2.0) * k2;
    v_2 = v[i-1] + (h/2.0) * k22;
    k3 = Dx(v_2);
    k33= Dv(x_2, k, m);
    
    
    
   
    x_3 = x[i-1] + h * k3;
    v_3 = v[i-1] + h * k33;
    k4 = Dx(v_3);
    k44= Dv(x_3, k, m);
    
    
    prom1 = (1.0/6.0)*(k1 + 2.0*k2 + 2.0*k3 + k4);
    prom2 = (1.0/6.0)*(k11 + 2.0*k22 + 2.0*k33 + k44);
    
    t[i] = t[i-1] + h;
    x[i] = x[i-1] + h * prom1;
    v[i]= v[i-1] + h * prom2;
        
    }
    for(int i = 0; i< puntos; i++)
    {
     std:: cout<<t[i]<<","<<v[i]<<","<<x[i]<< std:: endl ;
    }
   
}
