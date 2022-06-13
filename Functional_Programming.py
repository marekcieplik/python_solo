def double_(func, arg):
    u"""
    higher-order functions take other functions as arguments, or returns them as results.
    """
    return 2 * func(arg)


def power(x):
    u"""pure function - no side effects, and return value thad depends only on their arguments"""
    return x * x


def lambdas_instead_higher_order(func, arg):
    return func(arg)  # print(lambdas_instead_higher_order(func_spam, 5))


def func_spam(x):
    return 2 * x * x


lambdas_egg = lambda x: 2 * x * x  # print( lambda_egg(5)
u'''In this case better is pure function, e.g. 
def double_power(x)
    return 2 * x * x
'''


def pure_function(x, y):
    u'''pure function - no side effects, and return value thad depends only on their arguments'''
    return x * y + x


some_list = []


def impure(arg):
    u"""impure function changed the state of some_list, which is no argument"""
    some_list.append(arg)


"""
Why using pure function?
() easier to write and reason about,
() easier to test.
() memoization, result can be stored and referred to the next time, e.g. 
value = pure_function(2, 3)
print(value ** value)
"""


def pure_function_butter_than_assign_lambda(x, y):
    return 2 * x + 3 * y - 13


if __name__ == '__main__':
    print('lambdas_instead_higher_order', lambdas_instead_higher_order(func_spam, 5))  # 50
    print('lambdas_egg ', lambdas_egg(5))  # 50 == 2 * x * x
    print('lambda      ', (lambda k: 2 * k * k)(5))  # 50 == 2 * k * k

    print('pure_function_butter_than_assign_lambda:', pure_function_butter_than_assign_lambda(2, 3))
    print('lambda: ', (lambda x, y: 2 * x + 3 * y - 13)(2, 3))
