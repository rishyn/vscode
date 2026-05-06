// Algoritmo de Strassen usando un único vector<T> para almacenar la matriz
#include "strassen_flat_matrix.hpp"
#include <cassert>
#include <chrono>
#include <iostream>
#include <vector>


// Prueba
int main(int argc, char* argv[]) {
    size_t n = 4;
    if (argc > 1)
        n = std::stoi(argv[1]);
    divide_and_conquer::strassens_multiplication_flat::FlatMatrix<int> A(n), B(n);
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(-100000, 100000);
    for (size_t i = 0; i < n; ++i)
        for (size_t j = 0; j < n; ++j) {
            A(i, j) = dis(gen);
            B(i, j) = dis(gen);
        }
    auto start = std::chrono::high_resolution_clock::now();
    auto C = divide_and_conquer::strassens_multiplication_flat::strassen(A, B);
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;
    std::cout << "Resultado Strassen:\n";
    std::cout << "Tiempo: " << elapsed.count() << "s\n";

    start = std::chrono::high_resolution_clock::now();
    C = divide_and_conquer::strassens_multiplication_flat::iterative_multiply(A, B);
    end = std::chrono::high_resolution_clock::now();
    elapsed = end - start;
    std::cout << "Resultado Iterativo:\n";
    std::cout << "Tiempo: " << elapsed.count() << "s\n";

    return 0;
}
