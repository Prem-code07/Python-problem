class Component:
    def show(self):
        pass

class Leaf(Component):
    def show(self):
        print("Leaf")

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, child):
        self.children.append(child)

    def show(self):
        for child in self.children:
            child.show()

leaf1 = Leaf()
leaf2 = Leaf()
composite = Composite()
composite.add(leaf1)
composite.add(leaf2)
composite.show()
