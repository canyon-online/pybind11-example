# pybind11-example

A simple example project demonstrating how to use pybind11 to create Python bindings for C++ code.

## Overview

This project creates a Python module `example` that exposes a C++ function `square()` to Python. The function takes a number and returns its square.

## Project Structure

```
pybind11-example/
├── src/
│   ├── example/
│   │   ├── __init__.py             # Python package initialization
│   │   └── example.pyi             # Package type hinting
│   └── example.cpp                 # C++ source with pybind11 bindings
├── tests/
│   └── test_example.py             # Python package test
├── extern/
│   └── pybind11/                   # pybind11 submodule (v3.0.1)
├── CMakeLists.txt                  # CMake build configuration
├── pyproject.toml                  # Python project configuration
├── pytest.ini                      # pytest configuration
├── requirements-test.txt           # Test dependencies
└── README.md
```

## Requirements

- Python 3.12+
- CMake 3.18+
- Visual Studio 2022+ (on Windows) or GCC 4.8+/Clang 3.3+ (on Linux)
- Git (for submodules)

## Building

1. Clone the repository with submodules:
   ```bash
   git clone --recursive <repository-url>
   cd pybind11-example-dll
   ```

2. **Recommended: Using scikit-build-core (pip install)**
   ```bash
   pip install .
   ```

3. **Alternative: Direct CMake build**

   **Windows (Visual Studio):**
   ```bash
   mkdir build
   cd build
   cmake .. -G "Visual Studio 17 2022" -A x64
   cmake --build . --config Release
   ```

   **Linux/macOS:**
   ```bash
   mkdir build
   cd build
   cmake .. -DCMAKE_BUILD_TYPE=Release
   cmake --build .
   ```

## Usage

After building, the `example.pyd` file will be created in the build directory:

```python
import example

# Square a number
result = example.square(5)
print(result)  # 25.0

result = example.square(2.5)
print(result)  # 6.25
```

## Testing

Install pytest and run the tests:

```bash
pip install -r requirements-test.txt
pytest tests/
```

## Development

This project uses:
- **pybind11** for C++/Python bindings
- **scikit-build-core** for Python packaging
- **CMake** for build configuration
- **pytest** for testing
- **Visual Studio Code** with CMake and Python extensions for development
