class State:
    def handle(self):
        pass

class StartState(State):
    def handle(self):
        print("Starting...")

class StopState(State):
    def handle(self):
        print("Stopping...")

class Context:
    def set_state(self, state):
        self.state = state

    def request(self):
        self.state.handle()

context = Context()
context.set_state(StartState())
context.request()

context.set_state(StopState())
context.request()
