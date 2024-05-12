import csv
import matplotlib.pyplot as plt

class Processor:
    def __init__(self, src):
        self.src = src

    def createPIChart(self):
        plt.figure(figsize=(5, 5))
        labels = self.readCol(0)
        values = self.readCol(1)
        plt.pie(values, labels=labels, autopct='%1.1f%%')
        plt.show()

    def readCol(self, col):
        try:
            with open(self.src) as csvfile:
                csv_reader = csv.reader(csvfile)
                return [row[col] for row in csv_reader if row]
        except FileNotFoundError:
            print(f"Error: The file {self.src} does not exist.")
            return []
        except IndexError:
            print("Error: Column index out of range.")
            return []