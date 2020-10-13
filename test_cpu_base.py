import pytest

from cpu_base import CPUTest

@pytest.fixture
def cpu():
    cpu = CPUTest()

    cpu.memory.load([2,99,5,200,7,201,9,11,100])

    cpu.memory.set_contents_value(100, 12)
    cpu.memory.set_contents_value(101, 9)
    cpu.memory.set_contents_value(200, 255)

    return cpu


def test_disassemble(cpu):
    disassembly = cpu.disassemble()
    assert len(disassembly) == 7
    assert disassembly == [[0, 'LDBV', 99], [2, 'LDAM', 200], [4, 'LDMA', 201], [6, 'GTAB'], [7, 'JMPV', 100], [100, 'JCRV', 9], [200, 255]]