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

phone1 = ['1111', '2222', '2222', '1111']
phone2 = ['1111', '3333', '3333', '1111']
phone_numbers = set(phone1) | set(phone2)

mac = ['b4:6d:83:77:85:f3', 'b4:6d:83:77:85:f3', 'a4:6d:83:77:85:f4', 'c4:6d:83:77:85:f3', 'b4:6d:83:77:85:f3']

# New empty list
mac_unique = list()

# Iterate over the list
for item in mac:
    if item not in mac_unique:  # check if each element is already in mac_unique list
        mac_unique.append(item)  # add it if it's not in the mac_unique list

print(mac_unique)

years = [2010, 2010, 2011, 2011, 2012, 2012, 2012]

# New list with unique elements
years_unique = []

[years_unique.append(item) for item in years if item not in years_unique]

print(years_unique)

words = ['Anna', 'Car', 'Civic', 'Screen', 'Level', 'Cat', 'Mom']

palindromes = [items for items in words if items.lower() == items[::-1].lower()]

print(palindromes)


def remove_from_list(my_list, item):
    """
    Function that removes an item from a list.
    """
    while (item in my_list):
        my_list.remove(item)


list1 = [1, 2, 1, 1, 1, 1, 3]

remove_from_list(list1, 1)

print(list1)


def vowel_count(my_str):
    """
    This function counts the number of vowels in a string
    """
    vowels = 'aeiou'
    my_str = my_str.lower()  # ignoring the case (we consider only lower-case letters)

    # Dictionary that stores the result.
    result = dict()

    for char in my_str:
        if char in vowels:
            if char in result.keys():
                result[char] += 1
            else:
                result[char] = 1

    return result


r = vowel_count('Awesome')
print(r)

r = vowel_count('Wow! Python is great!')
print(r)


def counter(my_str):
    vowels = 'aeiou'
    no_of_vowels = 0

    # letter case doesn't matter
    my_str = my_str.lower()  # make a lowercase copy of my_str

    for char in vowels:
        no_of_vowels += my_str.count(char)

    no_of_consonants = len(my_str) - no_of_vowels

    return (no_of_vowels, no_of_consonants)


print(counter('Python'))
print(counter('BeautifUl'))

countries = ['USA', 'UK', 'France', 'Romania', 'France', 'Germany', 'USA', 'Canada', 'India', 'UK']

# Removing duplicates from list by transforming it to a set and then back to a list
countries = list(set(countries))
countries.sort()

print(countries)

with open('show_arp.txt', 'r', newline='') as f:
    # Reading file in list (each line is list element)
    contents = f.read().splitlines()

    # The argument newline='' is necessary only in Windows

    # Eliminating the first item from the list (files header)
    contents = contents[1:]

    # Empty list that stores tuples like (ip, mac)
    ip_mac = list()

    # Iterating over the list(file contents) line by line
    for line in contents:
        ip = line.split()[1]  ## Getting the IP
        mac = line.split()[3]  ## Getting the MAC

        # Adding the tuple to the ip_mac list
        ip_mac.append((ip, mac))

    print(ip_mac)