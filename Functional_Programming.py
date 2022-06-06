#higher-order functions take other functions as arguments and returns them as results.
def multiple_twice(func, arg):
    return func(func(arg) + func(arg))

def multiple(x):
    return x * x


print(multiple_twice(multiple, 2))  # ((x * x) + (x * x)) ** 2
