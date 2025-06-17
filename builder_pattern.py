class Car:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def show(self):
        print("Car parts:", self.parts)

class CarBuilder:
    def build_body(self):
        return "Body"

    def build_engine(self):
        return "Engine"

car = Car()
builder = CarBuilder()
car.add(builder.build_body())
car.add(builder.build_engine())
car.show()
