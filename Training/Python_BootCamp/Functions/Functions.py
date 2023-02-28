# functins
def my_function():
    print('Hello world')

my_function()

def say_hi(name):
    """ this is a function to great you

    """
    print(f'Hello {name} how are you')

say_hi('Dell')

def difference(a, b):
    x = a - b
    print(x)

difference(8, 5)


# Write a function called get_vat() with 2 parameters, price and vat percentage
# It calculates and returns the VAT (value-added tax).
# YOUR CODE STARTS HERE
def get_vat(price, vat_percentage):
    vat = price * vat_percentage / 100
    return vat


get_vat(200, 5)

# Capture the returned value in a new variable called vat.

x = 3


def increment():
    global x
    x = x + 1


# Calling the function
increment()
print(x)


# Challenges
def unique(Sample_list = []):

    new_list = list(set(Sample_list))
    print(new_list)

unique([1, 2, 3, 3, 3, 3, 4, 5, 1, 3, 5, 5, 5])

def all_divisors(n):
    divisors = []
    for x in range(1, int(n/2)+1):
        if n % x == 0:
            divisors.append(x)
    return divisors


def perfect_number(n):
    divs = all_divisors(n)
    if sum(divs) == n:
        return True
    else:
        return False

n = 496
if perfect_number(n):
    print(f'{n} it\'s a perfect number')
else:
    print(f'Nothing special about {n}, it\'s no perfect number')

fac = 1
def factorial(n):
    for i in range(1, n+1):
        global fac
        fac = fac * i

    return fac

print(factorial(3))

def prime(n):
    divisors = []
    for x in range(1, int(n / 2) + 1):
        if n % x == 0:
            divisors.append(x)
    if len(divisors) <= 2:
        return True
    else:
        pass
prime(8)
print("DONE WITH FIRST FUNCTIONS")
primes = []
for n in range(1_000_000, 100_000_000):
   if prime(n):
       primes.append(n)
       if len(primes) == 5:
           break
print(primes)

def fibo():
    n = 100
    a, b = 0, 1
    while a <= n:
        print(a, ' ', end=' ')
        a, b = b, a + b
fibo()





