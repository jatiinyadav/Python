# function arguments
def update(list1,list2):
    list1[2] = 4
    list2[2] = 9
    print("L1: ",list1)
    print("L2: ",list2)


list1 = [1,3,5,7]
list2 = [2,4,6,8]
update(list1,list2)
print("list1: ",list1)
print("list2: ",list2)


# Actual argument and formal argument 

# Actual argument has 4 types: Position     Keyword     Default     Variable Length 

# Position

def person1(name,age):
    print(name)
    print(age)

person1("Jatin", 19)


# Keyword

def person2(name,age):
    print(name)
    print(age-5)

person2(age=19, name="Jatin")

#default

def person3(name,age=19):
    print(name)
    print(age)

person3("Jatin")

# Variable length 

def sum(*b):

    a = 0

    for i in b:
        a = a + i

    print(a)

sum(1,2,3,4,5,6)
