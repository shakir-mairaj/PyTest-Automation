# enter py.test to run all test cases
#enter py.test filename to run a particular file
#enter py.test -k keyword to run testcases containing the keyword
#enter py.test -v to get more detailed output

import pytest


def test_reg():
    x = 100
    y = 201
    assert x + 1 == y, "test case passed"


def test_login():
    name = "admin"
    assert name.upper() == "ADMIN"


def test_logout():
    assert "user" == "admin", "test case failed"
