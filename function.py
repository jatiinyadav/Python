def greet():
    print("Hello")

greet()

print("------")

def add_sub(x,y):
    c = x + y 
    d = x - y
    return c,d 

r1, r2 = add_sub(4,5)
print(r1, r2)


print("------")


def sum(**three):
    
    for i,j in three.items():
        print(i,j)

sum(Name = "'Jatin'", Age = 19, Address = "Delhi")



# def odd_even(odd, even):

#     lst[0] = 9
#     print("L1: ",lst)

# lst = [1,2,3,4,5,6]    
# odd_even()
# print("Even and odd are: ", odd)

x = int(input("Enter a number: \n"))

def odd_even(x):
    if x%2==0:
        print(str(x) +  " is even.")
    else:
        print(str(x) + " is odd.")

odd_even(x)

list4 = [1,2,3,4,5,6]

even = 0
odd = 0

for i in list4:
    if i%2==0:
        even+=1
    else:
        odd+=1
    
print("Even numbers are: ", str(even)  +  " and odd numbers are: ", str(odd))


def count(lst):

    even = 0
    odd = 0

    for i in lst:
        if i %2==0:
            even+=1
        else:
            odd+=1
            
    return odd, even


lst = [1,2,3,4]
even, odd = count(lst)

print("EVEN: {} and ODD: {} " .format(odd,even))