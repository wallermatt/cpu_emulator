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

