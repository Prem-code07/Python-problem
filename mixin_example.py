class LoggingMixin:
    def log(self, message):
        print(f"Log: {message}")

class Worker(LoggingMixin):
    def work(self):
        self.log("Working hard...")

w = Worker()
w.work()
