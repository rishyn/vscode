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


    pnodo *lista;
    lista=NULL;

    float A,B , area ,resultado,promedio;
    int opcion , cantNodos =0;



    printf("menu \ninsertar medidas=1 \nmostrar lista=2 \nsalir=0");
    scanf("%d", &opcion);


    while(opcion != 0){
        if(opcion == 1){
            medidas();

            insertarEnLista(lista, area);
            cantNodos++;
        }
        if(opcion == 2){
            mostrarLista(lista);


        }

    }

    resultado =totalLista(lista);

    promedio  = resultado / cantNodos;


    printf("el promedio de las areas son %.2f ",promedio);









    return 0;
}















int medidas(){
    float area,A,B;

    printf("ingrese las medidas del cubo  \n");
    scanf("%f ", &A);
    scanf("%f ", &B);

    printf("las medidas son A=%.2f  , B=%.2f",A,B);

    area = A*B;

    return area;

}