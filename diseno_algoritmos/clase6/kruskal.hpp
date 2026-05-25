
#include "graph.hpp"
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Estructura para representar una arista
struct Edge {
    int u, v, w;
    bool operator<(const Edge& other) const { return w < other.w; }
};


// Estructura para Union-Find (Disjoint Set Union)
struct DSU {
    vector<int> parent, rank;
    DSU(int n) : parent(n), rank(n, 0) {
        for (int i = 0; i < n; ++i) parent[i] = i;
    }
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    bool unite(int x, int y) {
        int xr = find(x), yr = find(y);
        if (xr == yr) return false;
        if (rank[xr] < rank[yr]) parent[xr] = yr;
        else if (rank[xr] > rank[yr]) parent[yr] = xr;
        else { parent[yr] = xr; rank[xr]++; }
        return true;
    }
};

// Función que implementa Kruskal usando heap
pair<vector<Edge>, int> kruskalMST_heap(int V, vector<vector<int>>& edges) {
      // Convertir a vector de Edge
    vector<Edge> edgeList;
    for (auto& e : edges) {
        if (e.size() == 3)
            edgeList.push_back({e[0], e[1], e[2]});
    }
    auto cmp = [](const Edge& a, const Edge& b) { return a.w > b.w; };
    make_heap(edgeList.begin(), edgeList.end(), cmp);
    DSU dsu(V);
    vector<Edge> mst;
    int totalWeight = 0;
    while (!edgeList.empty() && mst.size() < V-1) {
        pop_heap(edgeList.begin(), edgeList.end(), cmp);
        Edge e = edgeList.back();
        edgeList.pop_back();
        if (dsu.unite(e.u, e.v)) {
            mst.push_back(e);
            totalWeight += e.w;
        }
    }
    return {mst, totalWeight};
}

// Kruskal usando sort
pair<vector<Edge>, int> kruskalMST_sort(int V, vector<vector<int>>& edges) {
    vector<Edge> edgeList;
    for (auto& e : edges) {
        if (e.size() == 3)
            edgeList.push_back({e[0], e[1], e[2]});
    }
    sort(edgeList.begin(), edgeList.end());
    DSU dsu(V);
    vector<Edge> mst;
    int totalWeight = 0;
    for (auto& e : edgeList) {
        if (dsu.unite(e.u, e.v)) {
            mst.push_back(e);
            totalWeight += e.w;
        }
        if (mst.size() == V-1) break;
    }
    return {mst, totalWeight};
}