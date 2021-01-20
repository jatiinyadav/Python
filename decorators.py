a = int(input("Enter 1st no. "))
b = int(input("Enter 2nd no. "))

def div(a,b):
    print(a/b)

def smart_div(func):

    def inner(a,b):

        if a<b:
            a,b =b,a

        return func(a,b)

    return inner

div1 = smart_div(div)

div1(a,b)