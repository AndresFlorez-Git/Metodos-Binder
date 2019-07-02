#include<iostream>

double factorial(double);
     
int main(){
   double n;
   std::cout<<"Inserte el número: ";
   std::cin>>n;
   std::cout<<"El factorial de "<<n<<" es: "<< factorial(n);
   return 0;
}

double factorial(double n)
{
   double b;
   b = n;
   for(int i = 1; i < n ; i++)
   {
        b = b*(n-i);
       
   }
   return b;
}

