"""
Created by 2020/12/01
QQ: 2574674466
微信公众号：TimTest
"""
import pytest
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    @pytest.mark.regression
    def test_two(self):
        x = "hello"
        assert hasattr(x,"check")
