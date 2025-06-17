class Light:
    def turn_on(self):
        print("Light is ON")

class LightOnCommand:
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

light = Light()
command = LightOnCommand(light)
command.execute()
