for i in range(1,21):
    if (i%3 == 0 and i%5 == 0):
        print("FIZZ BUZZ", i)
    elif(i%3 == 0):
        print("FIZZ" , i)
    elif(i%5==0):
        print("BUZZ", i)
    else:
        print(i)