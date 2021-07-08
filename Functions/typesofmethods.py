# 1.  Instance Method
# 2.  Class Method
# 3.  Static Method

class Student:

    college = "ABESIT"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def marks_avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def getSchool(cls):
        return cls.college

    @staticmethod
    def info():
        print("My college is ABESIT")


m1 = int(input("Enter 1st Student marks: "))
m2 = int(input("Enter 2nd Student marks: "))
m3 = int(input("Enter 3rd Student marks: "))

s1 = Student(m1, m2, m3)

print("The average marks are: {} ".format(s1.marks_avg()))

print(Student.getSchool())

Student.info()
