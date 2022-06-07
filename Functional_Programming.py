#higher-order functions take other functions as arguments and returns them as results.
def multiple_twice(func, arg):
    return func(func(arg) + func(arg))

def multiple(x):
    return x * x


print(multiple_twice(multiple, 2))  # ((x * x) + (x * x)) ** 2

# pure function - no side effects, and return value thad depends only on their arguments


def pure_function(x, y):
    return x * y + x


some_list = []


def impure(arg):  # this function changed the state of some_list
    some_list.append(arg)
