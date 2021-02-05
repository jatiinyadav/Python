import array as array

arr = array.array('i',[])

print(type(arr))

n = int(input("Enter the length of array: "))

for i in range(n):
    x = int(input("Enter the value for "+  str(i) + " : "))
    arr.append(x*x)                                                       # append means ki humein x main se value leke arr main dalni hai 
print(arr)

val = int(input("Enter the value to be searched: "))

print("The index of " + str(val) + " is " +  str(arr.index(val)))