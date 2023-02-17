# defining an outer function
def outer():
    msg = 'Python'
    x = 0


    def inner():

        nonlocal x
        x += 1
        print(f'{msg} is really cool!')
        return x

    return inner


func1 = outer()
print(type(func1))

xx = func1()
print(xx)

print(func1())
print(func1())

import functools


def my_new_decorator(just_a_func):
    @functools.wraps(just_a_func)  # preserving __name__ and __doc__
    def wrapper_my_new_decorator(*args, **kwargs):
        print('Extra code before calling just_a_func()')
        result = just_a_func(*args, **kwargs)
        print('Extra code after calling just_a_func()')
        return result

    return wrapper_my_new_decorator


@my_new_decorator
def just_a_func(x):
    """
    This is the docstring of just_a_func.
    """
    print(f'I\'m just a function. x = {x}')
    return x * x


result = just_a_func(100)
print(f'Returned value result: {result}')

print(f'Function\'s name: {just_a_func.__name__}')
print(f'{just_a_func.__doc__}')

from functools import wraps


# defining a decorator
def timer(fn):
    from time import time

    @wraps(fn)
    def wrapper_timer(*args, **kwargs):  # this is a generic decorator
        start_time = time()  # retrieving the current timestamp
        result = fn(*args, **kwargs)
        end_time = time()
        print(f'{fn.__name__} execution time:{end_time - start_time}')
        return result

    return wrapper_timer


# decorating the function
@timer
def sum_of_powers(n, p):
    nums = [x ** p for x in range(1, n)]
    return sum(nums)


s = sum_of_powers(1000000, 2)
print(s)

s = sum_of_powers(1000000, 3)
print(s)

s = sum_of_powers(1000000, 5)
print(s)