class Computer:

    def __init__(self):
        self.name_cpu = "Jatin"
        self.age = 19


    def config(self):

        name_cpu1 = input("Enter your name for config: ")
        name_ram1 = input("Enter your age for config: ")
        print("The name for config is:  " + name_cpu1 + " and age is: " + name_ram1 )

    def config2(self):

        name_cpu2 = input("Enter your name for config2: ")
        name_ram2 = input("Enter your age for config2: ")
        print("The name for config2 is:  " + name_cpu2 + " and age is: " + name_ram2 )

    def compare(self,comp2):
        
        self.age = int(input("Enter age for comp1:  "))
        comp2.age = int(input("Enter age for comp2:  "))

        if self.age == comp2.age:
            return True
        else: 
            return False
        

comp1 =  Computer()
comp2 =  Computer()

comp1.config()
comp2.config2()

if comp1.compare(comp2):
    print( " Age is same. " )

else:
    print(" Age is different. " )
#  Computer.config(comp1)   