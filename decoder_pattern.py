class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 2

coffee = Coffee()
print("Plain Coffee Cost:", coffee.cost())

milk_coffee = MilkDecorator(coffee)
print("Milk Coffee Cost:", milk_coffee.cost())
