/**
 * @file bubble_sort.hpp
 * @brief Bubble Sort algorithm header
 */
#pragma once
#include <vector>
#include <utility>

namespace sorting {
namespace bubble_sort {
// Bubble sort for std::vector
inline std::vector<int> bubble_sort(std::vector<int>& array) {
    bool swap_check = true;
    int size = array.size();
    for (int i = 0; (i < size) && (swap_check); i++) {
        swap_check = false;
        for (int j = 0; j < size - 1 - i; j++) {
            if (array[j] > array[j + 1]) {
                swap_check = true;
                std::swap(array[j], array[j + 1]);
            }
        }
    }
    return array;
}
} // namespace bubble_sort
} // namespace sorting
