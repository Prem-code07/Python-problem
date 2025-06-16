class Point:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Point(self.x + other.x)

p1 = Point(1)
p2 = Point(2)
result = p1 + p2
print(result.x)
