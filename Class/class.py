class Computer:

    def __init__(self):
        self.name_cpu = "Jatin"
        self.age = 19

    def compare(self, comp2):

        self = int(input("Enter age for comp1:  "))
        comp2 = int(input("Enter age for comp2:  "))

        if self == comp2:
            return True
        else:
            return False


comp1 = Computer()
comp2 = Computer()

if comp1.compare(comp2):
    print(" Age is same. ")

else:
    print(" Age is different. ")
