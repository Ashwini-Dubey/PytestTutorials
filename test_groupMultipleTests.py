# Grouping multiple tests in a class
class Test_MultipleTests:
    def test_one(self):
        assert 4 + 5 == 9

    def test_two(self):
        text = "Tests with multiple tests grouped in a class"
        assert "multiple" in text