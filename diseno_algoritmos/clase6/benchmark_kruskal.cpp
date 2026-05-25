#include "kruskal.hpp"
#include <benchmark/benchmark.h>
#include <vector>
#include <algorithm>
#include <random>
using namespace std;



static void BM_KruskalSort(benchmark::State& state) {
    int V = state.range(0);
    int E = state.range(1);
    vector<vector<int>> edges;
    vector<vector<pair<int,int>>> adj;
    generarGrafo(V, E, edges);
    for (auto _ : state) {
        auto res = kruskalMST_sort(V, edges);
        benchmark::DoNotOptimize(res);
    }
    state.SetComplexityN(state.range(0));
}

static void BM_KruskalHeap(benchmark::State& state) {
    int V = state.range(0);
    int E = state.range(1);
    vector<vector<int>> edges;
    vector<vector<pair<int,int>>> adj;
    generarGrafo(V, E, edges);
    for (auto _ : state) {
        auto res = kruskalMST_heap(V, edges);
        benchmark::DoNotOptimize(res);
    }
    state.SetComplexityN(state.range(0));
}

// Rango de tamaños de grafos

// Complejidad teórica aproximada: O(E log E) para ambos métodos
BENCHMARK(BM_KruskalSort)
    ->Args({100, 500})
    ->Args({200, 1000})
    ->Args({500, 3000})
    ->Args({1000, 6000})
    ->Complexity(benchmark::oNLogN);
BENCHMARK(BM_KruskalHeap)
    ->Args({100, 500})
    ->Args({200, 1000})
    ->Args({500, 3000})
    ->Args({1000, 6000})
    ->Complexity(benchmark::oNLogN);

BENCHMARK_MAIN();
