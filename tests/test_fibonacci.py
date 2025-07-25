import pytest

from fibonacci import Fibonacci


def test_RaiseValueError():
    with pytest.raises(ValueError):
        Fibonacci(9.6)

def test_ValueofZero():
    assert list(Fibonacci(0)) == [0]

def test_ValueofOne():
    assert list(Fibonacci(1)) == [0, 1]