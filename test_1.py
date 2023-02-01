# pytest file name and function name should either start or end with test keyword

import pytest


def test_a1():
    x = 1
    y = 2
    assert x + 1 == y, "test case passed"


def test_a2():
    name = "abc"
    assert name.upper() == "ABC"


def test_a3():
    assert 100 == 200, "test case failed"
