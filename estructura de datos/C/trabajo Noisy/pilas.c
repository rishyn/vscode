#include <stdio.h>
#include <stdlib.h>

struct Node {
    int dato;
    struct Node* sig;
};

struct Node* push(struct Node* cima, int dato) {
    struct Node* nuevoNodo = (struct Node)malloc(sizeof(struct Node));
    nuevoNodo->dato = dato;
    nuevoNodo->sig = cima;
    return nuevoNodo;
}

struct Node desapila(struct Node* cima) {
    if (cima == NULL) {
        printf("La pila esta vacia.\n");
        return NULL;
    }
    struct Node* temp = cima;
    cima = cima->sig;
    free(temp);
    return *cima;
}

void ImprimirPila(struct Node* cima) {
    struct Node* actual = cima;
    while (actual != NULL) {
        printf("%d -> ", actual->dato);
        actual = actual->sig;
    }
    printf("NULL\n");
}

int sumatoriaP(struct Node* cima) {
    int suma = 0;
    struct Node* actual = cima;
    while (actual != NULL) {
        suma += actual->dato;
        actual = actual->sig;
    }
    return suma;
}


int main() {
    struct Node* cima = NULL;




    // Apilar elementos
    cima = push(cima, 6);
    cima = push(cima, 7);
    cima = push(cima, 8);
    cima = push(cima, 4);
    cima = push(cima, 1);



    ImprimirPila(cima);

    // Desapilar elementos
    cima = desapila(cima);
    cima = desapila(cima);

    ImprimirPila(cima);

    int suma = sumatoriaP(cima);
    printf("Sumatoria de la pila: %d\n", suma);

    return 0;
}
