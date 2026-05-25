#include <iostream>
#include <vector>
#include <queue>
#include <random>
#include <fstream>
using namespace std;

#include "graph.hpp"

int main() {
    int V, E;
    cout << "Numero de nodos: ";
    cin >> V;
    cout << "Numero de aristas: ";
    cin >> E;

    vector<vector<int>> edges;
    vector<vector<pair<int,int>>> adj;
    generarGrafo(V, E, edges, adj);
    mostrarGrafoGraphviz(V, adj);
    int src;
    cout << "Nodo fuente (0 a " << V-1 << "): ";
    cin >> src;

    cout << "\nBellman-Ford:\n";
    vector<int> dist_bf = bellmanFord(V, edges, src);
    if (dist_bf.size() == 1 && dist_bf[0] == -1) {
        cout << "Ciclo negativo detectado.\n";
    } else {
        for (int d : dist_bf) cout << d << " ";
        cout << endl;
    }

    cout << "\nDijkstra:\n";
    vector<int> dist_dj = dijkstra(V, adj, src);
    for (int d : dist_dj) cout << d << " ";
    cout << endl;

    return 0;
}