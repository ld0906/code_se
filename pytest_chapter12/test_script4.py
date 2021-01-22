"""
Created by 2020/12/01
QQ: 2574674466
微信公众号：TimTest
"""

import pytest

def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()