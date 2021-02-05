class Student:

    def __init__(self):
        self.name = input("Enter your name: ")
        self.rollno = int(input("Enter your roll no. : "))
        self.lap = self.Laptop

    def show(self):
        print("Your Name: {} \n Your Roll no. {} ".format(self.name, self.rollno))

    class Laptop:

        def __init__(self):
            self.brand = input("Brand: ")
            self.cpu = input("CPU: ")
            self.ram = int(input("RAM: "))

        def show(self):
            print("Your Brand: {} \n Your CPU: {} \n Your RAM: {} ".format(self.brand, self.cpu, self.ram))


s1 = Student()

lap = s1.Laptop()

s1.show()

Student().Laptop().show()

print(s1.show())
print(Student().Laptop().show())