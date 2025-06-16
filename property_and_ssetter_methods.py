class MyClass:
    def __init__(self):
        self._x = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

obj = MyClass()
obj.x = 5
print(obj.x)
