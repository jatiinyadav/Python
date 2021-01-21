a = 5 // 2      #use double slash if you dont want to print float  number.
print(a)
print("-------")

b = 2 ** 3      #use ** to use power of. 
print(b)
print("-------")

print("Jatin\'s Lappy")     #use \ to include 's  
print("-------")

print(r"Lenovo/n sjss")     #use (r) to print same as it is in " ".
print("-------")

myname = ("Jatin Yadav")
print(len(myname))          # use length to calculate no.
print("-------")

#list

num = [2,4,7,9]
print(num[1])       #output will be 4.

num.insert(2,44)
print(num)          #(2,44) 2 is the place where you want to add any no, in this case its 44.

del num[2:]         #use del to delete numbers in list.
print(num)
print("-------")

name = ["Jatin","Yadav","Jatin", "Python"]
num = list(range(3))

print(name.count("Jatin"))

(name.insert(0,"Heyy"))

print(name)

(name.remove("Jatin"))

print(name)

(name.pop(1))

print(name)

num.extend([3,4,5,6,7,8,9,10])

print(num)

num.pop()

print(num)

num.reverse()

print(num)

num.sort()

print(num)

num.append(2)

print(num)

num.insert(0,"Hey")

print(num)

num.copy()

print(num)

num = [1,2,3,4,5,6,7,8,9,10]

print(min(num))

print(max(num))

print(sum(num))


num.clear()

print(num)

#tuple

tup = (2,4,6)           #in tuple value cannot be changed
print(tup)
print("-------")

print(tup.count(2))



#set

set = {2,3,4,5}           # in set value can be changed
print(set)


#dictionary

data = (2,4,6,7)
values = ('Hello, ','I am','Jatin','Yadav')
showDict = dict(zip(data,values))
print(showDict)

print(showDict.keys())

print(showDict.values())

print(showDict[2])

del showDict[2]

print(showDict)


say = list(range(10))

print(say)

say.pop()

print(say)