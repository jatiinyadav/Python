# pass list in a function

n = int(input("Enter the no. of elements you want in the list: "))

def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
            print(i, "EVEN")
        else: 
            odd += 1
            print(i, "ODD")
    return even,odd
lst = []

for i in range(1,n):
    app = int(input("Enter the "+ str(i)+ " no. "))
    lst.append(app)
even, odd = count(lst)
# print("There are " + str(even) + " even no ")
# print("There are " + str(odd) + " odd no ")
print("There are {} Even no. and {} Odd no.".format(even,odd))