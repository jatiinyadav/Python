from functools import reduce

# x = int(input("Enter the no.:  "))

# l = lambda k: x + x

# result = l(x)

# print(result)

# # l(x)

# # print("THE SUM IS: ", l(x))

# #filter

new_list1 = [1,2,4,2,5,3]

final_list1 = list(filter(lambda x: x%2==0, new_list1))

print(final_list1)

final_list1 = list(filter(lambda x: x%2!=0, new_list1))

print(final_list1)

#map 

new_list2 = [1,4,36,3,7,4,2,5,8]

final_list2 = list(map(lambda i: i*i, new_list2))

print(final_list2)

#reduce 

new_list3 = [1,3,6,3,7,3,9,4,7,2,6,3,6]

final_list3 = (reduce(lambda i,j: i+j, new_list3))

print(final_list3)

