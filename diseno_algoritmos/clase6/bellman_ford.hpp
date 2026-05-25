#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <random>
#include <fstream>
using namespace std;


vector<int> bellmanFord(int V, vector<vector<int>>& edges, int src) {
    vector<int> dist(V, std::numeric_limits<int>::max() );
    dist[src] = 0;
    for (int i = 0; i < V; i++) {
        for (vector<int> edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int wt = edge[2];
            if (dist[u] != std::numeric_limits<int>::max()  && dist[u] + wt < dist[v]) {
                if(i == V - 1)
                    return {-1};
                dist[v] = dist[u] + wt;
            }
        }
    }
    return dist;
}