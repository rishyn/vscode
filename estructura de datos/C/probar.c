#include<stdio.h>
#include<stdlib.h>

typedef struct lista_doble{
    int elemento;
    struct lista_doble *siguiente, *anterior;

}listaD_t;

void crearListaD(listaD_t **listaD);

int main (){
    FILE *archivo;


    listaD_t *listaD;

    archivo = fopen("guardias.in", "r");
    /*"r" : abrir un archivo para lectura, el fichero debe existir.
    "w" : abrir un archivo para escritura, se crea si no existe o se sobreescribe si existe.
    "a" : abrir un archivo para escritura al final del contenido, si no existe se crea.
    "r+" : abrir un archivo para lectura y escritura, el fichero debe existir.
    "w+" : crear un archivo para lectura y escritura, se crea si no existe o se sobreescribe si existe.
    "r+b ó rb+" : Abre un archivo en modo binario para actualización (lectura y escritura).
    "rb" : Abre un archivo en modo binario para lectura. */

    while (1){
        int a;
        a =fgetc(archivo);
        printf("%c",a);

        if (feof(archivo)){
            break;

        }

    }


    /* escribir en un archivo fprintf(archivo,"%d",3);   */
    fclose(archivo);
    return 0;
}

void crearListaD(listaD_t  **listaD){
    *listaD = (listaD_t *)malloc(sizeof(listaD_t));
    if(listaD == NULL){
        printf("ERROR");
        exit(1);
    }

}