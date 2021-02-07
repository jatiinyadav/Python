"r is read"
"w is write"
"a is append"

file = open("Handling/data.py",'r')

# print(file.readline())
# print(file.readline())
# print(file.readline())

file2= open("Handling/see.py",'w')

for i in file:
    file2.write(i)

# file.write(" I'm \n an \n iPhone \n user")

# use rb and wb for read binary and write binary