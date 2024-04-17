#include<stdio.h>
#include<time.h>

int main (){
    int numero,i ;
    srand(time(0));
    numero = 1000000;
    printf ("%d/n",numero);
    for (i=numero; i>0; i--)
        printf ("%d/n",i);

    return 0;
}