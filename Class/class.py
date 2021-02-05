class Computer:

    def __init__(self):
        self.name_cpu = "Jatin"
        self.age = 19

    def compare(self,comp2):
        
        self.age = int(input("Enter age for comp1:  "))
        comp2.age = int(input("Enter age for comp2:  "))

        if self.age == comp2.age:
            return True
        else: 
            return False
        

comp1 =  Computer()
comp2 =  Computer()

if comp1.compare(comp2):
    print( " Age is same. " )

else:
    print(" Age is different. " )