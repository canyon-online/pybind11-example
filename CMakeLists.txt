cmake_minimum_required(VERSION 3.15)
project(pybind11_example LANGUAGES CXX)

add_subdirectory(extern/pybind11)

pybind11_add_module(_core MODULE src/main.cpp)
install(TARGETS _core 
    LIBRARY DESTINATION pybind11_example
    RUNTIME DESTINATION pybind11_example)
