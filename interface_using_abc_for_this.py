from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_data(self):
        pass

class Document(Printable):
    def print_data(self):
        print("Document data")

doc = Document()
doc.print_data()
