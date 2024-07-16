"""test_1.py"""

import os
import sys

# sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.dirname(os.getcwd()))

from script import addition

# print(os.getcwd())
# print('\n\n')
# print(sys.path)


# print('\n\n')
# print(sys.path)


def test_addition():
    """test"""
    assert addition(1, -1) == 0
