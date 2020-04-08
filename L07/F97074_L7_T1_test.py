from F97074_L7_T1 import Student, Teacher

def test1():
    A=Teacher('Andonov',30,3000)
    B=Student('Petrov',21)
    B.attendCourse('CSCB101',2013)
    B.getCourses()
    B.addGrade('CSCB101',3)
    B.addGrade('CSCB101',4)
    B.getCourses()
    print(B.getAvgGrade('CSCB101'))

def test2():
    teacher = Teacher("Georgi Atanasov", 45, 3120)
    teacher.addCourse("CITB331", "Python")
    teacher.addCourse("CSCB212", "OOP")

    student = Student("Maria Ivanova", 20)
    student.attendCourse("CITB331", 2020)
    student.attendCourse("CSCB212", 2018)
    student.addGrade("CITB331", 5)
    student.addGrade("CITB331", 6)
    student.addGrade("CITB331", 6)
    student.addGrade("CSCB212", 4)
    student.addGrade("CSCB212", 5)
    student.addGrade("CSCB212", 5)
    student.addGrade("CSCB212", 5)

    # this should not raise as per requirementss
    student.addGrade("1234", 5)

    print("Teacher %s (%d) %.2f BGN" % (teacher.getName(), teacher.getAge(), teacher.getSalary()))
    print("Teacher %s courses" % teacher.getName())
    teacher.getCourses()

    print("Student %s (%d)" % (student.getName(), student.getAge()))
    print("Student %s courses" % student.getName())
    print("Student %s has %.2f in %s" % (student.getName(), student.getAvgGrade("CITB331"), "CITB331"))
    print("Student %s has %.2f in %s" % (student.getName(), student.getAvgGrade("CSCB212"), "CSCB212"))

# test1()
test2()
