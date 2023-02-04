import pytest

"""Parent of test_loginpage class"""


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass
