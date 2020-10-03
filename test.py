from base import ComponentBase, MemoryBase
from microcode import LDRV, LDRR, CPU, LDRM, LDMR, GTRR, JMPV


def main():
    A = ComponentBase("A Register")
    B = ComponentBase("B Register")
    P = ComponentBase("P Program Counter")
    C = ComponentBase("C Carry Flag")
    R = ComponentBase("R Result Flag")
    RAM = MemoryBase("RAM", 256)


    instruction_set = [
        LDRV("LDAV", 1, RAM, P, [A]),
        LDRV("LDBV", 2, RAM, P, [B]),
        LDRR("LDAB", 3, RAM, P, [A,B]),
        LDRR("LDBA", 4, RAM, P, [B,A]),
        LDRM("LDAM", 5, RAM, P, [A]),
        LDRM("LDBM", 6, RAM, P, [B]),
        LDMR("LDMA", 7, RAM, P, [A]),
        LDMR("LDMB", 8, RAM, P, [B]),
        GTRR("GTAB", 9, RAM, P, [A,B,R]),
        GTRR("GTBA", 10, RAM, P, [B,A,R]),
        JMPV("JMPV", 11, RAM, P),
        JMPV("JCRV", 12, RAM, P, [R]),
    ]

    instructions_by_opcode = {ins.opcode: ins for ins in instruction_set}

    cpu = CPU("cpu", 0, RAM, P, None, instructions_by_opcode)

    RAM.set_contents_value(0, 2)
    RAM.set_contents_value(1, 99)
    RAM.set_contents_value(2, 5)
    RAM.set_contents_value(3, 200)
    RAM.set_contents_value(4, 7)
    RAM.set_contents_value(5, 201)
    RAM.set_contents_value(6, 9)
    RAM.set_contents_value(7, 11)
    RAM.set_contents_value(8, 100)
    RAM.set_contents_value(100, 12)
    RAM.set_contents_value(101, 9)
    RAM.set_contents_value(200, 255)

    cpu.run()

    print(A.get_contents())
    print(B.get_contents())
    print(R.get_contents())
    print(RAM.dump())

main()
