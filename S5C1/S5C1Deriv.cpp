#include<iostream>
#include<math.h>


//double derivada(double x)
    
int main(){
   double fina;
   double inicio;
   int puntos;
   inicio = 0;
   fina = 10;
   puntos = 10;
    
    
   double espacio[puntos];
   double delta = (fina - inicio)/puntos ;
   
    
    
   for(int i=0; i<puntos;i++){
      espacio[i] = inicio +i*delta;
      std:: cout<<espacio[i]<<std:: endl;
      
   }
    
    return 0;
}


