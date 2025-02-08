import sys
import pytest

@pytest.mark.skipif(sys.version_info > (3, 8), reason="Requires Python 3.8-")
def test_python_version():
    assert True
