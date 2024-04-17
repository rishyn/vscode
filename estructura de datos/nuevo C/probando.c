#include<stdio.h>
#include<stdlib.h>

int main (){
    int numNodos=7;
    int matriz[100][100];

    for (int i = 0; i < numNodos; i++){
        for(int j = 0; j < numNodos; j++){
            matriz[i][j] = 999999;
            printf("matriz asociada \n fila[%d]\n columna[%d]",matriz[i][j]);
        }
        printf("\n");
    }










    return 0;
}