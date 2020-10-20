import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from lambda2 import mul, div


def test_mul():
    assert mul(6, 2) == 12


def test_div():
    assert div(6, 2) == 3