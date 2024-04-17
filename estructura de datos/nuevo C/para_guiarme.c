#include <stdio.h>
#include <limits.h>

#define V 7 // Número de nodos en el grafo

// Función para encontrar el nodo con el costo mínimo
int encontrarMinimo(int costos[], int visitado[]) {
    int min = INT_MAX, min_index;

    for (int i = 0; i < V; i++) {
        if (visitado[i] == 0 && costos[i] < min) {
            min = costos[i];
            min_index = i;
        }
    }

    return min_index;
}

// Función para imprimir el recorrido y el costo total
void imprimirRecorrido(int padre[], int grafo[V][V]) {
    printf("Camino\tCosto\n");
    for (int i = 1; i < V; i++) {
        printf("%d -> %d\t%d\n", padre[i], i, grafo[i][padre[i]]);
    }
}

// Función para realizar el análisis del camino mínimo
void caminoMinimo(int grafo[V][V]) {
    int padre[V];
    int costos[V];
    int visitado[V];

    // Inicializar costos e indicadores de visitado
    for (int i = 0; i < V; i++) {
        costos[i] = INT_MAX;
        visitado[i] = 0;
    }

    // Iniciar desde el primer nodo
    costos[0] = 0;
    padre[0] = -1;

    for (int count = 0; count < V - 1; count++) {
        int u = encontrarMinimo(costos, visitado);
        visitado[u] = 1;

        for (int v = 0; v < V; v++) {
            if (!visitado[v] && grafo[u][v] && grafo[u][v] < costos[v]) {
                padre[v] = u;
                costos[v] = grafo[u][v];
            }
        }
    }

    imprimirRecorrido(padre, grafo);
}

int main() {
    // Ejemplo de un grafo ponderado (costos entre nodos)
    int grafo[V][V] = {
        {0, 1, 2, 0, 0, 0, 0},
        {1, 0, 0, 4, 0, 0, 0},
        {2, 0, 0, 3, 0, 0, 0},
        {0, 4, 3, 0, 5, 6, 0},
        {0, 0, 0, 5, 0, 0, 2},
        {0, 0, 0, 6, 0, 0, 1},
        {0, 0, 0, 0, 2, 1, 0}
    };

    caminoMinimo(grafo);

    return 0;
}