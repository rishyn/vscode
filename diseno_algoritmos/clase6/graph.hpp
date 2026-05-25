#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <random>
#include <fstream>
using namespace std;

// Convierte una lista de adyacencia a lista de aristas
std::vector<std::vector<int>> adjListToEdgeList(const std::vector<std::vector<std::pair<int,int>>>& adj) {
    std::vector<std::vector<int>> edges;
    int V = adj.size();
    for (int u = 0; u < V; ++u) {
        for (const auto& [v, w] : adj[u]) {
            edges.push_back({u, v, w});
        }
    }
    return edges;
}

// Convierte una lista de adyacencia a matriz de adyacencia
std::vector<std::vector<int>> adjListToMatrix(int V, const std::vector<std::vector<std::pair<int,int>>>& adj) {
    const int INF = std::numeric_limits<int>::max() / 2; // Para evitar overflow
    std::vector<std::vector<int>> matrix(V, std::vector<int>(V, INF));
    for (int i = 0; i < V; ++i) {
        matrix[i][i] = 0; // Distancia a sí mismo es 0
        for (const auto& [j, w] : adj[i]) {
            matrix[i][j] = w;
        }
    }
    return matrix;
}

std::vector<std::vector<std::pair<int,int>>> edgeListToAdjList(const std::vector<std::vector<int>>& edges, int V) {
    std::vector<std::vector<std::pair<int,int>>> adj(V);
    for (const auto& edge : edges) {
        int u = edge[0], v = edge[1], w = edge[2];
        adj[u].push_back({v, w});
    }
    return adj;
}

// Busca si el vértice v está en la lista de adyacencia de u
bool is_adjacent(int u, int v, const std::vector<std::vector<std::pair<int,int>>>& adj) {
    for (const auto& neighbor : adj[u]) {
        if (neighbor.first == v) return true;
    }
    return false;
}

// Genera un grafo aleatorio dirigido y ponderado
void generarGrafo(int V, int E, vector<vector<int>>& edges) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> node_dist(0, V-1);
    std::uniform_int_distribution<> weight_dist(1, 100);
    edges.clear();
    for (int i = 1; i < V; ++i) {
        int w = weight_dist(gen);
        edges.push_back({i-1, i, w});
    }
    for (int i = V-1; i < E; ++i) {
        int u = node_dist(gen);
        int v = node_dist(gen);
        int w = weight_dist(gen);
        while (v == u) v = node_dist(gen);
        edges.push_back({u, v, w});
    }
}

void mostrarGrafoGraphviz(int V, const vector<vector<pair<int,int>>>& adj, const std::string& filename = "graph.dot") {
    std::ofstream fout(filename);
    fout << "digraph G {\n";
    for (int u = 0; u < V; ++u) {
        for (auto [v, w] : adj[u]) {
            fout << "    " << u << " -> " << v << " [label=\"" << w << "\"];\n";
        }
    }
    fout << "}\n";
    fout.close();
    std::cout << "Archivo Graphviz generado: " << filename << std::endl;
}
