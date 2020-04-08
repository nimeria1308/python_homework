class SchoolMember(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super().__init__(name, age)

        self.salary = salary

        # Courses that they teach
        self.courses = { }

    def getSalary(self):
        return self.salary

    def addCourse(self, signature, name):
        self.courses[signature] = name

    def getCourses(self):
        for signature, name in self.courses.items():
            print("%s %s" % (signature, name))

class Student(SchoolMember):
    # no need to define ctr as it matches parent's
    def __init__(self, name, age):
        super().__init__(name, age)

        # Attended courses
        self.courses = { }

    def attendCourse(self, signature, year):
        self.courses[signature] = {
            "grade": [ ],
            "year": year,
        }

    def addGrade(self, signature, grade):
        if signature in self.courses:
            self.courses[signature]["grade"].append(grade)

    def getCourses(self):
        for signature, course in self.courses.items():
            print("%s %s" % (signature, course))

    def getAvgGrade(self, signature):
        grades = self.courses[signature]["grade"]
        return sum(grades) / len(grades)
