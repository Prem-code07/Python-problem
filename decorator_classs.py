class MyClass:
    @staticmethod
    def decorator(func):
        def wrapper():
            print("Before function")
            func()
            print("After function")
        return wrapper

    @decorator
    def say_hello():
        print("Hello")

MyClass.say_hello()
