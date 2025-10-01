import os
import sys

# Add the build directory to Python path
sys.path.insert(
    0, os.path.join(os.path.dirname(__file__), "..", "build", "Release")
)  # or "Debug"

import _core


def test_hello_from_bin():
    result = _core.hello_from_bin()
    assert result == "Hello from pybind11-example!"
    assert isinstance(result, str)
