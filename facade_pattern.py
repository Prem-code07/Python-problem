class CPU:
    def start(self):
        print("CPU started")

class HardDrive:
    def read(self):
        print("HardDrive read")

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.hd = HardDrive()

    def start_computer(self):
        self.cpu.start()
        self.hd.read()

computer = ComputerFacade()
computer.start_computer()
