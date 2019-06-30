#include<iostream>

//int fact(n);
     
int main(){
   double n,b;
   std::cin>>n;
   b = n;
   
 
   for(int i = 1; i < n ; i++)
   {
        b = b*(n-i);
       
   }
       
   std::cout<<"El factorial de"<<n<<" es:"<<b;

   return 0;
}