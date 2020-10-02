from base import MicrocodeBase

class Load(MicrocodeBase):

    def action(self, value=None):
        if not value:
            value = self.get_component_contents(self.components[1])
        self.set_component_contents = value

