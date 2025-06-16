class MyClass:
    def __init__(self):
        self.__private_var = 10

    def __private_method(self):
        print("Private Method")

    def access_private(self):
        print(self.__private_var)
        self.__private_method()

obj = MyClass()
obj.access_private()
