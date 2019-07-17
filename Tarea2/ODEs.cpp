#include<iostream>
#include<math.h>
#include<fstream>
using namespace std;

double G1 = 6.674e-11; //Constante de gravitacion universal [N m**2/ kg**2]
double UA = 149597870700; // unidad astronomica en metros
double M = 1.989e30; // masa del sol
double yr = 31536000; // segundos al año
double G = G1*(1/(UA*UA*UA))*(M)*(yr*yr); // Constante de gravitacion universal [UA^3 /(Masa_Solar yr^2)]

double Euler(double, double, double, double, double, double, double, int, int);
double Leap_Frog(double, double, double, double, double, double, double, int, int);
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
    double h = 0.01; // delta temporal nominal
    for(int i = 0;i<3;i++)
    {
        int puntos = (t_finit - t_init)/h +1;
        Euler(X0, Y0, vX0, vY0, h, t_init, t_finit, puntos, cto);
        Leap_Frog(X0, Y0, vX0, vY0, h, t_init, t_finit, puntos, cto);
        Runge_Kutta(X0, Y0, vX0, vY0, h, t_init, t_finit, puntos, cto);
        h = h*0.1;
        cto = cto +1;
    }
    
 return 0;   
}



double Dx(double v)
{
    return v;
}

double Dv(double r, double mag_r)
{
    return -G*r/(mag_r*mag_r*mag_r);
}

double Euler(double X0, double Y0, double vX0, double vY0, double h, double t_init, double t_finit, int puntos, int cto)
{
    if (cto ==1)
    {
        ofstream Euler1;
        Euler1.open("Euler1.dat");
     /*Se declara los Arrays a utilizar*/
        double t[puntos];
        double r[puntos][2];
        double v[puntos][2];
      /* Condiciones iniciales del problema:*/
            
            t[0] = t_init;
            r[0][0] = X0;
            r[0][1] = Y0;
            v[0][0] = vX0;
            v[0][1] = vY0;
       /*Evolucin del sistema*/
        for (int i = 0; i<puntos;i++)
        {
            
            v[i+1][0] = v[i][0] + h*Dv(r[i][0],pow(r[i][0]*r[i][0]+r[i][1]*r[i][1],0.5));
            v[i+1][1] = v[i][1] + h*Dv(r[i][1],pow(r[i][0]*r[i][0]+r[i][1]*r[i][1],0.5));
            r[i+1][0] = r[i][0] + v[i][0]*h;
            r[i+1][1] = r[i][1] + v[i][1]*h;
            
            t[i+1] = t[i] + h;
        }
        for(int i = 0; i< puntos; i++)
        {
             Euler1<<t[i]<<","<<r[i][0]<<","<<r[i][1]<<","<<v[i][0]<<","<<v[i][1]<< endl ;
        }  
        Euler1.close();
    }
    if (cto ==2)
    {
        ofstream Euler2;
        Euler2.open("Euler2.dat");
     /*Se declara los Arrays a utilizar*/
        double t[puntos];
        double r[puntos][2];
        double v[puntos][2];
      /* Condiciones iniciales del problema:*/
            
            t[0] = t_init;
            r[0][0] = X0;
            r[0][1] = Y0;
            v[0][0] = vX0;
            v[0][1] = vY0;
       /*Evolucin del sistema*/
        for (int i = 0; i<puntos;i++)
        {
            v[i+1][0] = v[i][0] + h*Dv(r[i][0],pow(r[i][0]*r[i][0]+r[i][1]*r[i][1],0.5));
            v[i+1][1] = v[i][1] + h*Dv(r[i][1],pow(r[i][0]*r[i][0]+r[i][1]*r[i][1],0.5));
            r[i+1][0] = r[i][0] + v[i][0]*h;
            r[i+1][1] = r[i][1] + v[i][1]*h;
            
            t[i+1] = t[i] + h;
        }
        for(int i = 0; i< puntos; i++)
        {
             Euler2<<t[i]<<","<<r[i][0]<<","<<r[i][1]<<","<<v[i][0]<<","<<v[i][1]<< endl ;
        }  
        Euler2.close();
    }
    if (cto ==3)
    {
        ofstream Euler3;
        Euler3.open("Euler3.dat");
     /*Se declara los Arrays a utilizar*/
        double t[puntos];
        double r[puntos][2];
        double v[puntos][2];
      /* Condiciones iniciales del problema:*/
            
            t[0] = t_init;
            r[0][0] = X0;
            r[0][1] = Y0;
            v[0][0] = vX0;
            v[0][1] = vY0;
       /*Evolucin del sistema*/
        for (int i = 0; i<puntos;i++)
        {
            v[i+1][0] = v[i][0] + h*Dv(r[i][0],pow(r[i][0]*r[i][0]+r[i][1]*r[i][1],0.5));
            v[i+1][1] = v[i][1] + h*Dv(r[i][1],pow(r[i][0]*r[i][0]+r[i][1]*r[i][1],0.5));
            r[i+1][0] = r[i][0] + v[i][0]*h;
            r[i+1][1] = r[i][1] + v[i][1]*h;
            
            t[i+1] = t[i] + h;
        }
        for(int i = 0; i< puntos; i++)
        {
             Euler3<<t[i]<<","<<r[i][0]<<","<<r[i][1]<<","<<v[i][0]<<","<<v[i][1]<< endl ;
        } 
        Euler3.close();
    }
}

