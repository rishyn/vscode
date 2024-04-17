#include<stdio.h>
#include<stdlib.h>



typedef struct nodo_d{
    float dato;//el tipo de dato a insertar puede ser cualquiera

    struct nodo_d *ant ,*sig;
}nodo_d;

typedef struct ldoble{
    nodo_d *prim ,*ult;

}lista;


//insertar al principio de la lista como PILA
lista insertar_lifo (lista l,float d){
    nodo_d *nuevo;
    nuevo = (nodo_d* ) malloc(sizeof(nodo_d));
    nuevo->dato = d;
    nuevo->ant =NULL;
    nuevo->sig = l.prim;

    if (l.prim == NULL) //lista vacia, l.prim y l.ult son NULL
        l.ult = nuevo;
    else
        l.prim->ant = nuevo;
    l.prim = nuevo;
    return l;

}


int main (){
    nodo_d *p;//puntero para recorrer la lista
    float f;
    lista l;// la lista propiamente dicha



    l.prim = NULL;
    l.ult = NULL;

    l  = insertar_lifo (l,f); //insertar los numeros a la lista


    for (p =l.prim ; p != NULL ; p = p->sig){
        printf ("Dato = %6.2f \n ",p->dato);
    }





    return 0;
}