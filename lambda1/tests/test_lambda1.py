import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from lambda1 import inc, dec


def test_inc():
    assert inc(0) == 1


def test_dec():
    assert dec(0) == -1