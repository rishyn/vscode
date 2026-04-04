#include <benchmark/benchmark.h>
#include "linear_search.hpp"
#include "binary_search.hpp"
#include <vector>
#include <numeric>

static void BM_LinearSearchModern(benchmark::State& state) {
    int size = state.range(0);
    std::vector<int> data(size);
    std::iota(data.begin(), data.end(), 0);
    int key = size - 1; // Worst case: search for the last element

    for (auto _ : state) {
        auto result = modern_cpp::linear_search(data, key);
        benchmark::DoNotOptimize(result);
    }
    state.SetComplexityN(state.range(0));
}
BENCHMARK(BM_LinearSearchModern)->Range(8, 1 << 15)->Complexity(benchmark::oN);

static void BM_LinearSearchOld(benchmark::State& state) {
    int size = state.range(0);
    std::vector<int> data(size);
    std::iota(data.begin(), data.end(), 0);
    int key = size - 1; // Worst case: search for the last element
    
    for (auto _ : state) {
        auto result = legacy_cpp::linear_search(data.data(), static_cast<int>(data.size()), key);
        benchmark::DoNotOptimize(result);
    }
    state.SetComplexityN(state.range(0));
}
BENCHMARK(BM_LinearSearchOld)->Range(8, 1 << 15)->Complexity(benchmark::oN);

static void BM_BinarySearchModern(benchmark::State& state) {
    int size = state.range(0);
    std::vector<int> data(size);
    std::iota(data.begin(), data.end(), 0);
    int key = size - 1;
    
    for (auto _ : state) {
        auto result = modern_cpp::binary_search(data, key);
        benchmark::DoNotOptimize(result);
    }
    state.SetComplexityN(state.range(0));
}
BENCHMARK(BM_BinarySearchModern)->Range(8, 1 << 15)->Complexity(benchmark::oLogN);

static void BM_BinarySearchOld(benchmark::State& state) {
    int size = state.range(0);
    std::vector<int> data(size);
    std::iota(data.begin(), data.end(), 0);
    int key = size - 1;
    
    for (auto _ : state) {
        auto result = legacy_cpp::binary_search(data.data(), static_cast<int>(data.size()), key);
        benchmark::DoNotOptimize(result);
    }
    state.SetComplexityN(state.range(0));
}
BENCHMARK(BM_BinarySearchOld)->Range(8, 1 << 15)->Complexity(benchmark::oLogN);

BENCHMARK_MAIN();
