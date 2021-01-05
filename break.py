#

print("----------")


av = 3 
x = int(input("Enter the no. of candies you want?\n"))
i = 1
for i in range(x):
    if (x <= av ):
       print("Candy")
    else:
        print("Sorry, we only have " + str(av) + "  no. of candies")
        break
print("Have a great day ahead")


print("----------")


lit = [2,5,6,9]
for i in lit:
    if (i%2==0):
        print(i, "Even")
    else:
        print(i, "Odd")

print("----------")


av = 3 
candy = int(input("Enter The no. of candies you want?\n"))
i = 1
for i in range(candy):
    if (candy<=av):
        if (candy%2==0):
            print("Here are your even no. of candies")
        else:
            print("Here are your odd no. of candies")
    else:
        print("Sorry, we only have " + str(av) + "  no. of candies")
        break
print("Have a great day ahead")