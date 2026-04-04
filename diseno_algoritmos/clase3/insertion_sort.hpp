/**
 * @file insertion_sort.hpp
 * @brief Insertion Sort algorithm header
 */
#pragma once
#include <vector>
#include <cstdint>

namespace sorting {
// Insertion sort for C-style arrays
inline void insertionSort(int *arr, int n) {
    for (int i = 1; i < n; i++) {
        int temp = arr[i];
        int j = i - 1;
        while (j >= 0 && temp < arr[j]) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = temp;
    }
}
// Insertion sort for std::vector
inline void insertionSort(std::vector<int> *arr) {
    size_t n = arr->size();
    for (size_t i = 1; i < n; i++) {
        int temp = (*arr)[i];
        int32_t j = i - 1;
        while (j >= 0 && temp < (*arr)[j]) {
            (*arr)[j + 1] = (*arr)[j];
            j--;
        }
        (*arr)[j + 1] = temp;
    }
}
} // namespace sorting
