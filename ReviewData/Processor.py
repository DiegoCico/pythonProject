import csv
import matplotlib.pyplot as plt

class Processor:
    """
    Processor class to create visualizations from a CSV file.
    """
    def __init__(self, src):
        """
        Initialize the Processor with a source CSV file.
        """
        self.src = src

    def createScatterChart(self, label_col="", value_col=""):
        """
        Create a scatter chart from specified columns.
        """
        x, y = self._prepare_chart_data(0, 1)
        plt.scatter(y, x)
        plt.xlabel(f'{label_col}')
        plt.ylabel(f'{value_col}')
        plt.show()

    def createPIChart(self):
        """
        Create a pie chart from specified columns.
        """
        labels, values = self._prepare_chart_data(0, 1)
        plt.pie(values, labels=labels, autopct='%1.1f%%')
        plt.show()

    def createBarChart(self, label_col="", value_col=""):
        """
        Create a bar chart from specified columns.
        """
        labels, values = self._prepare_chart_data(0, 1)
        plt.bar(labels, values)
        plt.xlabel(f'{label_col}')
        plt.ylabel(f'{value_col}')
        plt.show()

    def readCol(self, col):
        """
        Read a column from the CSV file, handling potential errors.
        """
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

    def _prepare_chart_data(self, label_col, value_col):
        """
        Helper method to prepare data for charting.
        """
        plt.figure(figsize=(5, 5))
        labels = self.readCol(label_col)
        values = self.readCol(value_col)
        return labels, values
