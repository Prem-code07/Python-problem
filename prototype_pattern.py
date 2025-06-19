import copy

class Prototype:
    def __init__(self):
        self.value = []

    def clone(self):
        return copy.deepcopy(self)

p1 = Prototype()
p1.value.append(10)

p2 = p1.clone()
p2.value.append(20)

print("Original:", p1.value)
print("Cloned:", p2.value)
