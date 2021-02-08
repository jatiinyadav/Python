pos = 0

numb = int(input("Enter the number you want a list of: "))

def search(list, n):

    for i in range(len(list)):

        if list[i] == n:
            globals()['pos'] = i
            return True

    else:
        return False

list = []

for i in range(1, numb + 1):
    elements = int(input("Enter number for index {}: ".format(i)))
    list.append(elements)

n = int(input("Enter the number you want to search: "))

if search(list,n):
    print("Found at index:", pos + 1)
else:
    print("Not found")
