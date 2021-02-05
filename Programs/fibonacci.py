x = int(input("Till where you want the Fibonacci series?\n"))

def fib(x):

    a = 0
    b = 1

    if (x<=0):
        print("N0. should be >= 1")
    elif(x==1):
        print(a)
    else:
        print(a)
        print(b)
        for i in range(1,x):
            c = a + b
            a = b
            b = c
            if c > 100:
                break
            print(c)

fib(x)