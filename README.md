# pybind11-example

A simple example project demonstrating how to use pybind11 to create Python bindings for C++ code.

## Overview

This project creates a Python module `_core` that exposes a C++ function `hello_from_bin()` to Python. The module is wrapped in a Python package `pybind11_example` that provides a convenient `hello()` function.

## Project Structure

```
pybind11-example/
├── src/
│   ├── main.cpp                    # C++ source with pybind11 bindings
│   └── pybind11_example/
│       └── __init__.py             # Python package wrapper
├── tests/
│   ├── test_core.py                # Direct tests for _core module
│   └── test_pybind11_example.py    # Tests for Python package
├── extern/
│   └── pybind11/                   # pybind11 submodule
├── CMakeLists.txt                  # CMake build configuration
└── README.md
```

## Requirements

- Python 3.12+
- CMake 3.15+
- Visual Studio 2017+ (on Windows)
- Git (for submodules)

## Building

1. Clone the repository with submodules:
   ```bash
   git clone --recursive <repository-url>
   cd pybind11-example
   ```

2. Configure and build with CMake:
   ```bash
   mkdir build
   cd build
   cmake .. -G "Visual Studio 17 2022" -A x64
   cmake --build . --config Release
   ```

## Usage

After building, the `_core.pyd` file will be created in the build directory. You can use it directly or through the Python wrapper:

```python
# Direct usage of _core module
import _core
result = _core.hello_from_bin()
print(result)  # "Hello from pybind11-example!"

# Using the Python package wrapper
import pybind11_example
result = pybind11_example.hello()
print(result)  # "Hello from pybind11-example!"
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
- **CMake** for build configuration
- **pytest** for testing
- **Visual Studio Code** with CMake and Python extensions for development
