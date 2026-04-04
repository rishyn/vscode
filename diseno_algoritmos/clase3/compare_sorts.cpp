/**
 * @file compare_sorts.cpp
 * @brief Compare sorting times of merge_sort, insertion_sort, and bubble_sort
 *
 * This program creates a vector of random integers and compares the sorting time
 * of merge_sort, insertion_sort, and bubble_sort algorithms.
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <chrono>
#include "merge_sort.hpp"
#include "insertion_sort.hpp"
#include "bubble_sort.hpp"
#include "quick_sort.hpp"

// Helper to copy std::vector<int> to int array
void vector_to_array(const std::vector<int>& vec, int* arr) {
    for (size_t i = 0; i < vec.size(); ++i) arr[i] = vec[i];
}

int main(int argc, char* argv[]) {
    size_t n;
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <number_of_elements>\n";
        return 1;
    }
    n=std::stoi(argv[1]);
    // Generate random numbers
    std::vector<int> data(n);
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(-100000, 100000);
    for (size_t i = 0; i < n; ++i) data[i] = dis(gen);

    // Prepare copies for each sort
    std::vector<int> vec_bubble = data;
    std::vector<int> vec_insertion = data;
    std::vector<int> vec_merge = data;
    std::vector<int> vec_quick = data;

    // Bubble Sort
    auto start = std::chrono::high_resolution_clock::now();
    sorting::bubble_sort::bubble_sort(vec_bubble);
    auto end = std::chrono::high_resolution_clock::now();
    auto bubble_time = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();

    // Insertion Sort (array version)
    int* arr_insertion = new int[n];
    vector_to_array(vec_insertion, arr_insertion);
    start = std::chrono::high_resolution_clock::now();
    sorting::insertionSort(arr_insertion, n);
    end = std::chrono::high_resolution_clock::now();
    auto insertion_time = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();
    delete[] arr_insertion;

    // Merge Sort (array version)
    int* arr_merge = new int[n];
    vector_to_array(vec_merge, arr_merge);
    start = std::chrono::high_resolution_clock::now();
    sorting::merge_sort(arr_merge, 0, n - 1);
    end = std::chrono::high_resolution_clock::now();
    auto merge_time = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();
    delete[] arr_merge;

    // Quick Sort (vector version)
    start = std::chrono::high_resolution_clock::now();
    sorting::quick_sort::quick_sort(&vec_quick, 0, n - 1);
    end = std::chrono::high_resolution_clock::now();
    auto quick_time = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();

    std::cout << "\nSorting times for " << n << " elements:\n";
    std::cout << "Bubble Sort:    " << bubble_time << " ms\n";
    std::cout << "Insertion Sort: " << insertion_time << " ms\n";
    std::cout << "Merge Sort:     " << merge_time << " ms\n";
    std::cout << "Quick Sort:     " << quick_time << " ms\n";
    return 0;
}
