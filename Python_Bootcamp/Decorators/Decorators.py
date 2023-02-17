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