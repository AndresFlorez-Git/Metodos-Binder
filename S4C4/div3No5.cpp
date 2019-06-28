#include<iostream>

//int fact(n);
     
int main(){
   double n,b;
   n = 100;
   
   std::cout<<"Los numeros divisibles entre 3 y no entre 5 son:"; 
 
   for(int i = 0; i <= n ; i++)
   {
        if (i%3 == 0 && i%5 != 0)
       {
         std::cout<<i<<", ";  
       }
   }
       
   return 0;
}