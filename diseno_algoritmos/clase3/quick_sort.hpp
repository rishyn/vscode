/**
 * @file
 * @brief [Quick sort implementation](https://en.wikipedia.org/wiki/Quicksort)
 * in C++
 * @details
 *      Quick Sort is a [divide and conquer
 * algorithm](https://en.wikipedia.org/wiki/Category:Divide-and-conquer_algorithms).
 *      It picks an element as pivot and partition the given array around the
 * picked pivot. There are many different versions of quickSort that pick pivot
 * in different ways.
 *
 *      1. Always pick the first element as pivot
 *      2. Always pick the last element as pivot (implemented below)
 *      3. Pick a random element as pivot
 *      4. Pick median as pivot
 *
 *      The key process in quickSort is partition(). Target of partition is,
 *      given an array and an element x(say) of array as pivot, put x at it's
 *      correct position in sorted array and put all smaller elements (samller
 *      than x) before x, and put all greater elements (greater than x) after
 *      x. All this should be done in linear time
 *
 * @author [David Leal](https://github.com/Panquesito7)
 * @author [popoapp](https://github.com/popoapp)
 */

#include <algorithm>  /// for std::is_sorted
#include <cassert>    /// for std::assert
#include <cstdint>
#include <ctime>      /// for std::time
#include <iostream>   /// for IO operations
#include <vector>     /// for std::vector

/**
 * @brief Sorting algorithms
 * @namespace sorting
 */
namespace sorting {
/**
 * @namespace quick_sort
 * @brief Functions for the [Quick sort
 * implementation](https://en.wikipedia.org/wiki/Quicksort) in C++
 */
namespace quick_sort {
/**
 * @brief Sorts the array taking the last element as pivot
 * @details
 * This function takes last element as pivot, places
 * the pivot element at its correct position in sorted
 * array, and places all smaller (smaller than pivot)
 * to left of pivot and all greater elements to right of pivot
 * @tparam T array type
 * @param arr the array with contents given by the user
 * @param low first point of the array (starting index)
 * @param high last point of the array (ending index)
 * @returns index of the smaller element
 *  
 *  ### Time Complexity
 *  best case, average Case: O(nlog(n))
 *  Worst Case: O(n^2)  (Worst case occur when the partition 
 *  is consistently unbalanced.)
 
 *  ### Space Complexity
 *  average Case: O(log(n))
 *  Worst Case: O(n)  
 *  It's space complexity is due to the recursive function calls and partitioning process. 
 */ 

template <typename T>
int partition(std::vector<T> *arr, const int &low, const int &high) {
    T pivot = (*arr)[high];  // taking the last element as pivot
    int i = (low - 1);       // Index of smaller element

    for (int j = low; j < high; j++) {
        // If current element is smaller than or
        // equal to pivot
        if ((*arr)[j] <= pivot) {
            i++;  // increment index of smaller element
            std::swap((*arr)[i], (*arr)[j]);
        }
    }

    std::swap((*arr)[i + 1], (*arr)[high]);
    return (i + 1);
}

/**
 * @brief the main function that implements Quick Sort.
 *
 * Void function used in T (array type) function, which then
 * can be used as self-tests or other functionalities.
 * @tparam T array type
 * @param arr array to be sorted
 * @param low starting index
 * @param high ending index
 */
template <typename T>
void quick_sort(std::vector<T> *arr, const int &low, const int &high) {
    if (low < high) {
        int p = partition(arr, low, high);

        quick_sort(arr, low, p - 1);
        quick_sort(arr, p + 1, high);
    }
}

/**
 * @brief the main function that implements Quick Sort.
 *
 * T (array type) function which calls the void function. Can
 * be used for self-tests and other functionalities.
 * @tparam T array type
 * @param arr array to be sorted
 * @param low starting index
 * @param high ending index
 */
template <typename T>
std::vector<T> quick_sort(std::vector<T> arr, const int &low, const int &high) {
    if (low < high) {
        int p = partition(&arr, low, high);

        quick_sort(&arr, low, p - 1);
        quick_sort(&arr, p + 1, high);
    }
    return arr;
}

/**
 * @brief Utility function to print the array contents
 * @param arr the array to be printed
 * @param size size of the given array
 * @returns void
 */
template <typename T>
void show(const std::vector<T> &arr, const int &size) {
    for (int i = 0; i < size; i++) std::cout << arr[i] << " ";
    std::cout << "\n";
}

}  // namespace quick_sort
}  // namespace sorting