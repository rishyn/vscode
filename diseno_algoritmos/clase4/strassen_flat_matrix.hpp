// Algoritmo de Strassen usando un único vector<T> para almacenar la matriz
#include <cassert>
#include <iostream>
#include <vector>
#include <random>

namespace divide_and_conquer {
    namespace strassens_multiplication_flat {
// Acceso a elemento (i, j) en matriz almacenada como vector plano
#define IDX(i, j, n) ((i) * (n) + (j))

template <typename T>
class FlatMatrix {
 public:
    size_t n;
    std::vector<T> data;

    FlatMatrix(size_t n_) : n(n_), data(n_ * n_, 0) {}

    T& operator()(size_t i, size_t j) { return data[IDX(i, j, n)]; }
    const T& operator()(size_t i, size_t j) const { return data[IDX(i, j, n)]; }
};

// Suma de matrices
template <typename T>
FlatMatrix<T> add(const FlatMatrix<T>& A, const FlatMatrix<T>& B) {
    assert(A.n == B.n);
    FlatMatrix<T> C(A.n);
    for (size_t i = 0; i < A.n * A.n; ++i) {
        C.data[i] = A.data[i] + B.data[i];
    }
    return C;
}

// Resta de matrices
template <typename T>
FlatMatrix<T> sub(const FlatMatrix<T>& A, const FlatMatrix<T>& B) {
    assert(A.n == B.n);
    FlatMatrix<T> C(A.n);
    for (size_t i = 0; i < A.n * A.n; ++i) {
        C.data[i] = A.data[i] - B.data[i];
    }
    return C;
}

// Multiplicación de matrices por Strassen
// Solo para n potencia de 2
// No optimizado para n impar
// Para n pequeño usa multiplicación normal

// Multiplicación iterativa de matrices planas
template <typename T>
FlatMatrix<T> iterative_multiply(const FlatMatrix<T>& A,
                                 const FlatMatrix<T>& B) {
    assert(A.n == B.n);
    size_t n = A.n;
    FlatMatrix<T> C(n);
        for (size_t i = 0; i < n; ++i) {
            for (size_t k = 0; k < n; ++k) {
                for (size_t j = 0; j < n; ++j) {
                    C(i, j) += A(i, k) * B(k, j);
                }
            }
        }
    return C;
}

template <typename T>
FlatMatrix<T> strassen(const FlatMatrix<T>& A, const FlatMatrix<T>& B) {
    assert(A.n == B.n);
    size_t n = A.n;
    if (n <= 64) {
        return iterative_multiply(A, B);
    }
    size_t k = n / 2;
    // Submatrices
    FlatMatrix<T> A11(k), A12(k), A21(k), A22(k);
    FlatMatrix<T> B11(k), B12(k), B21(k), B22(k);
    for (size_t i = 0; i < k; ++i) {
        for (size_t j = 0; j < k; ++j) {
            A11(i, j) = A(i, j);
            A12(i, j) = A(i, j + k);
            A21(i, j) = A(i + k, j);
            A22(i, j) = A(i + k, j + k);
            B11(i, j) = B(i, j);
            B12(i, j) = B(i, j + k);
            B21(i, j) = B(i + k, j);
            B22(i, j) = B(i + k, j + k);
        }
    }
    // Strassen
    auto M1 = strassen(add(A11, A22), add(B11, B22));
    auto M2 = strassen(add(A21, A22), B11);
    auto M3 = strassen(A11, sub(B12, B22));
    auto M4 = strassen(A22, sub(B21, B11));
    auto M5 = strassen(add(A11, A12), B22);
    auto M6 = strassen(sub(A21, A11), add(B11, B12));
    auto M7 = strassen(sub(A12, A22), add(B21, B22));
    // Combinar resultados
    FlatMatrix<T> C(n);
    for (size_t i = 0; i < k; ++i) {
        for (size_t j = 0; j < k; ++j) {
            C(i, j) = M1(i, j) + M4(i, j) - M5(i, j) + M7(i, j);
            C(i, j + k) = M3(i, j) + M5(i, j);
            C(i + k, j) = M2(i, j) + M4(i, j);
            C(i + k, j + k) = M1(i, j) - M2(i, j) + M3(i, j) + M6(i, j);
        }
    }
    return C;
}
}}  // namespace divide_and_conquer