import array as array

arr1 = array.array('i', [2, 4, 6, 8])

print(type(arr1))               #view() if you change arr1, arr2 will be changed and in copy() only that arr wil change in which you are making changes

arr2 = arr1

arr1[1] = 8 

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))


vals = array.array('i',[3,5,7,9])
vals.reverse()

print(vals.buffer_info())

print(vals)

for i in vals:
    print(i)


print("-------")

vals = array.array('i',[2,5,4])

for i in range(len(vals)):
    print(vals[i])
  
print("-------")


val = array.array('i', [5,4,3,2])
newArr = array.array(val.typecode, (a*a for a in val))

for e in newArr:        
    print(e)

print("-------")

vow = ['a','e','i','o','u']
add = vow.index('i')
print(" The index of i: "  , add)

print("-------")

Se = [1,2,3]
xS = [4,5,6]
Se.extend(xS)
print('USe of exStend: ', Se)

#python liSt 
#inSert, clear, append, add, pop, extend, index, count, copy, reverSe, Sort