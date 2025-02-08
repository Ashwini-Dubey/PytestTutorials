# Grouping multiple tests in a class
import pytest
class Test_MultipleTests:
    def test_one(self):
        assert 4 + 5 == 9

    @pytest.mark.smoke
    def test_two(self):
        text = "Tests with multiple tests grouped in a class"
        assert "multiple" in text