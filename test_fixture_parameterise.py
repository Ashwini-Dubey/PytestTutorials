import pytest

@pytest.mark.parametrize("x, y, sum", [(1, 2, 3), (4, 5, 9), (10, 20, 30)])
def test_add(x, y, sum):
    assert x + y == sum
