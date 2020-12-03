import pytest
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    @pytest.mark.regression
    def test_two(self):
        x = "hello"
        assert hasattr(x,"check")