class Coffee:
    def cost(self):
        return 5

class MilkDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 2

coffee = Coffee()
milk_coffee = MilkDecorator(coffee)
print("Cost:", milk_coffee.cost())
