name = []
age = []
gpa = []


def addStudent(n,a,g):
    global name
    global age
    global gpa
    name.append(n)
    age.append(int(a))
    gpa.append(float(g))


def deleteStudent(n):
    if name.index(n) != -1:
        i = name.index(n)
        name.pop(i)
        age.pop(i)
        gpa.pop(i)
        print("Student Deleted")
    else:
        print("Student Not Found")

def smartStudent():
    high = 0
    pos = -1
    for i in range(len(gpa)):
        if high<gpa[i]:
            pos = i
    print(name[i])
    print(age[i])
    print(gpa[i])

def findStudent(n):
    pos = -1
    for i in range(len(name)):
        if name[i] == n:
            pos = i

    print(name[i])
    print(age[i])
    print(gpa[i])


def allStudents():
    for i in range(len(age)):
        print("Name: " + name[i], end="")
        print("   Age: " + age[i], end="")
        print("   GPA: " + gpa[i], end="")
        print()


