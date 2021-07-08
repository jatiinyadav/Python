try:
    print("Resource Open")
    a = int(input("Enter no. 1: "))
    b = int(input("Enter no. 2: "))
    print(a/b)

except ZeroDivisionError as e:
    print("You can't do", e)

except ValueError as e:
    print("You can't do", e)

except Exception as e:
    print("Something went wrong..")

finally:
    print("Resource Closed")

print("Thankyou!")
