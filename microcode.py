from base import InstructionBase


class LDRV(InstructionBase):
    '''
    Load value into specified register
    '''
    LENGTH = 2

    def run(self):
        value = self.get_memory_location_contents_and_inc_pc()
        self.components[0].set_contents(value)


class LDRR(InstructionBase):
    '''
    Load contents from register 1 to register 0
    '''
    LENGTH = 1

    def run(self):
        value = self.components[1].get_contents()
        self.components[0].set_contents(value)


class LDRM(InstructionBase):
    '''
    Load memory location value into specified register
    '''
    LENGTH = 2

    def run(self):
        address = self.get_memory_location_contents_and_inc_pc()
        value = self.memory.get_contents_value(address)
        self.components[0].set_contents(value)


class LDMR(InstructionBase):
    '''
    Load register into memory location
    '''
    LENGTH = 2

    def run(self):
        address = self.get_memory_location_contents_and_inc_pc()
        value = self.components[0].get_contents()
        self.memory.set_contents_value(address, value)


class LDIMRV(InstructionBase):
    '''
    Load memory location specified in register with value
    '''
    LENGTH = 2

    def run(self):
        value = self.get_memory_location_contents_and_inc_pc()
        address= self.components[0].get_contents()
        self.memory.set_contents_value(address, value)


class LDIMRR(InstructionBase):
    '''
    Load memory location specified in register 1 with value in register 2
    '''
    LENGTH = 1

    def run(self):
        address= self.components[0].get_contents()
        value= self.components[1].get_contents()
        self.memory.set_contents_value(address, value)


class LDIRRM(InstructionBase):
    '''
    Load register 1 with value in memory location specified by register 2
    '''
    LENGTH = 1

    def run(self):
        address = self.components[1].get_contents()
        value = self.memory.get_contents_value(address)
        self.components[0].set_contents(value)


class GTRR(InstructionBase):
    '''
    Compare two registers - if first > second then set third component to 1, else 0
    '''
    LENGTH = 1

    def run(self):
        if self.components[0].get_contents() > self.components[1].get_contents():
            self.components[2].set_contents(1)
        else:
            self.components[2].set_contents(0)


class LTRR(InstructionBase):
    '''
    Compare two registers - if first < second then set third component to 1, else 0
    '''
    LENGTH = 1

    def run(self):
        if self.components[0].get_contents() < self.components[1].get_contents():
            self.components[2].set_contents(1)
        else:
            self.components[2].set_contents(0)


class EQRR(InstructionBase):
    '''
    Compare two registers - if first == second then set third component to 1, else 0
    '''
    LENGTH = 1

    def run(self):
        if self.components[0].get_contents() == self.components[1].get_contents():
            self.components[2].set_contents(1)
        else:
            self.components[2].set_contents(0)


class JMPV(InstructionBase):
    '''
    Jump to address - either immediate or check if specified register/flag is not zero
    '''
    LENGTH = 2

    def run(self):
        address = self.get_memory_location_contents_and_inc_pc()
        if self.components:
            if not self.components[0].get_contents():
                return
        self.program_counter.set_contents(address)


class JMNV(InstructionBase):
    '''
    Jump to address - either immediate or check if specified register/flag is zero
    '''
    LENGTH = 2

    def run(self):
        address = self.get_memory_location_contents_and_inc_pc()
        if self.components:
            if self.components[0].get_contents():
                return
        self.program_counter.set_contents(address)


class JMPR(InstructionBase):
    '''
    Jump to address specified in register - either immediate or check if specified register/flag is set
    '''
    LENGTH = 1

    def run(self):
        address = self.components[0].get_contents()
        if len(self.components) == 2:
            if not self.components[1].get_contents():
                return
        self.program_counter.set_contents(address)


class JMNR(InstructionBase):
    '''
    Jump to address specified in register - either immediate or check if specified register/flag is zero
    '''
    LENGTH = 1

    def run(self):
        address = self.components[0].get_contents()
        if len(self.components) == 2:
            if self.components[1].get_contents():
                return
        self.program_counter.set_contents(address)


class INCR(InstructionBase):
    '''
    Add 1 to specified register
    '''
    LENGTH = 1

    def run(self):
        carry_flag = self.components[0].add_to_contents(1)
        self.components[1].set_contents(carry_flag)


class ADDRR(InstructionBase):
    '''
    Add specified register to specified register
    '''
    LENGTH = 1

    def run(self):
        carry_flag = self.components[0].add_to_contents(self.components[1].get_contents())
        self.components[2].set_contents(carry_flag)


class DECR(InstructionBase):
    '''
    Subtract 1 from specified register
    '''
    LENGTH = 1

    def run(self):
        carry_flag = self.components[0].subtract_from_contents(1)
        self.components[1].set_contents(carry_flag)


class SUBRR(InstructionBase):
    '''
    Subtract specified register from specified register
    '''
    LENGTH = 1

    def run(self):
        carry_flag = self.components[0].subtract_from_contents(self.components[1].get_contents())
        self.components[2].set_contents(carry_flag)
    

class PUSHR(InstructionBase):
    '''
    Push register contents onto stack
    '''
    LENGTH = 1

    def run(self):
        value = self.components[0].get_contents()
        self.memory.set_contents_value(self.program_counter.get_contents(), value)
        self.program_counter.set_contents(self.program_counter.get_contents() - 1)

class POPR(InstructionBase):
    '''
    Pop top of stack into register
    '''
    LENGTH = 1

    def run(self):
        stack_head = self.program_counter.get_contents() + 1
        value = self.memory.get_contents_value(stack_head)
        self.components[0].set_contents(value)
        self.program_counter.set_contents(stack_head)

class CALLV(InstructionBase):
    '''
    Push address of next instruction on stack then jump to address - either immediate or check if specified register/flag is not zero
    '''
    LENGTH = 2

    def run(self):
        address = self.get_memory_location_contents_and_inc_pc()
        if self.components:
            if not self.components[0].get_contents():
                return
        self.memory.set_contents_value(self.stack_pointer.get_contents(), self.program_counter.get_contents())
        self.stack_pointer.set_contents(self.stack_pointer.get_contents() - 1)
        self.program_counter.set_contents(address)

class CALNV(InstructionBase):
    '''
    Push address of next instruction on stack then jump to address - either immediate or check if specified register/flag is zero
    '''
    LENGTH = 2

    def run(self):
        address = self.get_memory_location_contents_and_inc_pc()
        if self.components:
            if self.components[0].get_contents():
                return
        self.memory.set_contents_value(self.stack_pointer.get_contents(), self.program_counter.get_contents())
        self.stack_pointer.set_contents(self.stack_pointer.get_contents() - 1)
        self.program_counter.set_contents(address)


class RET(InstructionBase):
    '''
    Set program counter with address popped from stack - either immediate or check if specified register/flag is not zero
    '''
    LENGTH = 1

    def run(self):
        if self.components:
            if not self.components[0].get_contents():
                return
        stack_head = self.stack_pointer.get_contents() + 1
        address = self.memory.get_contents_value(stack_head)
        self.stack_pointer.set_contents(stack_head)
        self.program_counter.set_contents(address)
