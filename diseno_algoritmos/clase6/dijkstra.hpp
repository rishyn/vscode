#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <random>
#include <fstream>
using namespace std;


// Dijkstra usando lista de adyacencia
vector<int> dijkstra(int V, vector<vector<pair<int,int>>>& adj, int src) {
    vector<int> dist(V, std::numeric_limits<int>::max() );
    vector<bool> visited(V, false );
    dist[src] = 0;
    //visited[src] = true;
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    pq.push({0, src});
    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        if (visited[u]) continue; // No volver a visitar nodos ya marcados
        visited[u] = true;
        for (auto [v, wt] : adj[u]) {
            if (!visited[v] && dist[u] + wt < dist[v]) {
                dist[v] = dist[u] + wt;
                pq.push({dist[v], v});
            }
        }
    }
    return dist;
}