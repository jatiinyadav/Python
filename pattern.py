# rows = 5
# for row in range(1, rows + 1):
#     for i in range(1, row + 1):
#         print(i , end = "")
#     print()
# print("------")


for i in range(4):
    for j in range(i+1):
        print("#", end="")

    print()


print("-------")


for i in range(5):
    for j in range(4-i):
        print("#", end="")

    print()