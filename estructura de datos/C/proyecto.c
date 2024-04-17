#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
typedef struct nodo{
    int dato;
    struct nodo* siguiente;
    struct nodo* atras;
} nodo;
nodo* primero = NULL;
nodo* ultimo = NULL;
int i;
int totalGuardias;
void guardias(int totalGuardias, int derecha, int izquierda){ //aun no terminada

}

void CrearLista(int totalGuardias){ //ingresar el total de guardias
    for (i = 1; i <= totalGuardias; i++){
    nodo* nuevo = (nodo*) malloc(sizeof(nodo));
    nuevo->dato = i;

    if(primero==NULL){
        primero = nuevo;
        primero->siguiente = primero;
        ultimo = primero;
        primero->atras = ultimo;
    }
    else{
        ultimo->siguiente = nuevo;
        nuevo->siguiente = primero;
        nuevo->atras = ultimo;
        ultimo = nuevo;
        primero->atras = ultimo;
    }
    }
}

void desplegarLista(){ //mostrar la lista
    nodo* actual = (nodo*) malloc(sizeof(nodo));
    actual = primero;
    if(primero!=NULL){
        do{
            printf("\n %d", actual->dato);
            actual = actual->siguiente;
        }while(actual != primero);
    }
    else{
        printf("\n La Lista se encuenta vacia\n\n");
    }
}

int main(){ //Funcion principal
    printf("Ingrese el tamaño de lista; ");
    scanf("%d", &totalGuardias);
    CrearLista(totalGuardias);
    desplegarLista();
    return 0;
}
