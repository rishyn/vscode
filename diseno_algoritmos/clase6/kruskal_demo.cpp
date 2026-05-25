#include "kruskal.hpp"
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
    int V = 6, E = 10;
    vector<vector<int>> edges;
    std::vector<std::vector<std::pair<int,int>>> adj;
    generarGrafo(V, E, edges);


    // Llamar a la función kruskalMST
    auto [mst, totalWeight] = kruskalMST_heap(V, edges);
    adj = edgeListToAdjList(edges, V);
    cout << "Aristas del MST (u, v, w):\n";
    for (auto& e : mst) cout << e.u << " - " << e.v << " : " << e.w << '\n';
    cout << "Peso total del MST: " << totalWeight << endl;
    mostrarGrafoGraphviz(V, adj, "kruskal_graph.dot");
    return 0;
}
