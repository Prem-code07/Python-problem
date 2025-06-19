class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class PetFactory:
    def get_pet(self):
        pass

class DogFactory(PetFactory):
    def get_pet(self):
        return Dog()

class CatFactory(PetFactory):
    def get_pet(self):
        return Cat()

def get_factory(animal="Dog"):
    factories = {"Dog": DogFactory(), "Cat": CatFactory()}
    return factories[animal]

factory = get_factory("Cat")
pet = factory.get_pet()
print(pet.speak())
