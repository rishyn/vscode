cmake_minimum_required(VERSION 3.11)
project(LinearSearchProject)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include_directories(.)

# Functional Test
add_executable(test_search test_search.cpp)

# Benchmark Configuration
find_package(benchmark QUIET)

add_executable(benchmark_search benchmark_search.cpp)
target_link_libraries(benchmark_search benchmark::benchmark)
