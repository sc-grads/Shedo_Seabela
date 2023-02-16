# YOUR CODE STARTS HERE
number_of_ip = 2 ** 128
no_of_digits = len(str(number_of_ip))
print(no_of_digits)

phone = {'Brand':'Samsung', 'Price':650.2, 'Seller': 'Nile'}
phone.update({'OS':'Android', 'Color': 'Black'})

phone = {'Brand':'Samsung', 'Price':650.2, 'Seller': 'Nile'}

# YOUR CODE STARTS HERE
price = phone['Price']
vat = format(price * 0.19, '.2f')
vat = float(vat)
print(vat)
