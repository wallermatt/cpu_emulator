from cpu_base import CPUTest

cpu = CPUTest()
cpu.simple_assembler('bubble.asm')

cpu.memory.set_contents_value(120, 10)
cpu.memory.set_contents_value(121, 9)
cpu.memory.set_contents_value(122, 8)
cpu.memory.set_contents_value(123, 7)
cpu.memory.set_contents_value(124, 6)
cpu.memory.set_contents_value(125, 5)
cpu.memory.set_contents_value(126, 4)
cpu.memory.set_contents_value(127, 3)
cpu.memory.set_contents_value(128, 2)
cpu.memory.set_contents_value(129, 1)

cpu.run()
print(cpu.memory.dump()[120:130])
