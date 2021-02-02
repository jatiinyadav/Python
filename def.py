from functools import reduce

x = int(input("Enter the no. your check \n"))

def odd_even(x):
    if x%2==0:
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")

odd_even(x)

 
#Filter 

li = [1,2,3,4,5,6,7,8]

final_list = list(filter(lambda x: (x%2==0), li))

print(final_list)

final_list = list(filter(lambda x: (x%2!=0), li))

print(final_list)

#map

newli = [1,2,3,4,5,6,7,8,9]

new_final_list = list(map(lambda x: (x*x), newli))

print(new_final_list)

#reduce

reduce_list = (reduce(lambda x,y: x + y, li))

print(reduce_list)

