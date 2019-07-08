#include <iostream>
#include <math.h>

double u(double, double, double);

int main(){
/* Condiciones iniciales */
    
    double vel  = 1;
    double ampl_max = 2;
    double ampl_min = 1;
    double x1_init = 0.75;
    double x2_init = 1.25;
    double x_min = 0;
    double x_max = 2;
    double t_init = 0;
    int N = 80;
    
    double dx = (x_max - x_min)/N;
    double dt = dx*0.25/vel;
/* Se declara los espacios temporales y espaciales*/
    double tiempo[N]; 
    double x[N];
    double ampl_x [N];
/* Valores iniciales de los arreglos */
    
    tiempo [0] = t_init;
    x[0] = 0;
    
     
/* Se rellenan esos espacios los espacios*/
    for(int i = 1; i<N; i++ )
    {
        tiempo[i] = tiempo[i-1] + dt;
        x[i] = x[i-1] + dx;
        ampl_x[i] = u(x[i],x1_init,x2_init);
        
        std:: cout<<x[i]<<","<<ampl_x[i]<< std::endl;
    }
/* Evolucion del sistema*/
    
    
    //for(int t = 1; t < N)
   
    return 0;
    
}

double u(double x,double x_min, double x_max){
    if (x< x_min || x > x_max)
    {
        return 1;
    }
    else 
    {
        return 2 ;  
    }
}

