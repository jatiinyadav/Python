# def start_end_decorator(func):

#     def wrapper(number):
#         print("Start")
#         result = func(number)
#         print("End")

#         return result

#     return wrapper

# @start_end_decorator
# def func(number):
#     print("Inside func")
#     return number + 5 

# result = func(5)
# print(result)

# def print_name():
#     print("Jatin Yadav")

# print_name()




def func1(func):

    def now():
        print("Start")
        func()
        print("End")

    return now

@func1
def func():
    print("Jatin Yadav")

# func = func1(func)

func()