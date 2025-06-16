class MyClass:
    class_var = "Class Variable"

    def __init__(self, instance_var):
        self.instance_var = instance_var

obj = MyClass("Instance Variable")
print(MyClass.class_var)
print(obj.instance_var)
