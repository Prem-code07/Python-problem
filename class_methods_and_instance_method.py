class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    def display(self):
        print("Instance Method")

obj = MyClass()
print(MyClass.get_count())
obj.display()
