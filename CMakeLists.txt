cmake_minimum_required(VERSION 3.18...4.0)
project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)

if(MSVC)
    add_compile_options("/MP")
endif()

set(PYBIND11_FINDPYTHON ON)
add_subdirectory(extern/pybind11)

pybind11_add_module(example src/example.cpp)

install(TARGETS example LIBRARY DESTINATION example)
