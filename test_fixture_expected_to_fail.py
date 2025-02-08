import pytest

@pytest.mark.xfail
def test_fail():
    assert 1 == 2
