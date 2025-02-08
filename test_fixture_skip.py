import pytest

@pytest.mark.skip(reason="Skipping this test for now")
def test_skip():
    assert 1 == 1
