from ReviewData.Processor import Processor

def menu():
    print("----------------------")
    print("A. Pie Chart")
    print("B. Bar Chart")
    print("C. Scatter Chart")
    print("D. Histogram Chart")
    print("E. Exit")
    print("----------------------")

src = input("What is the source file? \n")
processor = Processor(src)

print("What would you like to do?")
menu()
userInput = input()
if userInput.upper() == "A":
    processor.createPIChart()
