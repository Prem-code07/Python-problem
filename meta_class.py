class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['class_name'] = name
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

print(MyClass.class_name)
