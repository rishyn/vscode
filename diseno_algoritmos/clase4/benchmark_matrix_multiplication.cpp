// Benchmark para multiplicación de matrices: Strassen y método iterativo
// Implementaciones: vector de vectores y vector plano
#include "strassen_matrix_multiplication.hpp"
#include "strassen_flat_matrix.hpp"
#include <chrono>
#include <iostream>
#include <random>

using namespace divide_and_conquer;
using namespace std;

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

int main(int argc, char* argv[]) {
    size_t n = 256;
    if (argc > 1) n = std::stoi(argv[1]);
    cout << "Benchmark para matrices de tamaño " << n << " x " << n << "\n";

    // Vector de vectores
    strassens_multiplication::Matrix<int> A(n, n), B(n, n);
    fill_matrix_vector(A);
    fill_matrix_vector(B);

    // Vector plano
    strassens_multiplication_flat::FlatMatrix<int> Af(n), Bf(n);
    fill_matrix_flat(Af);
    fill_matrix_flat(Bf);

    // --- Vector de vectores: Strassen ---
    auto start = chrono::high_resolution_clock::now();
    auto C1 = A.strassens_multiplication(B);
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed = end - start;
    cout << "Strassen (vector de vectores): " << elapsed.count() << " s\n";

    // --- Vector de vectores: Iterativo ---
    start = chrono::high_resolution_clock::now();
    auto C2 = A.naive_multiplication(B);
    end = chrono::high_resolution_clock::now();
    elapsed = end - start;
    cout << "Iterativo (vector de vectores): " << elapsed.count() << " s\n";

    // --- Vector plano: Strassen ---
    start = chrono::high_resolution_clock::now();
    auto Cf1 = strassens_multiplication_flat::strassen(Af, Bf);
    end = chrono::high_resolution_clock::now();
    elapsed = end - start;
    cout << "Strassen (vector plano): " << elapsed.count() << " s\n";

    // --- Vector plano: Iterativo ---
    start = chrono::high_resolution_clock::now();
    auto Cf2 = strassens_multiplication_flat::iterative_multiply(Af, Bf);
    end = chrono::high_resolution_clock::now();
    elapsed = end - start;
    cout << "Iterativo (vector plano): " << elapsed.count() << " s\n";

    return 0;
}
