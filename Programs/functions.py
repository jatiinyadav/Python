# def greet(first_name, last_name):
#     print(f' Hi, {first_name}  {last_name}')
#     print("Welcome To Python World!!")


# greet("Jatin", "Yadav")

import random

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)

        return(first, second)

ludo = Dice()
print(ludo.roll())


from pathlib import Path

path = Path("emails")
print(path.mkdir())  #rmdir to remove directory


