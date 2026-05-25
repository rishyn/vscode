cmake_minimum_required(VERSION 3.20)
# Add benchmark to CMAKE_PREFIX_PATH if not already set
project(Graph)
# If necessary, use the RELATIVE flag, otherwise each source file may be listed
# with full pathname. RELATIVE may makes it easier to extract an executable name
# automatically.
#add_subdirectory("../thirdparty")
file( GLOB APP_SOURCES RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} *.cpp )
# file( GLOB APP_SOURCES ${CMAKE_SOURCE_DIR}/*.c )
# AUX_SOURCE_DIRECTORY(${CMAKE_CURRENT_SOURCE_DIR} APP_SOURCES)

# Google Benchmark
find_package(benchmark REQUIRED)

foreach( testsourcefile ${APP_SOURCES} )
    string( REPLACE ".cpp" "" testname ${testsourcefile} )
    add_executable( ${testname} ${testsourcefile} )
    set_target_properties(${testname} PROPERTIES
        LINKER_LANGUAGE CXX
        CXX_STANDARD 20
        COMPILE_OPTIONS "-O3;-ffast-math;"
    )
    #target_include_directories(${testname} PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/.. /opt/homebrew/include)
    if(testname STREQUAL "benchmark_kruskal")
        target_link_libraries(${testname} benchmark::benchmark)
    endif()
endforeach( testsourcefile ${APP_SOURCES} )
