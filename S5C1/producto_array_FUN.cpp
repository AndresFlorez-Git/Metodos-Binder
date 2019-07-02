#include<iostream>



int producto(int *arreglo, int *arreglo2);
int dot(int *arreglo, int *arreglo2);

int main()
{
    int *pointer1;
    int *pointer2;

    int arreglo1[5] = {1, 2, 3, 4, 5};
    int arreglo2[5] = {10, 20, 30, 40, 50};

    pointer1 = arreglo1;
    pointer2 = arreglo2;
   std:: cout<<"La multiplicación por elementos es:";
   producto(pointer1,pointer2);
   std:: cout<<"el producto punto da:";
   dot(pointer1,pointer2);
       
   return 0;
}



int producto(int *arreglo, int *arreglo2)
{
 
 for(int i = 0; i<5; i++)
 {
  
  std::cout<<arreglo[i]*arreglo2[i]<<" ,";   
 }
}

int dot(int *arreglo, int *arreglo2)
{
 int w;
 w = 0;
 
 for(int i = 0; i<5; i++)
 {
  w = w + arreglo[i]*arreglo2[i];
 }
  std::cout<<w<<" ,";
}