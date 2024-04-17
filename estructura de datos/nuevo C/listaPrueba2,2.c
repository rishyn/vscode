#include<stdlib.h>
#include<stdio.h>

//Estructura Nodo
typedef struct snodo{
    int dato;
    struct snodo *sig;
}tnodo;

typedef tnodo *pnodo;



void insertarEnLista (pnodo *inicial, float num){
    pnodo nuevo; //creamos un nodo para el nuevo elemento
    nuevo = (pnodo)malloc(sizeof(pnodo)); //reservamos memoria
    nuevo->dato = num; //asignamos el valor al nodo
    nuevo->sig = *inicial; //enlazamos el nodo a la lista (incial)
    *inicial = nuevo; //Cabeza pasa a ser el último nodo agregado
}


int esVacia (pnodo inicial){//Retornamos 1 si la lista está vacía, 0 en caso contrario
	int vacia=1;
	if(inicial!=NULL)
		vacia=0;
    return vacia;
}


void mostrarLista(pnodo actual){//actual = inicial (al iniciar la función)
    while(actual != NULL){ //Mientras actual no sea NULL
        printf("%d ",actual->dato); //Imprimimos el valor del nodo
        actual = actual->sig; //Pasamos al siguiente nodo
    }
    printf("\n");
}

int totalLista(pnodo actual){//actual = inicial (al iniciar la función)
    float total=0;
    while(actual != NULL){ //Mientras actual no sea NULL
        total+=actual->dato; //Imprimimos el valor del nodo
        actual = actual->sig; //Pasamos al siguiente nodo
    }


    return total;
}










int main () {


    pnodo *lista1,*lista2;
    lista1=NULL;
    lista2=NULL;



    float A,B , area ,resultado,resultado2,promedio;
    int opcion , cantNodos =0;



    printf("menu \nhacer pago =1 \nhacer cobro =2 \nsalir=0");
    scanf("%d", &opcion);


    while(opcion != 0){
        if(opcion == 1){
            float monto;

            printf("ingrese cuando va a pagar \n");
            scanf("%f ", &monto);

            insertarEnLista(lista1, monto);

        }
        if(opcion == 2){
            float monto;
            printf("ingrese cuanto va a cobrar \n");
            scanf("%f", &monto);

            insertarEnLista(lista2 ,monto);


        }

    }

    resultado =totalLista(lista1);
    resultado2 =totalLista(lista2);
    printf("total lista paga es  %.2f  total lista cobro  %.2f", resultado,resultado2);

    promedio = resultado+ resultado2;


    printf("la suma total de las trasacciones es %.2f\n ",promedio);









    return 0;
}















