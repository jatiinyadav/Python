
from array import * 
arr = array('i',[])

n = int(input("Enter the length of array"))

for i in range(n):
    x = int(input("Enter the next value"))
    arr.append(x)                               # append means ki humein x main se value leke arr main dalni hai 
print(arr)

val = int(input("Enter the value to be searched"))

#method one 
k = 0
for e in arr:
    if e == val:
        print(k)
        break
    k += 1

# method two
print(arr.index(val))
