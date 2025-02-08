import pytest

def divide(x, y):
    return x / y

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
