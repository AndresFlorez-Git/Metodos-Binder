#include<iostream>

//int fact(n);
     
int main(){
   double num1,num2, cto;
   std::cout<<"Inserte el primer valor entero: ";
   std::cin>> num1;
   std::cout<<"Inserte el segundo valor entero: ";
   std::cin>> num2; 
   std::cout<<"Los numeros primos entre "<<num1<<" y "<<num2<<" son: ";
   for(int i = num1; i <= num2 ; i++)
   {
       cto = 1;
       for(int j = 2; j<i; j++)
       {
          cto = (i%j)*cto; 
       }
       if(cto != 0)
       {
       std::cout<<i<<", ";
       }   
      
   }
       
   return 0;
}