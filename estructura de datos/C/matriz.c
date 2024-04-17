#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define tamano 3
#define xd
/*
void multiplicar (int A[xd][xd] , int B[xd][xd]  ,int C[xd][xd] ,int m,int n,int p ){

    int i, j, k;
    for (i=0 ; i<m ; i++ ){
        for(j=0 ; j<n ; j++){
            for(k=0 ; k<p ; k++ ){
                C[i][k] = C [i][k];
            }
        }
    }

    return;
}
*/

int main(){
    clock_t tiempo_inicio, tiempo_final;
    double segundos;
    tiempo_inicio = clock();


    //srand(time(NULL));
    int i,j,k;
    int N=tamano,P=tamano,M=tamano;
    int matriz2 [N] [P],matriz [M] [N],matrizF[M] [P],x1,y1,x2,y2,x3,y3; //matricez


    //matriz 1 creacion con numeros aleatorios
    for (x1=0 ; x1<M ; x1++){
        for(y1=0 ; y1<N ; y1++){
            matriz [x1][y1] =  rand() % 256;

        }
    }
   //mostrar matriz 1
   printf( "matriz 1\n");
   for(x1 = 0 ; x1<M; x1++){
        for(y1=0 ; y1<N; y1++){

            printf("%d ",matriz[x1] [y1]);
        }
        printf("\n");
    }


   /* //matriz 2 creacion con numeros aleatorios
    for (x2=0 ; x2<N ; x2++){
        for(y2=0 ; y2<P ; y2++){
            matriz2 [x2] [y2]=  rand() %256;
        }
    }

    //vaciar matris de resultado
    for (x3=0 ; x3<M ; x3++){
        for (y3=0 ; y3<P ; y3++){
            matrizF [x3] [y3] = 0;
        }
    }
    */


    /*
    printf( "En Forma Tabular ------->\n");
    printf( "Elemento       velor \n");
    for ( x = 0 ; x<600 ; x++){
        for( y = 0 ; y<606 ; y++){
            printf("matriz [%d] [%d]= %d\n",x,y,matriz [x] [y]);
        }
    }
    */

   /*
    printf("matriz 2 \n");
    // mostrar matriz 2
    for( x2=0 ; x2<N ; x2++){
        for(y2=0 ; y2<P ; y2++){
            printf("%d ",matriz2[x2] [y2]);
        }
        printf("\n");
    }
    //matrizF[M] [P]= matrizF[M] [P] + matriz[M] [N]* matriz2[N][P];

    //multiplicar( matriz,matriz2 , matrizF,M , N , P );



    //matriz 3
    printf("matriz 3\n");
    for(i=0 ; i<M ; i++){
        for(k=0 ; k<P ; k++){
            printf("%d ",matrizF[i] [k]);
        }
        printf("\n");
    }

    */
    tiempo_final = clock();
    segundos = (double) (tiempo_inicio - tiempo_final ) / CLOCKS_PER_SEC;
    printf("%f",segundos);




    return 0;
}


//crear otra matriz y aprender a multiplicar