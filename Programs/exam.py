for i in range (1,10,2):
    for j in range (i):
        print(i, end="")
    print()

print("----------")

count = 4

while True:
    print(count)
    count += 2
    if (count >= 12):
        break

print("----------")

for i in range (1,10):
    if (i%2!=0):
        print(i)
        continue

print("----------")

count = 5

while count<=10:
    print("Inside while", count)
    count += 1

else:
    print("Outside while", count)

print("----------")

low = int(input("Enter lower range: "))
upp = int(input("Enter upper range: "))
for n in range(low, upp + 1):
    print(n)

print("----------")

for i in range(1,25,5):
    print(i)

print("----------")


def square(x):
    print(x*x)

square(5)

print("----------")

x = 1
while x < 4:
    x+=1
    y = 1
    while y < 3:
        print(y, end="")
        y += 1

list = [1,2,3,4,5]

del list[0:2]
print(list)

print("----------")

list1 = [1,2,3,4,5]
list1 = [x + 10 for x in list1]

print(list1)

print("----------")

set1 = set([1,2,3,4,6])
set2 = set([6,7,8,9,10])

union = set1 | set2 
print(union)
intersection = set1 & set2
print(intersection)
difference = set1 - set2
print(difference)

number = input("Enter something: ")
print(number.isdigit())
print(number.isalpha())
