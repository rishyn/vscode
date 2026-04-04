#ifndef LINEAR_SEARCH_HPP
#define LINEAR_SEARCH_HPP

#include <optional>
#include <cstddef>

namespace modern_cpp {

/**
 * @brief Performs a linear search on a container.
 * 
 * @tparam Container The type of the container (must support range-based for loops).
 * @tparam T The type of the value to search for.
 * @param container The container to search through.
 * @param key The value to search for.
 * @return std::optional<std::size_t> The index of the first occurrence of the key, 
 *         or std::nullopt if not found.
 */
template <typename Container, typename T>
constexpr std::optional<std::size_t> linear_search(const Container& container, const T& key) {
    std::size_t index = 0;
    for (const auto& element : container) {
        if (element == key) {
            return index;
        }
        ++index;
    }
    return std::nullopt;
}

} // namespace modern_cpp

namespace legacy_cpp {
/**
 * @brief Legacy linear search implementation.
 */
int linear_search(int *array, int size, int key) {
    for (int i = 0; i < size; ++i) {
        if (array[i] == key) {
            return i;
        }
    }
    return -1;
}
}
#endif // LINEAR_SEARCH_HPP
