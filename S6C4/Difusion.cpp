#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;
int main(){

    /*Constantes iniciales del problema-------------------------------------------------------------------*/
    
    double lado = 1;
    double v = 1e-4;
    double dx = 0.01;
    double t_finit = 2500;
    double t_init = 0;
    int puntos = lado/dx;
    double dt = 0.25*dx*dx/v;
    int puntosTemporales = (t_finit-t_init)/dt;
    
    /*Declaración de los array a utlizar------------------------------------------------------------------*/
    
    double x[puntos];
    double y[puntos];
    double matriz[puntos][puntos];
    
    double pasado[puntos][puntos];
    double presente[puntos][puntos];
    double futuro[puntos][puntos];
    
    /*Archivos de salida*/
    
    ofstream Datos_inicio;
    ofstream Datos_Evolucion_Periodico;
    ofstream Datos_Evolucion_FronteraFija;
    
    
    
    /* Condiciones iniciales del problema -----------------------------------------------------------------*/
    Datos_inicio.open("Datos_inicio.dat");
    
    for(int i = 0; i< puntos; i++)
    {
         for (int j = 0; j< puntos; j++)
         {
             if((i>20 && i<40) && (j>20 && j<60))
             {
                 matriz[i][j] = 100;
             }
             else
             {
                 matriz[i][j] = 50;
             }
         }
    }
    
    for(int i = 0; i< puntos;i++)
    {
        for(int j = 0; j< puntos;j++)
        {
            Datos_inicio<<matriz[i][j]<<",";
            presente[i][j] = matriz[i][j];
        }
        Datos_inicio<<endl;
    }
    Datos_inicio.close();
    
     /* Evolución del sistema caso periodico -----------------------------------------------------------------------------*/
    
   
        // Construimos el futuro
        Datos_Evolucion_Periodico.open("Datos_Evolucion_Periodico.dat");
        int cto = 0;
        for (int t = 0; t<= puntosTemporales; t++)
        {
            
             if(cto == 0 || cto % 20 == 0)
            {
                 for (int i = 0; i<puntos;i++)
                 {
                     for(int j = 0; j< puntos; j++)
                     {
                        Datos_Evolucion_Periodico<<presente[i][j]<<",";
                         
                     }
                  Datos_Evolucion_Periodico<<endl; 
                 }
             
                 
            }
            
            
            for (int i = 0; i<puntos;i++ )
            {
                    for (int j = 0; j< puntos; j++)
                    {
                        if (i>0 && j >0)
                        {
                            futuro[i][j] = (v*dt/(dx*dx))*(presente[i+1][j] + presente[i-1][j] -4*presente[i][j] + presente[i][j+1] + presente[i][j-1]) + presente[i][j];
                        }
                        else 
                        {
                         futuro[i][j]= presente[i][j];   
                        }
                        
                    }
                
            }
            
            for(int i = 0; i<puntos; i++)
            {
                for (int j = 0; j< puntos; j++)
                {
                    pasado[i][j] = presente[i][j];
                    presente[i][j]= futuro[i][j];
                }
            }
            
           cto = cto+1;
        }
    
    Datos_Evolucion_Periodico.close();
    
     /* Evolución del sistema caso frontera fija -----------------------------------------------------------------------------*/
    
   
        // Construimos el futuro
        Datos_Evolucion_FronteraFija.open("Datos_Evolucion_FronteraFija.dat");
        cto = 0;
        for (int t = 0; t<= puntosTemporales; t++)
        {
            
             if(cto == 0 || cto % 20 == 0)
            {
                 for (int i = 0; i<puntos;i++)
                 {
                     for(int j = 0; j< puntos; j++)
                     {
                        Datos_Evolucion_FronteraFija<<presente[i][j]<<",";
                         
                     }
                  Datos_Evolucion_FronteraFija<<endl; 
                 }
             
                 
            }
            
            
            for (int i = 0; i<puntos;i++ )
            {
                    for (int j = 0; j< puntos; j++)
                    {
                        if (i>0 && j >0 && i <puntos-1 && j <puntos-1)
                        {
                            futuro[i][j] = (v*dt/(dx*dx))*(presente[i+1][j] + presente[i-1][j] -4*presente[i][j] + presente[i][j+1] + presente[i][j-1]) + presente[i][j];
                        }
                        else 
                        {
                         futuro[i][j]= 50;   
                        }
                        
                    }
                
            }
            
            for(int i = 0; i<puntos; i++)
            {
                for (int j = 0; j< puntos; j++)
                {
                    pasado[i][j] = presente[i][j];
                    presente[i][j]= futuro[i][j];
                }
            }
            
           cto = cto+1;
        }
    
    Datos_Evolucion_FronteraFija.close();
    
    return 0;
}
