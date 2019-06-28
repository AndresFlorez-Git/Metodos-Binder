#include<iostream>

//int fact(n);
     
int main(){
   double n,b;
   n = 7;
   b = n;
   
 
   for(int i = 1; i < n ; i++)
   {
        b = b*(n-i);
       
   }
       
   std::cout<<"El factorial de"<<n<<" es:"<<b;

   return 0;
}


