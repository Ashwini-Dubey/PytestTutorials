import pytest

@pytest.fixture
def setup_teardown():
    print("\nSetup: Open resource")
    yield "resource"
    print("\nTeardown: Close resource")

def test_resource(setup_teardown):
    assert setup_teardown == "resource"