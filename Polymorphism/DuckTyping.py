class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")


class MyEditor:

    def execute(self):
        print("Numbers")
        print("Colors")
        print("Compiling")
        print("Running")


class Laptop:

    def code(self, ide):
        idee.execute()

idee = MyEditor()

lap1 = Laptop()

lap1.code(idee)


print("----------------")

class Bird: 
    def fly(self): 
        print("Fly with wings") 
  
class Airplane: 
    def fly(self): 
        print("Fly with fuel") 
  
class Fish: 
    def swim(self): 
        print("Fish swim in sea") 
  
# Attributes having same name are 
# considered as duck typing 
for obj in Bird(), Airplane(), Fish(): 
    obj.fly() 