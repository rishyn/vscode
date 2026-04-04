#pragma once
#include <vector>
#include <span>
#include <algorithm>

// Merge Sort using std::vector and std::span for subranges
namespace sorting {
namespace span_merge_sort {
template <typename T>
void merge(std::span<T> left, std::span<T> right, std::span<T> out) {
    size_t i = 0, j = 0, k = 0;
    while (i < left.size() && j < right.size()) {
        if (left[i] <= right[j]) {
            out[k++] = left[i++];
        } else {
            out[k++] = right[j++];
        }
    }
    while (i < left.size()) {
        out[k++] = left[i++];
    }
    while (j < right.size()) {
        out[k++] = right[j++];
    }
}

template <typename T>
void merge_sort(std::span<T> arr) {
    if (arr.size() <= 1) return;
    size_t mid = arr.size() / 2;
    std::vector<T> left(arr.begin(), arr.begin() + mid);
    std::vector<T> right(arr.begin() + mid, arr.end());
    merge_sort(std::span<T>(left));
    merge_sort(std::span<T>(right));
    merge(std::span<T>(left), std::span<T>(right), arr);
}

}  // namespace span_merge_sort
}  // namespace sorting