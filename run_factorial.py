from cpu_base import CPUTest

cpu = CPUTest()
cpu.simple_assembler('factorial.asm')




cpu.run(debug=True)
print(cpu.memory.dump()[150:152])
