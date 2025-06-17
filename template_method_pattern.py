class DataProcessor:
    def process(self):
        self.read_data()
        self.process_data()

    def read_data(self):
        pass

    def process_data(self):
        pass

class CSVDataProcessor(DataProcessor):
    def read_data(self):
        print("Reading CSV data")

    def process_data(self):
        print("Processing CSV data")

processor = CSVDataProcessor()
processor.process()
