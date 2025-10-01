import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pybind11_example


def test_hello():
    result = pybind11_example.hello()
    assert result == "Hello from pybind11-example!"
    assert isinstance(result, str)
