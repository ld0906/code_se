"""
Created by 2020/12/01
QQ: 2574674466
微信公众号：TimTest
"""

import pytest

@pytest.mark.regression
def test_method1():
    assert 3 ==2

@pytest.mark.regression
def test_method2():
    assert 3 ==3

@pytest.mark.skip
def test_method3():
    assert 4>1

@pytest.mark.regression
def test_method4():
    assert 5 > 4

@pytest.mark.xfail
def test_method5():
    assert 7 < 6


def test_method6():
    assert 5 < 6


def test_method7():
    assert 7 > 6
