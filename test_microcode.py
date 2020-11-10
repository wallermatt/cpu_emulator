import pytest

from base import Component, DoubleComponent, Memory
from microcode import LDRV


def test_LDRV():
    program_counter = Component("P")
    A = Component("A")
    memory = Memory(256)
    LDAV = LDRV("LDAV", 1, memory, program_counter, [A])
    assert LDAV.LENGTH == 2
