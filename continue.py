#for i in range(16):
        #continue
    #print(i)  


list = [2,3,4,5]
for i in list:
    if(i%3==0 or i%5==0):
        continue
    print(i)

print("-------")

list = [1,2,3,4,5,6]
for j in list:
    if(j%6!= 0):
        continue
    print(j, end="9 ")