# Abstract class

# Abstract Method, in a method where we have nothing in the method and we use pass

from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):

    def process(self):
        print("Its running: ")


class Programmer:
    def work(self, com):
        print("Solving bugs")
        com.process()


com1 = Laptop()

# com = Computer()

com1.process()
prog1 = Programmer()
prog1.work(com1)


print("---------")


class Animal(ABC):

    def move(self):
        pass


class Human(Animal):

    def move(self):
        print("I can walk and run")


class Snake(Animal):

    def move(self):
        print("I can crawl")


class Dog(Animal):

    def move(self):
        print("I can bark")


class Lion(Animal):

    def move(self):
        print("I can roar")


# Driver code
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()
