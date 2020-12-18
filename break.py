#
av = 3 
x = int(input("Enter the no. of candies you want?\n"))
i = 1
for i in range(x): 
    if (x <= av):
       print("Candy")
        i+= 1 
    else:
        print("Sorry, we only have " + str(av) + "  no. of candies")
        break
print("Have a great day ahead")


print("----------")


lit = [2,4,5,6]
for i in lit:
    if (i%2==0):
        print(i, "Y")
    else:
        print(i, "N")

print("----------")