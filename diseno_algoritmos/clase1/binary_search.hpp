#ifndef BINARY_SEARCH_HPP
#define BINARY_SEARCH_HPP

#include <optional>
#include <cstddef>

namespace modern_cpp {

/**
 * @brief Performs a binary search on a sorted container.
 * 
 * @tparam Container The type of the container (must support size() and operator[]).
 * @tparam T The type of the value to search for.
 * @param container The container to search through (must be sorted).
 * @param key The value to search for.
 * @return std::optional<std::size_t> The index of the key, 
 *         or std::nullopt if not found.
 */
template <typename Container, typename T>
constexpr std::optional<std::size_t> binary_search(const Container& container, const T& key) {
    // TODO: Implement binary search algorithm
    return std::nullopt;
}

} // namespace modern_cpp

namespace legacy_cpp {
/**
 * @brief Legacy binary search implementation.
 */
int binary_search(int *array, int size, int key) {
    int low = 0;
    int high = size - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (array[mid] == key) {
            return mid;
        } else if (array[mid] < key) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}
} // namespace legacy_cpp
#endif // BINARY_SEARCH_HPP
