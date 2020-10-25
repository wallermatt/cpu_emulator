from cpu_base import CPUTest

cpu = CPUTest()
cpu.simple_assembler('pivot.asm')

cpu.memory.set_contents_value(200, 10)
cpu.memory.set_contents_value(201, 9)
cpu.memory.set_contents_value(202, 8)
cpu.memory.set_contents_value(203, 7)
cpu.memory.set_contents_value(204, 6)
cpu.memory.set_contents_value(205, 1)
cpu.memory.set_contents_value(206, 4)
cpu.memory.set_contents_value(207, 3)
cpu.memory.set_contents_value(208, 2)
cpu.memory.set_contents_value(209, 5)

old = cpu.memory.dump()[200:210]
cpu.run(debug=True)
print(old)
print(cpu.memory.dump()[200:210])
cpu.disassemble_to_file('qs.csv')
