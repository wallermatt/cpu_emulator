from cpu_base import CPUTest

cpu = CPUTest()
cpu.simple_assembler('factorial_call.asm')




cpu.run(debug=True)
print(cpu.B.get_contents())
print(cpu.memory.dump()[150:255])
