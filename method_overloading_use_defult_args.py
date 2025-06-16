class MyClass:
    def show(self, a=None, b=None):
        if a and b:
            print(a, b)
        elif a:
            print(a)
        else:
            print("No arguments")

obj = MyClass()
obj.show()
obj.show(1)
obj.show(1, 2)
