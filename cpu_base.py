from base import Component, Memory, InstructionBase
from microcode import LDRV, LDRR, LDRM, LDMR, GTRR, JMPV


class CPUTest(InstructionBase):

    MEMORY_SIZE = 256
    PROGRAM_COUNTER = "program_counter"

    def __init__(self):
        self.memory = Memory(self.MEMORY_SIZE)
        self.program_counter = Component(self.PROGRAM_COUNTER)
        self.registers = self._define_registers()
        self.instructions = self._define_instructions()
        self.instructions_by_opcode = {ins.opcode: ins for ins in self.instructions}

    def _define_registers(self):
        registers = []
        self.A = Component("A Register")
        self.B = Component("B Register")
        self.C = Component("C Carry Flag")
        self.R = Component("R Result Flag")

        registers = [
            self.A,
            self.B,
            self.C,
            self.R
        ]

        return registers

    def _define_instructions(self):
        instructions = [
            LDRV("LDAV", 1, self.memory, self.program_counter, [self.A]),
            LDRV("LDBV", 2, self.memory, self.program_counter, [self.B]),
            LDRR("LDAB", 3, self.memory, self.program_counter, [self.A,self.B]),
            LDRR("LDBA", 4, self.memory, self.program_counter, [self.B,self.A]),
            LDRM("LDAM", 5, self.memory, self.program_counter, [self.A]),
            LDRM("LDBM", 6, self.memory, self.program_counter, [self.B]),
            LDMR("LDMA", 7, self.memory, self.program_counter, [self.A]),
            LDMR("LDMB", 8, self.memory, self.program_counter, [self.B]),
            GTRR("GTAB", 9, self.memory, self.program_counter, [self.A,self.B,self.R]),
            GTRR("GTBA", 10, self.memory, self.program_counter, [self.A,self.R]),
            JMPV("JMPV", 11, self.memory, self.program_counter),
            JMPV("JCRV", 12, self.memory, self.program_counter, [self.R]),
        ]
    
        return instructions

    def run(self):
        print("Starting CPU execution at {}".format(self.program_counter.get_contents()))
        opcode = self.get_memory_location_contents_and_inc_pc()
        while opcode != 0:
            self.instructions_by_opcode[opcode].run()
            opcode = self.get_memory_location_contents_and_inc_pc()
        print("Ending CPU execution at {}".format(self.program_counter.get_contents()))
