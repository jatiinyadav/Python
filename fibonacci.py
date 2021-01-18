x = int(input("Till where you want the Fibonacci series?\n"))

def fib(n):

    a = 0
    b = 1

    if (n<=0):
        print("N0. should be >= 1")
    elif(n==1):
        print(a)
    else:
        print(a)
        for i in range(1,n):
            c = a + b
            a = b
            b = c
            if c > 100:
                break
            print(c)

fib(x)