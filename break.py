print("----------")

say = list(range(1,4))

for i in say:
    if i%2==0:
        print("Even")
        continue
    else:
        print("Odd")
        continue


print("----------")


av = 10
candy = int(input("Enter The no. of candies you want?\n"))
i = 1
for i in range(1,candy+1):
    if (candy<=av):
        if (candy%2==0):
            print(i, " no. of Candies")
        else:
            print(i, " no. of Candies")
    else:
        print("Sorry, we only have " + str(av) + " candies")
        break
print("Have a great day ahead")


print("----------")