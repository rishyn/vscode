#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <random>
#include <fstream>
using namespace std;


// Algoritmo de Floyd-Warshall para encontrar todas las distancias más cortas entre pares de nodos
std::vector<std::vector<int>> floydWarshall(int V, const std::vector<std::vector<int>>& adjMatrix) {
    const int INF = std::numeric_limits<int>::max() / 2; // Para evitar overflow
    std::vector<std::vector<int>> dist = adjMatrix;

    // Inicializar: si no hay arista, poner INF (excepto en la diagonal)
    for (int i = 0; i < V; ++i) {
        for (int j = 0; j < V; ++j) {
            if (i != j && dist[i][j] == 0)
                dist[i][j] = INF;
        }
    }

    // Floyd-Warshall
    for (int k = 0; k < V; ++k) {
        for (int i = 0; i < V; ++i) {
            for (int j = 0; j < V; ++j) {
                if (dist[i][k] < INF && dist[k][j] < INF)
                    dist[i][j] = std::min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }
    return dist;
}