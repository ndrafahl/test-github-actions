import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from lambda3 import get_random_int


def test_get_random_int():
    x = 0
    y = 10
    z = get_random_int(x, y)
    assert z > x and z < y
