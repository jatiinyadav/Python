a = int(input("Enter 1st no. "))
b = int(input("Enter 2nd no. "))

def div(a,b):
    print(a/b)

#changing the behaviour is called decorators 

def smart_div(function):

    def div(a,b):

        if a<b:
            a,b =b,a

        return function(a,b)

    return div

div1 = smart_div(div)

div1(a,b) 