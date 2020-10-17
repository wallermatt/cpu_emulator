import csv
from base import Component, Memory, InstructionBase
from microcode import LDRV, LDRR, LDRM, LDMR, GTRR, JMPV, INC


class CPUTest(InstructionBase):

    MEMORY_SIZE = 256
    PROGRAM_COUNTER = "program_counter"

    def __init__(self):
        self.memory = Memory(self.MEMORY_SIZE)
        self.program_counter = Component(self.PROGRAM_COUNTER)
        self.registers = self._define_registers()
        self.instructions = self._define_instructions()
        self.instructions_by_opcode = {ins.opcode: ins for ins in self.instructions}
        self.instructions_by_name = {ins.name: ins for ins in self.instructions}

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
            INC("INCA", 13, self.memory, self.program_counter, [self.A, self.C]),
        ]
    
        return instructions

    def _decimal_to_hex(self, decimal_int):
        return hex(decimal_int)[2:]

    def _hex_to_decimal(self, hex_str):
        return int(hex_str, 16)

    def _load_file_to_list(self, filename):
        row_list = []
        with open(filename, 'r') as f:
            row_list = [r.strip('\n') for r in f.readlines()]
        return row_list
    
    def run(self):
        print("Starting CPU execution at {}".format(self.program_counter.get_contents()))
        opcode = self.get_memory_location_contents_and_inc_pc()
        while opcode != 0:
            self.instructions_by_opcode[opcode].run()
            opcode = self.get_memory_location_contents_and_inc_pc()
        print("Ending CPU execution at {}".format(self.program_counter.get_contents()))

    def disassemble(self):
        disassembly = []
        address = 0
        while address < self.MEMORY_SIZE:
            contents = self.memory.get_contents_value(address)
            current_row = [address, contents]
            if contents in self.instructions_by_opcode:
                instruction = self.instructions_by_opcode[contents]
                current_row.append(instruction.name)
                number_of_args = instruction.LENGTH - 1
                for _ in range(number_of_args):
                    address += 1
                    current_row.append(self.memory.get_contents_value(address))
            disassembly.append(current_row)
            address += 1
        return disassembly

    def disassemble_to_file(self, filename="cpu.csv"):
        disassembly = self.disassemble()
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(disassembly)

    def simple_assembler(self, filename):
        row_list = self._load_file_to_list(filename)
        contents_list = []
        for row in row_list:
            symbols = row.split(',')
            if symbols[0] in self.instructions_by_name:
                instruction = self.instructions_by_name[symbols[0]]
                if len(symbols) != instruction.LENGTH:
                    raise('{} length is {} but symbols are {}'. format(
                        instruction.name,
                        instruction.LENGTH,
                        symbols
                    ))
                symbols[0] = instruction.opcode
            for symbol in symbols:
                contents_list.append(int(symbol))
        print(contents_list)
        self.memory.load(contents_list)



