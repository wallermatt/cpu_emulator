from cpu_base import CPUTest

cpu = CPUTest()
cpu.simple_assembler('test_pointer.asm')




cpu.run(debug=True)
print(cpu.memory.dump()[100:110])
