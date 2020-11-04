import pytest

from base import Component, DoubleComponent


def test_double_compont_get_contents():
    H = Component("H")
    L = Component("L")
    HL = DoubleComponent("HL", L, H)

    H.set_contents(0)
    L.set_contents(0)
    assert HL.get_contents() == 0

    H.set_contents(0)
    L.set_contents(1)
    assert HL.get_contents() == 1

    H.set_contents(1)
    L.set_contents(1)
    assert HL.get_contents() == 257
