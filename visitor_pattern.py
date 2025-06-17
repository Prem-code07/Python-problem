class Element:
    def accept(self, visitor):
        visitor.visit(self)

class ConcreteElement(Element):
    pass

class Visitor:
    def visit(self, element):
        print(f"Visited {element.__class__.__name__}")

e = ConcreteElement()
v = Visitor()
e.accept(v)
