# to run test cases using markers run command py.test -m markername
# and use @pytest.mark.markername above the function

import pytest


@pytest.mark.home
def test_m1():
    x = 10
    y = 11
    assert x + y == 21
    print(x)


def test_m2():
    assert "name" == "name"


@pytest.mark.home
def test_m3():
    assert True
