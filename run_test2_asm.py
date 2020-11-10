import datetime
from cpu_base import CPUTest

cpu = CPUTest()
cpu.simple_assembler('test2.asm')
print(cpu.memory.dump()[0:20])

start = datetime.datetime.now()
cpu.run(debug=True)
print(datetime.datetime.now() - start)
print(cpu.memory.dump()[200:221])
#