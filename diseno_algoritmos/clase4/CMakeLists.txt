cmake_minimum_required(VERSION 3.20)
# Add benchmark to CMAKE_PREFIX_PATH if not already set
project(Divide_and_Conquer)
# If necessary, use the RELATIVE flag, otherwise each source file may be listed
# with full pathname. RELATIVE may makes it easier to extract an executable name
# automatically.
file( GLOB APP_SOURCES RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} *.cpp )
# file( GLOB APP_SOURCES ${CMAKE_SOURCE_DIR}/*.c )
# AUX_SOURCE_DIRECTORY(${CMAKE_CURRENT_SOURCE_DIR} APP_SOURCES)

# Google Benchmark Configuration
find_package(benchmark QUIET)

if(NOT benchmark_FOUND)
    include(FetchContent)
    FetchContent_Declare(
      google_benchmark
      GIT_REPOSITORY https://github.com/google/benchmark.git
      GIT_TAG        v1.8.3
    )
    set(BENCHMARK_ENABLE_TESTING OFF CACHE BOOL "" FORCE)
    set(BENCHMARK_ENABLE_GTEST_TESTS OFF CACHE BOOL "" FORCE)
    set(BENCHMARK_ENABLE_INSTALL OFF CACHE BOOL "" FORCE)
    FetchContent_MakeAvailable(google_benchmark)
endif()

foreach( testsourcefile ${APP_SOURCES} )
    string( REPLACE ".cpp" "" testname ${testsourcefile} )
    if(testsourcefile STREQUAL "benchmark_matrix_multiplication_bm.cpp")
        add_executable(benchmark_matrix_multiplication_bm benchmark_matrix_multiplication_bm.cpp)
        target_link_libraries(benchmark_matrix_multiplication_bm benchmark::benchmark pthread)
        set_target_properties(benchmark_matrix_multiplication_bm PROPERTIES
            LINKER_LANGUAGE CXX
            CXX_STANDARD 20
            COMPILE_OPTIONS "-O3;-Wall;-ffast-math"
        )
        install(TARGETS benchmark_matrix_multiplication_bm DESTINATION "bin/divide_and_conquer")
    else()
        add_executable( ${testname} ${testsourcefile} )
        set_target_properties(${testname} PROPERTIES
            LINKER_LANGUAGE CXX
            CXX_STANDARD 20
            COMPILE_OPTIONS "-O3;-Wall;-ffast-math"
        )
        if(OpenMP_CXX_FOUND)
            target_link_libraries(${testname} OpenMP::OpenMP_CXX)
        endif()
        install(TARGETS ${testname} DESTINATION "bin/divide_and_conquer")
    endif()
endforeach( testsourcefile ${APP_SOURCES} )
