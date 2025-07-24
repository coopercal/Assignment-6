import pytest

from fibonacci import Fibonacci


def test_RaiseValueError():
    with pytest.raises(ValueError):
        Fibonacci(9.6)