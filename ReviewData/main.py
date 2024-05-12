from ReviewData.Processor import Processor

def menu():
    """Display the menu options."""
    print("----------------------")
    print("📊 A. Pie Chart")
    print("📈 B. Bar Chart")
    print("🌟 C. Scatter Chart")
    print("❌ E. Exit")
    print("----------------------")

while True:
    src = input("Hey there! Welcome to our Data Visualization Tool! \nWhat's the name of your data file? (Type 'E' to exit)\n")
    if src.upper() == 'E':
        print("Thank you for using our Data Visualization Tool! Have a fantastic day!")
        break

    processor = Processor(src)

    print("Fantastic! What would you like to do?")
    menu()
    userInput = input("Type the letter corresponding to your choice (or 'E' to exit): ")

    if userInput.upper() == "E":
        print("Thank you for using our Data Visualization Tool! Have a fantastic day!")
        break
    elif userInput.upper() == "A":
        processor.createPieChart()
    elif userInput.upper() == "B":
        col = input("🚀 Awesome! Please enter the label for the X-axis: ")
        row = input("🎉 Great choice! Now, what should we label the Y-axis? ")
        processor.createBarChart(col, row)
    elif userInput.upper() == "C":
        X = input("🎨 Exciting! What label would you like for the X-axis? ")
        Y = input("✨ Wonderful! And how about the Y-axis? ")
        processor.createScatterChart(X, Y)
