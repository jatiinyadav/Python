# function arguments
def update(list1,list2):
    print(id(list1))
    list1[2] = 4
    list2[2] = 9
    print(id(list2))
    print("L1: ",list1)
    print("L2: ",list2)


list1 = [1,3,5,7]
list2 = [2,4,6,8]
print(id(list1))
update(list1,list2)
print("list1: ",list1)
print("list2: ",list2)