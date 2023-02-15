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
