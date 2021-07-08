# global keyword

# preference will be give 1st to local variable

a = 10
print(id(a))


def maggi():
    a = 9
    # x = globals()['a']
    # print(x)
    # print(id(x))
    print("In fun", a)
    globals()['a'] = 15


maggi()
print("Value of a:", a)


print("Outside: ", a)

print("------")

x = 10


def foo():
    x = 20

    def bar():
        x = 15
        print("value of bar: ", x)

        globals()['x'] = 18
        # global x
        # x = 25

    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)


foo()
print("x in main: ", x)

print("------")

a = 10


def hey():
    a = 10
    print("Inside hey", a)
    globals()['a'] = 20


print("Before caaling hey", a)
hey()
print("After caaling hey", a)
