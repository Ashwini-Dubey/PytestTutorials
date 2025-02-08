import pytest

@pytest.fixture()
def sample_data():
    return {"name":"Ashwini","age":28}

def test_fixture(sample_data):
    assert sample_data["name"] == "Ashwini"
    assert sample_data["age"] == 28