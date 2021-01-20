import sys
sys.setrecursionlimit(20)

print(sys.getrecursionlimit())



i = 0


def greet():


    global i
    i += 1

    print("Hello, World!!", i)

    greet()


greet()