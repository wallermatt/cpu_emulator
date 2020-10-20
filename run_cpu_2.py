from cpu_base import CPUTest

cpu = CPUTest()
cpu.simple_assembler('bubble.asm')
cpu.run()
print(cpu.memory.dump())
