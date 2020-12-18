from array import *     #here * means to include all the functions of array

vals = array('i',[3,5,7,9])
vals.reverse()

for i in vals:
    print(i)

print("-------")

vals = array('i',[2,5,4])

for i in range(len(vals)):
    print(vals[i])
  
print("-------")

#till here on git hub


val = array('i', [5,4,3,2])
newArr = array(val.typecode, (a*a for a in val))

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