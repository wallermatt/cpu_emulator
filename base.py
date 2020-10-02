

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
        self.contents = [ComponentBase('address: %s'.format(e)) for e in range(size)]

    def get_contents(self, address):
        return self.contents[address]

    def get_contents_value(self, address):
        return self.contents[address].get_contents

    def set_contents_value(self, address, value):
        self.contents[address].set_contents = value


class MicrocodeBase:

    def __init__(self, name, components):
        self.name = name
        self.components = components

    def action(self):
        pass

    def get_component_contents(self, component):
        return component.get_contents

    def set_component_contents(self, component, value):
        component.set_contents = value
