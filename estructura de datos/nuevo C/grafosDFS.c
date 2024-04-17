//los nodos lo comun, aristas son los q unen a los
//nodos y etas pueden tener su peso
// minuto 1 12 22 el profe se caga de risa

#include<stdio.h>
#include<stdlib.h>

#define MAX_NODOS 100
#define INF 999999
//matriz de adyasencia
typedef struct {
    int cantNodos;
    int MatrizAd[MAX_NODOS][MAX_NODOS];//matriz de adyacencia
}Grafo;



Grafo* crearGrafo(int numNodos){
    Grafo* grafo1 = (Grafo*)malloc(sizeof(Grafo));
    grafo1->cantNodos = numNodos;//definimos la cantidad de vertices que tendra el grafo
    for (int i = 0; i < numNodos; i++) {
        for (int j = 0; j < numNodos; j++) {
            grafo1->MatrizAd[i][j] = INF;//La matriz de adyacencia tendrá una dimensión = n^2
        }
    }
    return grafo1;
}
//char name[15] =0; para poder ingresar nombres en el codigo en los nodos en ves de numeros
void insertarArista(Grafo* grafop, int inicio, int destino, int distancia) {
    grafop->MatrizAd[inicio][destino] = distancia;
    grafop->MatrizAd[destino][inicio] = distancia;//si queremos implementar un grafo dirigido, omitimos una inserción
}

//Depth First Search
void DFS(Grafo* grafop, int nodo, int destino, int visitados[], int camino[], int distCam, int distMax) {
    visitados[nodo] = 1;
    camino[nodo] = 1;
    if (nodo == destino) {
        printf("Camino encontrado: ");//Se muestran los nodos del camino
        for (int i = 0; i < grafop->cantNodos; i++)//se asume q los nodos del grafo estan ordenados del camino del mayor al menor
            if (camino[i] == 1)
                printf("%d ", i);
        printf("\nPeso total: %d\n", distCam);
    }
    else
        for (int i = 0; i < grafop->cantNodos; i++)
            if (grafop->MatrizAd[nodo][i] != INF && !visitados[i]) {
                int nuevoPesoCamino = distCam + grafop->MatrizAd[nodo][i];
                if (nuevoPesoCamino <= distMax)
                    DFS(grafop, i, destino, visitados, camino, nuevoPesoCamino, distMax);
            }
    // Retroceder
    visitados[nodo] = 0;
    camino[nodo] = 0;
}



void buscarCamino(Grafo* grafop, int inicio, int destino, int distMax) {
    int visitados[MAX_NODOS] = {0};
    int camino[MAX_NODOS] = {0};

    printf("Caminos desde %d hasta %d con peso máximo %d:\n", inicio, destino, distMax);
    DFS(grafop, inicio, destino, visitados, camino, 0, distMax);
}


/*
void encontrarCaminoMenorPeso(Grafo* grafop, int inicio, int destino) {
    int visitados[MAX_NODOS] = {0};
    int camino[MAX_NODOS] = {0};
    int pesoMin = INF;

    printf("Camino con menor peso desde %d hasta %d:\n", inicio, destino);
    DFS_MenorPeso(grafop, inicio, destino, visitados, camino, 0, &pesoMin);

    if (pesoMin == INF) {
        printf("No hay camino desde %d hasta %d\n", inicio, destino);
    } else {
        printf("Peso total: %d\n", pesoMin);
    }
}

void DFS_MenorPeso(Grafo* grafop, int nodo, int destino, int visitados[], int camino[], int pesoCam, int* pesoMin) {
    visitados[nodo] = 1;
    camino[nodo] = 1;

    if (nodo == destino) {
        if (pesoCam < *pesoMin) {
            *pesoMin = pesoCam;
            printf("Nuevo camino encontrado con menor peso: ");
            for (int i = 0; i < grafop->cantNodos; i++)
                if (camino[i] == 1)
                    printf("%d ", i);
            printf("\n");
        }
    } else {
        for (int i = 0; i < grafop->cantNodos; i++)
            if (grafop->MatrizAd[nodo][i] != INF && !visitados[i]) {
                int nuevoPesoCamino = pesoCam + grafop->MatrizAd[nodo][i];
                DFS_MenorPeso(grafop, i, destino, visitados, camino, nuevoPesoCamino, pesoMin);
            }
    }

    // Retroceder
    visitados[nodo] = 0;
    camino[nodo] = 0;
}

*/
int main() {
    //por el momento nombrare las ciudades como numeros

    int cantidadNodos = 7;
    Grafo* grafop = crearGrafo(cantidadNodos);
    //añadir aristas al grafo
    insertarArista(grafop , 1 , 2 , 53300 );
    insertarArista(grafop , 1 , 3 , 113000 );
    insertarArista(grafop , 3 , 2 , 112000 );
    insertarArista(grafop , 3 , 4 , 158000 );
    insertarArista(grafop , 4 , 5 , 148000 );
    insertarArista(grafop , 2 , 5 , 67200 );
    insertarArista(grafop , 4 , 6 , 136000 );
    insertarArista(grafop , 5 , 6 , 210000 );
    insertarArista(grafop , 5 , 7 , 194000 );
    insertarArista(grafop , 6 , 7 , 114000 );

    buscarCamino(grafop, 3 , 7 , 400000 );




    /*
    int cantidadNodos = 4;
    Grafo* grafop = crearGrafo(cantidadNodos);
    insertarArista(grafop, 0, 1, 5);
    insertarArista(grafop, 0, 2, 3);
    insertarArista(grafop, 1, 2, 2);
    insertarArista(grafop, 1, 3, 7);
    insertarArista(grafop, 2, 3, 1);
    buscarCamino(grafop, 0, 3, 20);

    */
    return 0;
}
