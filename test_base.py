import pytest

from base import Component, DoubleComponent


def test_double_component_get_contents():
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


def test_double_component_add_to_contents():
    H = Component("H")
    L = Component("L")
    HL = DoubleComponent("HL", L, H)

    H.set_contents(0)
    L.set_contents(0)

    carry_flag = HL.add_to_contents(1)
    assert HL.get_contents() == 1
    assert carry_flag == 0

    carry_flag = HL.add_to_contents(1000)
    assert HL.get_contents() == 1001
    assert carry_flag == 0

    carry_flag = HL.add_to_contents(100000)
    assert HL.get_contents() == 35465
    assert carry_flag == 1


def test_double_component_subtract_from_contents():
    H = Component("H")
    L = Component("L")
    HL = DoubleComponent("HL", L, H)

    H.set_contents(0)
    L.set_contents(1)

    carry_flag = HL.subtract_from_contents(1)
    assert HL.get_contents() == 0
    assert carry_flag == 0

    HL.set_contents_value(1000)
    carry_flag = HL.subtract_from_contents(1000)
    assert HL.get_contents() == 0
    assert carry_flag == 0

    HL.set_contents_value(1001)
    carry_flag = HL.subtract_from_contents(2)
    assert HL.get_contents() == 999
    assert carry_flag == 0

    HL.set_contents_value(1)
    carry_flag = HL.subtract_from_contents(2)
    assert HL.get_contents() == 65535
    assert carry_flag == 1


def test_double_components_set_contents_value():
    H = Component("H")
    L = Component("L")
    HL = DoubleComponent("HL", L, H)

    H.set_contents(0)
    L.set_contents(0)

    HL.set_contents_value(1)
    assert HL.get_contents() == 1

    HL.set_contents_value(1000)
    assert HL.get_contents() == 1000

    HL.set_contents_value(0)
    assert HL.get_contents() == 0


def test_double_components_set_contents():
    H = Component("H")
    L = Component("L")
    HL = DoubleComponent("HL", L, H)

    H.set_contents(0)
    L.set_contents(0)

    HL.set_contents(1,0)
    assert HL.get_contents() == 1

    HL.set_contents(1,1)
    assert HL.get_contents() == 257
    assert L.get_contents() == 1
    assert H.get_contents() == 1
