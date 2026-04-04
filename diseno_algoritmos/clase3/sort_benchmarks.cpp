#include <benchmark/benchmark.h>
#include <vector>
#include <random>
#include <span>
#include "merge_sort.hpp"
#include "merge_sort_span.hpp"
#include "insertion_sort.hpp"
#include "bubble_sort.hpp"
#include "quick_sort.hpp"



// Helper to generate random vector
std::vector<int> generate_random_vector(size_t n) {
    std::vector<int> data(n);
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(-100000, 100000);
    for (size_t i = 0; i < n; ++i) data[i] = dis(gen);
    return data;
}



// Bubble Sort Benchmark
static void BM_BubbleSort(benchmark::State& state) {
    for (auto _ : state) {
        auto data = generate_random_vector(state.range(0));
        benchmark::DoNotOptimize(sorting::bubble_sort::bubble_sort(data));
    }
    state.SetComplexityN(state.range(0));
}
BENCHMARK(BM_BubbleSort)->RangeMultiplier(2)->Range(256, 8192)->Complexity(benchmark::oNSquared);

// Insertion Sort Benchmark
static void BM_InsertionSort(benchmark::State& state) {
    for (auto _ : state) {
        auto data = generate_random_vector(state.range(0));
        int* arr = new int[data.size()];
        for (size_t i = 0; i < data.size(); ++i) arr[i] = data[i];
        sorting::insertionSort(arr, data.size());
        benchmark::DoNotOptimize(arr);
        delete[] arr;
    }
    state.SetComplexityN(state.range(0));
}
BENCHMARK(BM_InsertionSort)->RangeMultiplier(2)->Range(256, 8192)->Complexity(benchmark::oNSquared);

// Merge Sort Benchmark

static void BM_MergeSort(benchmark::State& state) {
    for (auto _ : state) {
        auto data = generate_random_vector(state.range(0));
        int* arr = new int[data.size()];
        for (size_t i = 0; i < data.size(); ++i) arr[i] = data[i];
        sorting::merge_sort(arr, 0, data.size() - 1);
        benchmark::DoNotOptimize(arr);
        delete[] arr;
    }
    state.SetComplexityN(state.range(0));
}
BENCHMARK(BM_MergeSort)->RangeMultiplier(2)->Range(256, 8192)->Complexity(benchmark::oNLogN);


// Merge Sort (std::span) Benchmark
static void BM_MergeSort_Span(benchmark::State& state) {
    for (auto _ : state) {
        auto data = generate_random_vector(state.range(0));
        sorting::span_merge_sort::merge_sort(std::span<int>(data));
        benchmark::DoNotOptimize(data);
    }
    state.SetComplexityN(state.range(0));
}
BENCHMARK(BM_MergeSort_Span)->RangeMultiplier(2)->Range(256, 8192)->Complexity(benchmark::oNLogN);


// Quick Sort Benchmark
static void BM_QuickSort(benchmark::State& state) {
    for (auto _ : state) {
        auto data = generate_random_vector(state.range(0));
        sorting::quick_sort::quick_sort(&data, 0, data.size() - 1);
        benchmark::DoNotOptimize(data);
    }
    state.SetComplexityN(state.range(0));
}
BENCHMARK(BM_QuickSort)->RangeMultiplier(2)->Range(256, 8192)->Complexity(benchmark::oNLogN);

BENCHMARK_MAIN();

