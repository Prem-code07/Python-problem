class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        if self.successor:
            self.successor.handle(request)

class ConcreteHandler1(Handler):
    def handle(self, request):
        if request < 10:
            print("Handler1 handled", request)
        else:
            super().handle(request)

class ConcreteHandler2(Handler):
    def handle(self, request):
        if request < 20:
            print("Handler2 handled", request)
        else:
            super().handle(request)

h2 = ConcreteHandler2()
h1 = ConcreteHandler1(h2)

h1.handle(5)
h1.handle(15)
h1.handle(25)
