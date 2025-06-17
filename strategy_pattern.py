class Operation:
    def execute(self, a, b):
        pass

class Add(Operation):
    def execute(self, a, b):
        return a + b

class Subtract(Operation):
    def execute(self, a, b):
        return a - b

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, a, b):
        return self.strategy.execute(a, b)

context = Context(Add())
print("Add:", context.execute_strategy(5, 3))

context = Context(Subtract())
print("Subtract:", context.execute_strategy(5, 3))
