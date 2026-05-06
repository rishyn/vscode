/**
 * @brief [Strassen's
 * algorithm](https://en.wikipedia.org/wiki/Strassen_algorithm) is one of the
 * methods for multiplying two matrices. It is one of the faster algorithms for
 * larger matrices than naive multiplication method.
 *
 * It involves dividing each matrices into 4 blocks, given they are evenly
 * divisible, and are combined with new defined matrices involving 7 matrix
 * multiplications instead of eight, yielding O(n^2.8073) complexity.
 *
 * @author [AshishYUO](https://github.com/AshishYUO)
 */
#include "strassen_matrix_multiplication.hpp"
#include <cassert>   /// For assert operation
#include <chrono>    /// For std::chrono; time measurement
#include <iostream>  /// For I/O operations
#include <tuple>     /// For std::tuple
#include <vector>    /// For creating dynamic arrays

/**
 * @brief Self-test implementations
 * @returns void
 */
static void test(const size_t s = 512) {
    // const size_t s = 32;
    auto matrix_demo =
        divide_and_conquer::strassens_multiplication::Matrix<size_t>(s, s);

    for (size_t i = 0; i < s; ++i) {
        for (size_t j = 0; j < s; ++j) {
            matrix_demo[i][j] = i + j;
        }
    }

    auto matrix_demo2 =
        divide_and_conquer::strassens_multiplication::Matrix<size_t>(s, s);
    for (size_t i = 0; i < s; ++i) {
        for (size_t j = 0; j < s; ++j) {
            matrix_demo2[i][j] = 2 + i + j;
        }
    }

    auto start = std::chrono::system_clock::now();
    auto Mat3 = matrix_demo2 * matrix_demo;
    auto end = std::chrono::system_clock::now();

    std::chrono::duration<double> time = (end - start);
    std::cout << "Strassen time: " << time.count() << "s" << std::endl;

    start = std::chrono::system_clock::now();
    auto conf = matrix_demo2.naive_multiplication(matrix_demo);
    end = std::chrono::system_clock::now();

    time = end - start;
    std::cout << "Normal time: " << time.count() << "s" << std::endl;

    // std::cout << Mat3 << conf << std::endl;
    assert(Mat3 == conf);
}

/**
 * @brief main function
 * @returns 0 on exit
 */
int main(int argc, char* argv[]) {
    size_t arg_size = 32;  // valor por defecto
    if (argc > 1) {
        try {
            int input = std::stoi(argv[1]);
            if (input > 0) {
                arg_size = static_cast<size_t>(input);
            } else {
                std::cerr << "El tamaño debe ser un entero positivo. Usando "
                             "valor por defecto (32)."
                          << std::endl;
            }
        } catch (const std::exception& e) {
            std::cerr << "Argumento inválido: " << argv[1]
                      << ". Usando valor por defecto (32)." << std::endl;
        }
    }
    std::cout << "Running Strassen's Matrix Multiplication for size "
              << arg_size << " x " << arg_size << "...\n";
    test(arg_size);  // run self-test implementation
    return 0;
}
