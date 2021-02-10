class Student:

    def __init__(self):
        self.name = input("Name: ")
        self.rollno = int(input("Roll no. : "))
        self.lap = self.Laptop()                            #Object created in inner class

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

s1.show()

s1.lap.show()

# If we dont want to declare in inner class then for outer class declare a new object

# lap1 = Student.Laptop()

# print(lap1.show())