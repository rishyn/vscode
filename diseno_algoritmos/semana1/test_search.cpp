#include "linear_search.hpp"
#include "binary_search.hpp"
#include <iostream>
#include <vector>
#include <array>
#include <string>
#include <cassert>

void test_vector() {
    std::vector<int> v = {10, 20, 30, 40, 50};
        
    auto result = modern_cpp::linear_search(v, 60);
    assert(!result.has_value());
    
    std::cout << "Vector tests passed!" << std::endl;
}

void test_array() {
    std::array<std::string, 3> arr = {"apple", "banana", "cherry"};
    
    auto result = modern_cpp::linear_search(arr, "banana");
    assert(result.has_value() && *result == 1);
    
    result = modern_cpp::linear_search(arr, "date");
    assert(!result.has_value());
    
    std::cout << "Array tests passed!" << std::endl;
}

void test_initializer_list() {
    auto result = modern_cpp::linear_search(std::vector<double>{1.1, 2.2, 3.3}, 2.2);
    assert(result.has_value() && *result == 1);
    
    std::cout << "Initializer list tests passed!" << std::endl;
}

void test_binary_search() {
    // TODO: Implement tests for binary search
}

void test_binary_search_old() {
    int arr[] = {10, 20, 30, 40, 50};
    int size = 5;

    assert(legacy_cpp::binary_search(arr, size, 30) == 2);
    assert(legacy_cpp::binary_search(arr, size, 10) == 0);
    assert(legacy_cpp::binary_search(arr, size, 50) == 4);
    assert(legacy_cpp::binary_search(arr, size, 60) == -1);
    
    std::cout << "Binary search old tests passed!" << std::endl;
}

int main() {
    test_vector();
    test_array();
    test_initializer_list();
    test_binary_search();
    test_binary_search_old();
    std::cout << "All modern C++17 tests passed!" << std::endl;
    return 0;
}
