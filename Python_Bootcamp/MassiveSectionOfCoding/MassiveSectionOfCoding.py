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

my_list = [1, 2.3, 'abc', (5, 6, 'x', 'y')]
my_var = str(my_list[1]) + my_list[2][0] + my_list[-1][-1]
print(my_var)

languages = ['English', 'Python', 'Java', 'Golang', 'German']
languages = languages[1:4]

my_list = list(range(-20, 10, 3))

days = [10, 11, 13, 14, 15]
days.insert(2,12)

message = 'Wow! Python is great'
vowels = 'aeio'
no_vowels = [x for x in message if x not in vowels and x != ' ']
print(no_vowels)

names1 = {'John', 'Marry', 'Lena', 'Pollux'}
names2 = {'Dan', 'Arthur', 'Marry', 'Lena', 'Castor'}
names = names1 & names2
names = list(names)
