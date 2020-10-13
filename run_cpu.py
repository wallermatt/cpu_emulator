from cpu_base import CPUTest

cpu = CPUTest()

cpu.memory.load([2,99,5,200,7,201,9,11,100])

cpu.memory.set_contents_value(100, 12)
cpu.memory.set_contents_value(101, 9)
cpu.memory.set_contents_value(200, 255)

print(cpu.memory.dump())

cpu.run()

print(cpu.A.get_contents())
print(cpu.B.get_contents())
print(cpu.R.get_contents())
print(cpu.memory.dump())
