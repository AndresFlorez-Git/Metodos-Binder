#include<iostream>
#include<math.h>


double funcion(double x);
    
int main(){
   double fina;
   double inicio, h;
   int puntos;
   /*
   std::cout<<"ingrese punto inicial: ";
   std::cin>>inicio;
   std::cout<<"ingrese punto final: ";
   std::cin>>fina;
   std::cout<<"ingrese la cantidad de puntos deseado: ";
   std::cin>>puntos;
   */
   
   inicio = 0;
   fina = 7;
   puntos = 100;
   
    
   double espacio[puntos];
   double array[puntos] ;
   double derivada[puntos];
   double delta = (fina - inicio)/puntos ;
   
    
    
   for(int i=0; i<puntos;i++){
      espacio[i] = inicio +i*delta;
      
   }
    
   h = espacio[1]-espacio[0];
   
   for(int i = 0; i<puntos;i++)
   {
      
       array[i] = funcion(espacio[i]);
       derivada[i] = (funcion(espacio[i]+h/2)-funcion(espacio[i]-h/2))/h;
       std:: cout<<espacio[i]<<","<<array[i]<<","<<derivada[i]<<std:: endl;
   }
       
   
    
    return 0;
}

double funcion(double x)
{
    return cos(x);
}



