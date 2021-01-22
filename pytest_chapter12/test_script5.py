"""
Created by 2020/12/01
QQ: 2574674466
微信公众号：TimTest
"""
import pytest

@pytest.fixture()
def test_1():
    return 33

@pytest.fixture()
def test_2():
    return [1,2,3]

def test_fixture(test_1,test_2):
    a = test_1
    b = test_2

    assert a == 33
    assert len(b) == 3

