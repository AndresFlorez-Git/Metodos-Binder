#include<iostream>
#include<math.h>
#include<fstream>
using namespace std;

double G1 = 6.674e-11; //Constante de gravitacion universal [N m**2/ kg**2]
double UA = 149597870700; // unidad astronomica en metros
double M = 1.989e30; // masa del sol
double yr = 31536000; // segundos al año
double G = G1*(1/(UA*UA*UA))*(M)*(yr*yr); // Constante de gravitacion universal [UA^3 /(Masa_Solar yr^2)]

//double Euler();

double Runge_Kutta(double, double, double, double, double, double, double, int, int);

int main(){
 
    /*Constantes iniciales del problema*/
    double X0 = 0.1163;
    double Y0 = 0.9772;
    
    double vX0 = -6.35;
    double vY0 = 0.606;
    
    int orbitas = 20;
    
    int cto = 1;
    /*Tiempos inicial y final*/
    
    double t_init = 0;
    double t_finit = 20;
    double h = 0.001; // delta temporal nominal
    int puntos = (t_finit - t_init)/h +1;
    
    
    Runge_Kutta(X0, Y0, vX0, vY0, h, t_init, t_finit, puntos, cto);
    
    
 return 0;   
}



double Dx(double v)
{
    return v;
}

double Dv(double r, double mag_r)
{
    return -G*1.0*r/(mag_r*mag_r*mag_r);
}
/*
double Euler()
{
    
}
*/


double Runge_Kutta(double X0, double Y0, double vX0, double vY0, double h, double t_init, double t_finit, int puntos, int cto)
{
    
    
    /* Se declara los arrays a utilizar */
    
    double t[puntos];
    double r[puntos][2];
    double v[puntos][2];
  
         
    /* Condiciones iniciales del problema:*/
    
    t[0] = t_init;
    r[0][0] = X0;
    r[0][1] = Y0;
    v[0][0] = vX0;
    v[0][1] = vY0;
    
    
    /* Declaración de variables auxiliares ki asociadas al método de Runge Kutta*/
    //Nota: las variables K que tienen un solo sub-indice, estan asociadas a la ecuacion diferencial dx(t)/d(t) = v(t)
    //Nota: las variables K que tienen dos sub-indices, estan asociadas a la ecuacion diferencial dv(t)/d(t) = -G M r/|r^3|

    
    double k1x, k1y;
    double k2x, k2y;
    double k3x, k3y;
    double k4x, k4y;
    double prom1x, prom1y;
    
    double k11x, k11y;
    double k22x, k22y;
    double k33x, k33y;
    double k44x, k44y;
    double prom2x, prom2y;
    
    double r0x, r0y;
    double r1x, r1y;
    double r2x, r2y;
    double r3x, r3y;
    
    double v1x, v1y;
    double v2x, v2y;
    double v3x, v3y;
    
    
    /* Evolución del sistema */
    
    for(int i = 1 ; i< puntos;  i++)
    {
        r0x = r[i-1][0];
        r0y = r[i-1][1];
        k1x = Dx(v[i-1][0]);
        k1y = Dx(v[i-1][1]);    
        k11x = Dv(r[i-1][0],pow(r0x*r0x+r0y*r0y,0.5));
        k11y = Dv(r[i-1][1],pow(r0x*r0x+r0y*r0y,0.5));
            
       
        r1x = r[i-1][0] + (h*0.5) * k1x;
        r1y = r[i-1][1] + (h*0.5) * k1y;
        v1x = v[i-1][0] + (h*0.5) * k11x;
        v1y = v[i-1][1] + (h*0.5) * k11y;    
        k2x = Dx(v1x);
        k2y = Dx(v1y);
        k22x = Dv(r1x,pow(r1x*r1x+r1y*r1y,0.5));
        k22y = Dv(r1y,pow(r1x*r1x+r1y*r1y,0.5));
        
        
       
        r2x = r[i-1][0] + (h*0.5) * k2x;
        r2y = r[i-1][1] + (h*0.5) * k2y;
        r2x = v[i-1][0] + (h*0.5) * k22x;
        r2y = v[i-1][1] + (h*0.5) * k22y;
        k3x = Dx(v2x);
        k3y = Dx(v2y);
        k33x= Dv(r2x,pow(r2x*r2x+r2y*r2y,0.5));
        k33y= Dv(r2y,pow(r2x*r2x+r2y*r2y,0.5));
        
        
       
        r3x = r[i-1][0] + h * k3x;
        r3y = r[i-1][1] + h * k3y;
        v3x = v[i-1][0] + h * k33x;
        v3y = v[i-1][1] + h * k33y;
        k4x = Dx(v3x);
        k4y = Dx(v3y);
        k44x= Dv(r3x,pow(r3x*r3x+r3y*r3y,0.5));
        k44y= Dv(r3y,pow(r3x*r3x+r3y*r3y,0.5));
        
        //cout<<k11x<<","<<k11y<<"|"<<k22x<<","<<k22y<<"|"<<k33x<<","<<k33y<<endl;
        prom1x = (1.0/6.0)*(k1x + 2.0*k2x + 2.0*k3x + k4x);
        prom1y = (1.0/6.0)*(k1y + 2.0*k2y + 2.0*k3y + k4y);
        prom2x = (1.0/6.0)*(k11x + 2.0*k22x + 2.0*k33x + k44x);
        prom2y = (1.0/6.0)*(k11y + 2.0*k22y + 2.0*k33y + k44y);
    
        t[i] = t[i-1] + h;
        r[i][0] = r[i-1][0] + h * prom1x;
        r[i][1] = r[i-1][1] + h * prom1y;    
        v[i][0]= v[i-1][0] + h * prom2x;
        v[i][1]= v[i-1][1] + h * prom2y;
        /*if (t[i]>14.5)
        {
                cout<<t[i]<<" | "<<r[i][0]<<" | "<<r[i][1]<<" | "<<v[i][0]<<" | "<<v[i][1]<<" | "<<prom1x <<" | "<< prom1y<<" | " <<prom1x<<" | " << prom1y <<endl ;
        }*/
    }
    
    for(int i = 0; i< puntos; i++)
    {
         cout<<t[i]<<","<<r[i][0]<<","<<r[i][1]<<","<<v[i][0]<<","<<v[i][1]<< endl ;
    }
   
}
