class MyClass:
    def __init__(self):
        self._protected_var = 20

    def _protected_method(self):
        print("Protected Method")

obj = MyClass()
print(obj._protected_var)
obj._protected_method()
