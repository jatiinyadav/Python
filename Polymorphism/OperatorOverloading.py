class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + self.m2
        m2 = other.m1 + other.m2
        s3 = Student(m1,m2)

        return s3

    def __gt__(self,other):
        grt1 = self.m1 + self.m2
        grt2 = other.m1 + other.m2
        
        if grt1 > grt2:
            return True
        else:
            return False

    def __str__(self):
        return "Marks are {} {}".format(self.m1, self.m2)

    # def show(self):
    #     print("Marks are {} {}".format(self.m1, self.m2))

s1 = Student(10,20)
s2 = Student(30,40)

s3 = s1 + s2

print(s3.m1)
print(s3.m2)


# s1.show()
# s2.show()

print(s1)
print(s2)

if s1 > s2:
    print("Student 1 wins")
else:
    print("Student 2 wins")