double Leap_Frog(double X0, double Y0, double vX0, double vY0, double h, double t_init, double t_finit, int puntos, int cto)
{
    if (cto ==1)
    {
        ofstream LeapFrog1;
        LeapFrog1.open("LeapFrog1.dat");
     /*Se declara los Arrays a utilizar*/
        double t[puntos];
        double r[puntos][2];
        double v[puntos][2];
      /* Condiciones iniciales del problema:*/
            
            t[0] = t_init;
            r[0][0] = X0;
            r[0][1] = Y0;
            v[0][0] = vX0;
            v[0][1] = vY0;
        
        /*Tiempo Anterior*/
        double vantx = v[0][0] - h*Dv(r[0][0],pow(r[0][0]*r[0][0]+r[0][1]*r[0][1],0.5));
        double vanty = v[0][1] - h*Dv(r[0][1],pow(r[0][0]*r[0][0]+r[0][1]*r[0][1],0.5));
       /*Evolucion inicial del sistema*/
        v[1][0] = vantx + 2*h*Dv(r[0][0],pow(r[0][0]*r[0][0]+r[0][1]*r[0][1],0.5));
        v[1][1] = vanty + 2*h*Dv(r[0][1],pow(r[0][0]*r[0][0]+r[0][1]*r[0][1],0.5));
        r[1][0] = r[0][0] + h*v[0][0];
        r[1][1] = r[0][1] + h*v[0][1];
        /*Evolucion general del sistema*/
        for (int i = 1; i<puntos;i++)
        {
            
            v[i+1][0] = v[i-1][0] + 2.0*h*Dv(r[i][0],pow(r[i][0]*r[i][0]+r[i][1]*r[i][1],0.5));
            v[i+1][1] = v[i-1][1] + 2.0*h*Dv(r[i][1],pow(r[i][0]*r[i][0]+r[i][1]*r[i][1],0.5));
            r[i+1][0] = r[i-1][0] + 2.0*v[i][0]*h;
            r[i+1][1] = r[i-1][1] + 2.0*v[i][1]*h;
            
            t[i+1] = t[i] + h;
        }
        for(int i = 0; i< puntos; i++)
        {
             LeapFrog1<<t[i]<<","<<r[i][0]<<","<<r[i][1]<<","<<v[i][0]<<","<<v[i][1]<< endl ;
        }  
        LeapFrog1.close();
    }
    if (cto ==2)
    {
        ofstream LeapFrog2;
        LeapFrog2.open("LeapFrog2.dat");
     /*Se declara los Arrays a utilizar*/
        double t[puntos];
        double r[puntos][2];
        double v[puntos][2];
      /* Condiciones iniciales del problema:*/
            
            t[0] = t_init;
            r[0][0] = X0;
            r[0][1] = Y0;
            v[0][0] = vX0;
            v[0][1] = vY0;
        
        /*Tiempo Anterior*/
        double vantx = v[0][0] - h*Dv(r[0][0],pow(r[0][0]*r[0][0]+r[0][1]*r[0][1],0.5));
        double vanty = v[0][1] - h*Dv(r[0][1],pow(r[0][0]*r[0][0]+r[0][1]*r[0][1],0.5));
       /*Evolucion inicial del sistema*/
        v[1][0] = vantx + 2*h*Dv(r[0][0],pow(r[0][0]*r[0][0]+r[0][1]*r[0][1],0.5));
        v[1][1] = vanty + 2*h*Dv(r[0][1],pow(r[0][0]*r[0][0]+r[0][1]*r[0][1],0.5));
        r[1][0] = r[0][0] + h*v[0][0];
        r[1][1] = r[0][1] + h*v[0][1];
        /*Evolucion general del sistema*/
        for (int i = 1; i<puntos;i++)
        {
            
            v[i+1][0] = v[i-1][0] + 2.0*h*Dv(r[i][0],pow(r[i][0]*r[i][0]+r[i][1]*r[i][1],0.5));
            v[i+1][1] = v[i-1][1] + 2.0*h*Dv(r[i][1],pow(r[i][0]*r[i][0]+r[i][1]*r[i][1],0.5));
            r[i+1][0] = r[i-1][0] + 2.0*v[i][0]*h;
            r[i+1][1] = r[i-1][1] + 2.0*v[i][1]*h;
            
            t[i+1] = t[i] + h;
        }
        for(int i = 0; i< puntos; i++)
        {
             LeapFrog2<<t[i]<<","<<r[i][0]<<","<<r[i][1]<<","<<v[i][0]<<","<<v[i][1]<< endl ;
        }  
        LeapFrog2.close();
    }
    if (cto ==3)
    {
        ofstream LeapFrog3;
        LeapFrog3.open("LeapFrog3.dat");
     /*Se declara los Arrays a utilizar*/
        double t[puntos];
        double r[puntos][2];
        double v[puntos][2];
      /* Condiciones iniciales del problema:*/
            
            t[0] = t_init;
            r[0][0] = X0;
            r[0][1] = Y0;
            v[0][0] = vX0;
            v[0][1] = vY0;
        
        /*Tiempo Anterior*/
        double vantx = v[0][0] - h*Dv(r[0][0],pow(r[0][0]*r[0][0]+r[0][1]*r[0][1],0.5));
        double vanty = v[0][1] - h*Dv(r[0][0],pow(r[0][0]*r[0][0]+r[0][1]*r[0][1],0.5));
       /*Evolucion inicial del sistema*/
        v[1][0] = vantx + 2*h*Dv(r[0][0],pow(r[0][0]*r[0][0]+r[0][1]*r[0][1],0.5));
        v[1][1] = vanty + 2*h*Dv(r[0][0],pow(r[0][0]*r[0][0]+r[0][1]*r[0][1],0.5));
        r[1][0] = r[0][0] + h*v[0][0];
        r[1][1] = r[0][1] + h*v[0][1];
        /*Evolucion general del sistema*/
        for (int i = 1; i<puntos;i++)
        {
            
            v[i+1][0] = v[i-1][0] + 2.0*h*Dv(r[i][0],pow(r[i][0]*r[i][0]+r[i][1]*r[i][1],0.5));
            v[i+1][1] = v[i-1][1] + 2.0*h*Dv(r[i][1],pow(r[i][0]*r[i][0]+r[i][1]*r[i][1],0.5));
            r[i+1][0] = r[i-1][0] + 2.0*v[i][0]*h;
            r[i+1][1] = r[i-1][1] + 2.0*v[i][1]*h;
            
            t[i+1] = t[i] + h;
        }
        for(int i = 0; i< puntos; i++)
        {
             LeapFrog3<<t[i]<<","<<r[i][0]<<","<<r[i][1]<<","<<v[i][0]<<","<<v[i][1]<< endl ;
        }  
        LeapFrog3.close();
    }
    
}




double Runge_Kutta(double X0, double Y0, double vX0, double vY0, double h, double t_init, double t_finit, int puntos, int cto)
{
    
    if (cto ==1)
    {
        ofstream RK1;
        RK1.open("RK1.dat");
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
             RK1<<t[i]<<","<<r[i][0]<<","<<r[i][1]<<","<<v[i][0]<<","<<v[i][1]<< endl ;
        }
        RK1.close();
    } 
    
    if (cto ==2)
    {
        ofstream RK2;
        RK2.open("RK2.dat");
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
             RK2<<t[i]<<","<<r[i][0]<<","<<r[i][1]<<","<<v[i][0]<<","<<v[i][1]<< endl ;
        }
        RK2.close();
    }
    
    if (cto ==3)
    {
        ofstream RK3;
        RK3.open("RK3.dat");
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
             RK3<<t[i]<<","<<r[i][0]<<","<<r[i][1]<<","<<v[i][0]<<","<<v[i][1]<< endl ;
        }
        RK3.close();
    }
       
    }
