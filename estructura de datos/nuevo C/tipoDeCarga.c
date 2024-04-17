#include<stdlib.h>
#include<stdio.h>
#include<string.h>

int main(){
    char tipo_carga[10];
    float A,B,C, volumen,resultado2;

    printf("Ingrese q tipo de carga es \n");

    gets(tipo_carga);


    printf("ingrese las medidas A,B,C del objeto \n") ;
    scanf("%f",&A);
    scanf("%f",&B);
    scanf("%f",&C);


    printf("su carga es de tipo %s \n ",tipo_carga);

    printf("Las medidas son A=%.2f, B=%.2f , C=%.2f\n",A,B,C);

    volumen = A*B*C;

    if(volumen > 1000){

        resultado2= (volumen * 5) /100;
        volumen = resultado2 + volumen;

        printf("El volumen total de su objeto es : %.2f",volumen);
    }
    else{
        printf("El volumen total de su objeto es : %.2f",volumen);


    }




    return 0;
}