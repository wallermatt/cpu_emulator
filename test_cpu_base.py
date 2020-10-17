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
    assert len(disassembly) == 251
    assert disassembly[0] == [0, 2, 'LDBV', 99]
    assert disassembly[-1] == [255, 0]


def test_disassemble_to_file(cpu):
    cpu.disassemble_to_file()


def test_decimal_to_hex(cpu):
    assert cpu._decimal_to_hex(0) == '0'
    assert cpu._decimal_to_hex(1) == '1'
    assert cpu._decimal_to_hex(255) == 'ff'
    assert cpu._decimal_to_hex(1000) == '3e8'


def test_hex_to_decimal(cpu):
    assert cpu._hex_to_decimal('0') == 0
    assert cpu._hex_to_decimal('1') == 1
    assert cpu._hex_to_decimal('ff') == 255

def test_load_file_to_list(cpu):
    row_list = cpu._load_file_to_list('test1.asm')
    assert row_list == ['LDAV,5', 'LDBA', '255']


def test_simple_assembler(cpu):
    cpu.simple_assembler('test1.asm')
    disassembly = cpu.disassemble()
    assert cpu.memory.dump()[0:4] == [1, 5, 4, 255]
    assert disassembly[0:3] == [[0, 1, 'LDAV', 5], [2, 4, 'LDBA'], [3, 255]]


def test_inca(cpu):
    cpu.A.set_contents(0)
    assert cpu.C.get_contents() == 0
    cpu.instructions_by_name['INCA'].run()
    assert cpu.A.get_contents() == 1
    assert cpu.C.get_contents() == 0

    cpu.A.set_contents(0)
    cpu.C.set_contents(1) 
    cpu.instructions_by_name['INCA'].run()
    assert cpu.A.get_contents() == 1
    assert cpu.C.get_contents() == 0

    cpu.A.set_contents(255)
    cpu.instructions_by_name['INCA'].run()
    assert cpu.A.get_contents() == 0
    assert cpu.C.get_contents() == 1


def test_ADDAB(cpu):
    cpu.A.set_contents(0)
    cpu.B.set_contents(1)
    cpu.instructions_by_name['ADDAB'].run()
    assert cpu.A.get_contents() == 1
    assert cpu.C.get_contents() == 0

    cpu.A.set_contents(10)
    cpu.B.set_contents(255)
    cpu.instructions_by_name['ADDAB'].run()
    assert cpu.A.get_contents() == 9
    assert cpu.C.get_contents() == 1


def test_DECA(cpu):
    cpu.A.set_contents(1)
    assert cpu.C.get_contents() == 0
    cpu.instructions_by_name['DECA'].run()
    assert cpu.A.get_contents() == 0
    assert cpu.C.get_contents() == 0

    cpu.A.set_contents(1)
    cpu.C.set_contents(1) 
    cpu.instructions_by_name['DECA'].run()
    assert cpu.A.get_contents() == 0
    assert cpu.C.get_contents() == 0

    cpu.A.set_contents(0)
    cpu.instructions_by_name['DECA'].run()
    assert cpu.A.get_contents() == 255
    assert cpu.C.get_contents() == 1


def test_SUBAB(cpu):
    cpu.A.set_contents(1)
    cpu.B.set_contents(1)
    cpu.instructions_by_name['SUBAB'].run()
    assert cpu.A.get_contents() == 0
    assert cpu.C.get_contents() == 0

    cpu.A.set_contents(10)
    cpu.B.set_contents(255)
    cpu.instructions_by_name['SUBAB'].run()
    assert cpu.A.get_contents() == 11
    assert cpu.C.get_contents() == 1


def test_LTAB(cpu):
    cpu.A.set_contents(1)
    cpu.B.set_contents(1)
    cpu.R.set_contents(0)
    cpu.instructions_by_name['LTAB'].run()
    assert cpu.R.get_contents() == 0

    cpu.A.set_contents(0)
    cpu.B.set_contents(1)
    cpu.R.set_contents(0)
    cpu.instructions_by_name['LTAB'].run()
    assert cpu.R.get_contents() == 1


def test_EQAB(cpu):
    cpu.A.set_contents(1)
    cpu.B.set_contents(1)
    cpu.R.set_contents(0)
    cpu.instructions_by_name['EQAB'].run()
    assert cpu.R.get_contents() == 1

    cpu.A.set_contents(0)
    cpu.B.set_contents(1)
    cpu.R.set_contents(0)
    cpu.instructions_by_name['EQAB'].run()
    assert cpu.R.get_contents() == 0
