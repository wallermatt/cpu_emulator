

class ComponentBase:

    def __init__(self, name):
        self.name = name
        self.contents = 0

    def get_name(self):
        return self.name

    def get_contents(self):
        return self.contents

    def set_contents(self, value):
        self.contents = value


class MemoryBase(ComponentBase):

    def __init__(self, name, size):
        self.name = name
        self.contents = [ComponentBase("address: {}".format(e)) for e in range(size)]

    def get_contents(self, address):
        return self.contents[address]

    def get_contents_value(self, address):
        return self.contents[address].get_contents()

    def set_contents_value(self, address, value):
        self.contents[address].set_contents(value)

    def dump(self):
        return [e.get_contents() for e in self.contents]


class Component:

    MAX_VALUE = 256

    def __init__(self, name):
        self.name = name
        self.contents = 0

    def get_name(self):
        return self.name

    def get_contents(self):
        return self.contents

    def set_contents(self, value):
        self.contents = value

    def add_to_contents(self, value):
        carry_flag = 0
        result = self.contents + value
        if result >= self.MAX_VALUE:
            result = result % self.MAX_VALUE
            carry_flag = 1
        self.contents = result
        return carry_flag



class Memory:

    def __init__(self, size):
        self.contents = [ComponentBase("address: {}".format(e)) for e in range(size)]

    def get_contents(self, address):
        return self.contents[address]

    def get_contents_value(self, address):
        return self.contents[address].get_contents()

    def set_contents_value(self, address, value):
        self.contents[address].set_contents(value)

    def dump(self):
        return [e.get_contents() for e in self.contents]

    def load(self, data):
        for address,value in enumerate(data):
            self.contents[address].set_contents(value)



class InstructionBase:

    def __init__(self, name, opcode, memory, program_counter, components=None):
        self.name = name
        self.opcode = opcode
        self.memory = memory
        self.program_counter = program_counter
        self.components = components

    def get_memory_location_contents_and_inc_pc(self):
        pc_value = self.program_counter.get_contents()
        contents = self.memory.get_contents_value(pc_value)
        self.program_counter.set_contents(pc_value + 1)
        return contents

    def run(self):
        pass


