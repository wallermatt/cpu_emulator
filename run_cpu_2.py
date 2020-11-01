import datetime
from cpu_base import CPUTest

cpu = CPUTest()
cpu.simple_assembler('bubble.asm')

cpu.memory.set_contents_value(200, 10)
cpu.memory.set_contents_value(201, 9)
cpu.memory.set_contents_value(202, 8)
cpu.memory.set_contents_value(203, 5)
cpu.memory.set_contents_value(204, 6)
cpu.memory.set_contents_value(205, 1)
cpu.memory.set_contents_value(206, 4)
cpu.memory.set_contents_value(207, 3)
cpu.memory.set_contents_value(208, 2)
cpu.memory.set_contents_value(209, 5)

cpu.memory.set_contents_value(210, 1)
cpu.memory.set_contents_value(211, 4)
cpu.memory.set_contents_value(212, 3)
cpu.memory.set_contents_value(213, 2)
cpu.memory.set_contents_value(214, 5)

start = datetime.datetime.now()
cpu.run(debug=False)
print(datetime.datetime.now() - start)
print(cpu.memory.dump()[200:221])
