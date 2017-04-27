# Sample Test passing with nose and pytest
from .context import {{ cookiecutter.package_name }}
from {{ cookiecutter.package_name }} import *


def test_pass():
    assert True, "dummy sample test"
