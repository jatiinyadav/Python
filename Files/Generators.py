def TopTen():

    n = 1

    while n<= 10:
        sq = n * n
        yield sq
        n += 1

values = TopTen()

print(values.__next__())
print(values.__next__())
print(values.__next__())

for i in values:
    print(i)



# Normally
# def TopTen():

#     n = 1

#     while n <=10:
#         sq = n * n
#         n += 1

#     return sq

# values = TopTen()

# print(values)

# for i in values:
#     print(i)