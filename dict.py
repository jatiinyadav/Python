import math as m
a = m.sqrt(337)
print(a)
values = ["1","2","3"]
names = ["I'm", "Jatin", "Yadav"]
des = dict(zip(values,names))
print(des)


l1 = ['1','2','3']
l2 = ['4','5','6']

for i in l1:
    for j in l2:
        print(i,j)

i = 1
n = 2
while(i<=5):
    print(n," * ", i , " = " ,  n*i)
    i +=1