from cpu_base import CPUTest

cpu = CPUTest()
cpu.simple_assembler('fibo.asm')
cpu.run()
print(cpu.memory.dump())
