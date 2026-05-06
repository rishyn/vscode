#include "strassen_matrix_multiplication.hpp"
#include "strassen_flat_matrix.hpp"
#include <benchmark/benchmark.h>
#include <random>

using namespace divide_and_conquer;

// Utilidades para rellenar matrices

template <typename T>
void fill_matrix_vector(strassens_multiplication::Matrix<T>& M) {
    auto sz = M.size();
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(-1000, 1000);
    for (size_t i = 0; i < sz.first; ++i)
        for (size_t j = 0; j < sz.second; ++j)
            M[i][j] = dis(gen);
}

template <typename T>
void fill_matrix_flat(strassens_multiplication_flat::FlatMatrix<T>& M) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(-1000, 1000);
    for (size_t i = 0; i < M.n; ++i)
        for (size_t j = 0; j < M.n; ++j)
            M(i, j) = dis(gen);
}

// Benchmarks para cada implementación

static void BM_Strassen_Vector(benchmark::State& state) {
    size_t n = state.range(0);
    strassens_multiplication::Matrix<int> A(n, n), B(n, n);
    fill_matrix_vector(A);
    fill_matrix_vector(B);
    for (auto _ : state) {
        auto C = A * B;
        benchmark::DoNotOptimize(C);
    }
    state.SetComplexityN(state.range(0));
}
BENCHMARK(BM_Strassen_Vector)
    ->Arg(512)->Arg(1024)->Arg(2048)
    ->Complexity(benchmark::oNCubed); // O(n^3) teórico, Strassen es O(n^2.81)

static void BM_Iterative_Vector(benchmark::State& state) {
    size_t n = state.range(0);
    strassens_multiplication::Matrix<int> A(n, n), B(n, n);
    fill_matrix_vector(A);
    fill_matrix_vector(B);
    for (auto _ : state) {
        auto C = A.naive_multiplication(B);
        benchmark::DoNotOptimize(C);
    }
    state.SetComplexityN(state.range(0));
}
BENCHMARK(BM_Iterative_Vector)
    ->Arg(512)->Arg(1024)->Arg(2048)
    ->Complexity(benchmark::oNCubed); // O(n^2) para acceso, pero O(n^3) para multiplicación

static void BM_Strassen_Flat(benchmark::State& state) {
    size_t n = state.range(0);
    strassens_multiplication_flat::FlatMatrix<int> A(n), B(n);
    fill_matrix_flat(A);
    fill_matrix_flat(B);
    for (auto _ : state) {
        auto C = strassens_multiplication_flat::strassen(A, B);
        benchmark::DoNotOptimize(C);
    }
    state.SetComplexityN(state.range(0));
}
BENCHMARK(BM_Strassen_Flat)
    ->Arg(512)->Arg(1024)->Arg(2048)
    ->Complexity(benchmark::oNCubed); // O(n^3) teórico, Strassen es O(n^2.81)

static void BM_Iterative_Flat(benchmark::State& state) {
    size_t n = state.range(0);
    strassens_multiplication_flat::FlatMatrix<int> A(n), B(n);
    fill_matrix_flat(A);
    fill_matrix_flat(B);
    for (auto _ : state) {
        auto C = strassens_multiplication_flat::iterative_multiply(A, B);
        benchmark::DoNotOptimize(C);
    }
    state.SetComplexityN(state.range(0));
}
BENCHMARK(BM_Iterative_Flat)
    ->Arg(512)->Arg(1024)->Arg(2048)
    ->Complexity(benchmark::oNCubed); // O(n^2) para acceso, pero O(n^3) para multiplicación

BENCHMARK_MAIN();
