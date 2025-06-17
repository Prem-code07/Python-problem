class RealSubject:
    def request(self):
        print("RealSubject: Handling request.")

class Proxy:
    def __init__(self):
        self.real_subject = RealSubject()

    def request(self):
        print("Proxy: Checking access...")
        self.real_subject.request()

p = Proxy()
p.request()
