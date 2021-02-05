class Car:

    wheels = 4                          # Class (Static) Variables before __init__                

    def __init__(self):
        self.com = "BMW"                # Instance Variables inside __init__
        self.mil = "10"

c1 = Car()
c2 = Car()

Car.wheels = 5                          # The value of all the wheels is now 5

# c1.wheels = 10                        # For individual changes 
# c2.wheels = 15

print(c1.com, c1.mil, c1.wheels)        # print(c1.com, c1.mil, Car.wheels) 
print(c2.com, c2.mil, c2.wheels)        #  print(c1.com, c1.mil, Car.wheels) 