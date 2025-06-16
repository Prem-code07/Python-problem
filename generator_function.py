class MyClass:
    def generator(self, n):
        for i in range(n):
            yield i

obj = MyClass()
for value in obj.generator(3):
    print(value)
