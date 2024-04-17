#include<stdio.h>
#include<stdlib.h>


typedef struct snodo {
    int dato;
    struct snodo *ant;
    struct snodo *izqu;
    struct snodo *dere;

}tnodo;

typedef tnodo *pnodo;


//si vacia = 0 esta llena  si vacia =1 significa q esta vacia

int esVacia (pnodo inicial){
    int vacia = 0;
    if (inicial == NULL){
        vacia = 1 ;
    }

    return vacia;
}

pnodo front (pnodo inicial){
    pnodo nuevo;
    nuevo = (pnodo)malloc (sizeof(pnodo)); // reservamos memoria
    nuevo->dato = inicial->dato;
    return nuevo;

}

pnodo endP (pnodo actual){
    if(actual = NULL){
        while(actual->izqu != NULL){ // mientras actual no sea el ultimo nodo
            actual = actual->izqu; //pasamos al siguiente nodo

        }
    }
    else{
        printf("La lista esta vacia. \n");

    }
    return actual;

}


pnodo CrearNodo (int numero){
    pnodo nuevo;
    nuevo =(pnodo)malloc(sizeof(pnodo));
    nuevo->dato = numero;
    return nuevo;
}


void VinculosNodo (pnodo *actual, pnodo anterior,pnodo izquierda ,pnodo derecha){
    (*actual)->ant = anterior;
    (*actual)->izqu = izquierda;
    (*actual)->dere = derecha;

}

void mostrarLista (pnodo actual ){ //actual = inicial (al iniciar la funcion)
    if(actual != NULL){ //Mientras actual no sea NULL
        printf("Dato: %d\n",actual->dato);
        mostrarLista(actual->izqu);
        mostrarLista(actual->dere);

    }
    printf("\n");
}


int main(){
    //Unidad 2 TDA - taller con colas

    pnodo nodo1= CrearNodo (1);
    pnodo nodo2= CrearNodo (2);
    pnodo nodo3= CrearNodo (4);
    pnodo nodo4= CrearNodo (3);
    pnodo nodo5= CrearNodo (5);
    pnodo nodo6= CrearNodo (6);

    VinculosNodo(&nodo1,NULL,nodo2,nodo4);
    VinculosNodo(&nodo2,nodo1,nodo3,nodo5);
    VinculosNodo(&nodo3,nodo2,NULL,NULL);
    VinculosNodo(&nodo4,nodo1,NULL,nodo6);
    VinculosNodo(&nodo5,nodo2,NULL,NULL);
    VinculosNodo(&nodo6,nodo4,NULL,NULL);

    mostrarLista(nodo1);
    return 0;
    
}
