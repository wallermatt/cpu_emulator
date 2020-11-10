import csv
from base import Component, Memory, InstructionBase, DoubleComponent
from microcode import (
    LDRV, LDRR, LDRM, LDMR, GTRR, JMPV, INCR, ADDRR, DECR, SUBRR, LTRR, EQRR, JMNV, LDIMRV,
    LDIMRR, LDIRRM, PUSHR, POPR, JMPR, JMNR, CALLV, CALNV, RET, RETN
)
class CPUTest(InstructionBase):

    MEMORY_SIZE = 256
    PROGRAM_COUNTER = "P"
    STACK_POINTER = "S"

    def __init__(self):
        self.memory = Memory(self.MEMORY_SIZE)
        self.program_counter_low = Component("PL")
        self.program_counter_high = Component("PH")
        self.program_counter = DoubleComponent("P", self.program_counter_low, self.program_counter_high)
        self.stack_pointer = Component(self.STACK_POINTER)
        self.stack_pointer.set_contents(self.MEMORY_SIZE - 1)
        self.registers = self._define_registers()
        self.registers_by_name ={reg.name: reg for reg in self.registers}
        self.instructions = self._define_instructions()
        self.instructions_by_opcode = {ins.opcode: ins for ins in self.instructions}
        self.instructions_by_name = {ins.name: ins for ins in self.instructions}

    def _define_registers(self):
        registers = []
        self.A = Component("A")
        self.B = Component("B")
        self.D = Component("D")
        self.C = Component("C")
        self.R = Component("R")
        self.H = Component("H")
        self.L = Component("L")
        self.HL = DoubleComponent("HL", self.L, self.H)

        registers = [
            self.A,
            self.B,
            self.D,
            self.C,
            self.R,
            self.program_counter,
            self.stack_pointer,
            self.H,
            self.L,
            self.HL,
        ]

        return registers

    def _define_instructions(self):
        instructions = [
            LDRV("LDAV", 1, self.memory, self.program_counter, [self.A]),
            LDRV("LDBV", 2, self.memory, self.program_counter, [self.B]),
            LDRR("LDAB", 3, self.memory, self.program_counter, [self.A, self.B]),
            LDRR("LDBA", 4, self.memory, self.program_counter, [self.B, self.A]),
            LDRM("LDAM", 5, self.memory, self.program_counter, [self.A]),
            LDRM("LDBM", 6, self.memory, self.program_counter, [self.B]),
            LDMR("LDMA", 7, self.memory, self.program_counter, [self.A]),
            LDMR("LDMB", 8, self.memory, self.program_counter, [self.B]),
            GTRR("GTAB", 9, self.memory, self.program_counter, [self.A, self.B, self.R]),
            GTRR("GTBA", 10, self.memory, self.program_counter, [self.B, self.A, self.R]),
            JMPV("JMPV", 11, self.memory, self.program_counter),
            JMPV("JMPRV", 12, self.memory, self.program_counter, [self.R]),
            INCR("INCA", 13, self.memory, self.program_counter, [self.A, self.C]),
            INCR("INCB", 14, self.memory, self.program_counter, [self.B, self.C]),
            ADDRR("ADDAB", 15, self.memory, self.program_counter, [self.A, self.B, self.C]),
            ADDRR("ADDBA", 16, self.memory, self.program_counter, [self.B, self.A, self.C]),
            DECR("DECB", 170, self.memory, self.program_counter, [self.B, self.C]),
            SUBRR("SUBAB", 18, self.memory, self.program_counter, [self.A, self.B, self.C]),
            SUBRR("SUBBA", 19, self.memory, self.program_counter, [self.B, self.A, self.C]),
            LTRR("LTAB", 20, self.memory, self.program_counter, [self.A, self.B, self.R]),
            LTRR("LTBA", 21, self.memory, self.program_counter, [self.B, self.A, self.R]),
            EQRR("EQAB", 22, self.memory, self.program_counter, [self.A, self.B, self.R]),
            EQRR("EQBA", 23, self.memory, self.program_counter, [self.B, self.A, self.R]),
            JMNV("JMNRV", 24, self.memory, self.program_counter, [self.R]),
            JMPV("JMPCV", 25, self.memory, self.program_counter, [self.C]),
            JMNV("JMNCV", 26, self.memory, self.program_counter, [self.C]),
            LDIMRV("LDIMAV", 27, self.memory, self.program_counter, [self.A]),
            LDIMRV("LDIMBV", 28, self.memory, self.program_counter, [self.B]),
            LDIMRR("LDIMAB", 29, self.memory, self.program_counter, [self.A, self.B]),
            LDIMRR("LDIMBA", 30, self.memory, self.program_counter, [self.B, self.A]),
            LDRV("LDDV", 31, self.memory, self.program_counter, [self.D]),
            LDRR("LDDA", 32, self.memory, self.program_counter, [self.D, self.A]),
            LDRR("LDDB", 33, self.memory, self.program_counter, [self.D, self.B]),
            LDIMRV("LDIMDV", 34, self.memory, self.program_counter, [self.D]),
            LDIMRR("LDIMDA", 35, self.memory, self.program_counter, [self.D, self.A]),
            LDIMRR("LDIMDB", 36, self.memory, self.program_counter, [self.D, self.B]),
            INCR("INCD", 37, self.memory, self.program_counter, [self.D, self.C]),
            DECR("DECD", 38, self.memory, self.program_counter, [self.D, self.C]),
            ADDRR("ADDDA", 39, self.memory, self.program_counter, [self.D, self.A, self.C]),
            ADDRR("ADDDB", 40, self.memory, self.program_counter, [self.D, self.B, self.C]),
            GTRR("GTDB", 41, self.memory, self.program_counter, [self.D, self.B, self.R]),
            LDIRRM("LDIADM", 42, self.memory, self.program_counter, [self.A, self.D]),
            LDIRRM("LDIBDM", 43, self.memory, self.program_counter, [self.B, self.D]),
            PUSHR("PUSHA", 44, self.memory, self.stack_pointer, [self.A]),
            PUSHR("PUSHB", 45, self.memory, self.stack_pointer, [self.B]),
            PUSHR("PUSHD", 46, self.memory, self.stack_pointer, [self.D]),
            POPR("POPA", 47, self.memory, self.stack_pointer, [self.A]),
            POPR("POPB", 48, self.memory, self.stack_pointer, [self.B]),
            POPR("POPD", 49, self.memory, self.stack_pointer, [self.D]),
            GTRR("GTAD", 50, self.memory, self.program_counter, [self.A, self.D, self.R]),
            GTRR("GTBD", 51, self.memory, self.program_counter, [self.B, self.D, self.R]),
            JMPR("JMPA", 52, self.memory, self.program_counter, [self.A]),
            JMPR("JMRA", 53, self.memory, self.program_counter, [self.A, self.R]),
            PUSHR("PUSHP", 54, self.memory, self.stack_pointer, [self.program_counter]),
            LDRM("LDDM", 55, self.memory, self.program_counter, [self.D]),
            JMPR("JMPB", 56, self.memory, self.program_counter, [self.B]),
            DECR("DECA", 57, self.memory, self.program_counter, [self.A, self.C]),
            CALLV("CALLV", 58, self.memory, self.program_counter, None, self.stack_pointer),
            CALLV("CALRV", 59, self.memory, self.program_counter, [self.R], self.stack_pointer),
            CALLV("CALCV", 60, self.memory, self.program_counter, [self.C], self.stack_pointer),
            RET("RET", 61, self.memory, self.program_counter, None, self.stack_pointer),
            RET("RETR", 62, self.memory, self.program_counter, [self.R], self.stack_pointer),
            RET("RETC", 63, self.memory, self.program_counter, [self.C], self.stack_pointer),
            CALNV("CANRV", 64, self.memory, self.program_counter, [self.R], self.stack_pointer),
            CALNV("CANCV", 65, self.memory, self.program_counter, [self.C], self.stack_pointer),
            RETN("RETNR", 66, self.memory, self.program_counter, [self.R], self.stack_pointer),
            RETN("RETNC", 67, self.memory, self.program_counter, [self.C], self.stack_pointer),
            LDMR("LDMD", 68, self.memory, self.program_counter, [self.D]),
            ADDRR("ADDHLA", 69, self.memory, self.program_counter, [self.HL, self.B, self.C]),
            INCR("INCHL", 70, self.memory, self.program_counter, [self.HL, self.C]),
            DECR("DECHL", 71, self.memory, self.program_counter, [self.HL, self.C]),
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
    
    def run(self, debug=False):
        instruction_count = 0
        old_state, new_state = {}, {}
        print("Starting CPU execution at {}".format(self.program_counter.get_contents()))
        if debug:
            old_state = self.copy_current_state_values_into_dict()
        opcode = self.get_memory_location_contents_and_inc_pc()
        while opcode != 0:
            self.instructions_by_opcode[opcode].run()
            instruction_count += 1
            if debug:
                new_state = self.copy_current_state_values_into_dict()
                changes = self.compare_state_copies(old_state, new_state)
                if self.PROGRAM_COUNTER in changes:
                    pc_changes = changes[self.PROGRAM_COUNTER]
                    if pc_changes[1] - pc_changes[0] == self.instructions_by_opcode[opcode].LENGTH:
                        changes.pop(self.PROGRAM_COUNTER, None)
                print( self.instructions_by_opcode[opcode].name, changes)
                old_state = new_state
            opcode = self.get_memory_location_contents_and_inc_pc()
        print("Ending CPU execution at {}, instruction count {}".format(self.program_counter.get_contents(), instruction_count))

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
        variable_dict = {}
        line_count = 0
        row_list = self._load_file_to_list(filename)
        contents_list = []

        for row in row_list:
            row = row.replace(' ', '')
            symbols = row.split(',')
            if ';' in symbols[0]:
                continue
            if '=' in symbols[0]:
                variable_value = symbols[0].split('=')
                variable_dict[variable_value[0]] = int(variable_value[1])
                continue
            if ':' in symbols[0]:
                variable_dict[symbols[0][:-1]] = line_count
                continue
            if symbols[0] in self.instructions_by_name:
                instruction = self.instructions_by_name[symbols[0]]
                if len(symbols) != instruction.LENGTH:
                    raise('{} length is {} but symbols are {}'. format(
                        instruction.name,
                        instruction.LENGTH,
                        symbols
                    ))
                symbols[0] = instruction.opcode
                line_count += instruction.LENGTH

        for row in row_list:
            row = row.replace(' ', '')
            symbols = row.split(',')
            if ';' in symbols[0]:
                continue
            if '=' in symbols[0]:
                continue
            if ':' in symbols[0]:
                continue
            if symbols[0] in self.instructions_by_name:
                instruction = self.instructions_by_name[symbols[0]]
                symbols[0] = instruction.opcode
            for symbol in symbols:
                if symbol in variable_dict:
                    symbol = variable_dict[symbol]
                contents_list.append(int(symbol))
        self.memory.load(contents_list)

    def get_all_registers_contents(self):
        return {r.name: r.get_contents() for r in self.registers}

    def copy_current_state_values_into_dict(self):
        state_copy = self.get_all_registers_contents()

        for i, contents in enumerate(self.memory.dump()):
            state_copy[i] = contents

        return state_copy

    def compare_state_copies(self, old, new):
        changes = {}
        for component in old:
            if old[component]  != new[component]:
                changes[component] = (old[component], new[component])
        return changes
