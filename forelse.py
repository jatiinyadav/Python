nums = [2,4,5,9,10]
for j in nums:
    if (j%5==0):
        print('The no. ' +  str(j) +  ' is a multiple of 5' )
        continue
else: 
    print("Not a multiple of 5") 