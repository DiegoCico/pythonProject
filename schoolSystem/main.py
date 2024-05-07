import student
print("Welcome to the school system")
print("what would you like to do")
print()
r = ""

def showMenu():
    print("------------------------------")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. find smartest student")
    print("4. find student")
    print("5. Show all")
    print("6. exit")
    print("------------------------------")

while(r != "6"):
    showMenu()
    r = input()
    if r == "1":
        student.name.append(input("Name: "))
        student.age.append(input("age: "))
        student.gpa.append(float(input("gpa: ")))

    if r == "2":
        s = input("Name of the student: ")
        student.deleteStudent(s)

    if r =="3":
        student.smartStudent()

    if r == "4":
        s = input("Name of student: ")
        student.findStudent(s)

    if r == "5":
        student.allStudents()