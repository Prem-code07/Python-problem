class Flyweight:
    def __init__(self, shared_state):
        self.shared_state = shared_state

    def operation(self, unique_state):
        print(f"Shared: {self.shared_state}, Unique: {unique_state}")

class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, shared_state):
        if shared_state not in self._flyweights:
            self._flyweights[shared_state] = Flyweight(shared_state)
        return self._flyweights[shared_state]

factory = FlyweightFactory()
fw1 = factory.get_flyweight("A")
fw2 = factory.get_flyweight("A")

fw1.operation("X")
fw2.operation("Y")
