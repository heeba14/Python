class Student:
    'Common base class for all Students'
    stdCount = 0
    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.stdCount += 1

    def displayCount(self):
        print("Total Students %d" % Student.stdCount)

    def displayStudent(self):
        print("Name : ", self.name, ", Score: ", self.score)


#Class Instance
std1 = Student("Heeba", 80)
std2 = Student("Ruzeena", 85)
std1.displayStudent()
std2.displayStudent()
print("Total Students %d" % Student.stdCount)
print("Doc Name:", Student.__doc__)
print("Class Name:", Student.__name__)
print("Module Name:", Student.__module__)