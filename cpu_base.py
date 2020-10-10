class CPUBase:

    def __init__(self, memory, program_counter, registers, instructions):
        self.memory = MemoryBase(memory['name'])
        self.program_counter = program_counter
        self.registers = registers
        # self.instructions = instructions