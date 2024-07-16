import os, sys

# sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.dirname(os.getcwd()))

from script import addition


def test_data_type():
    assert isinstance(addition(1, 2), int)
