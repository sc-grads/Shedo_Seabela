# Challenges
from math import pi

# int, float, bool, string, list.
my_int, my_float, my_bool, my_string, my_list = 3, 3.5, True, 'This is a revison version', [3, 3.5, True, "This is a revision"]

print(f'These are data types {my_int}, {my_float}, {my_bool}, {my_string}, {my_list} \n')
print(f' of type {type(my_int)} {type(my_float)}, {type(my_bool)}, {type(my_string)}, {type(my_list)} respectively')

# A company's revenue is 45,897,513.
# Calculate the company's profit if the profit represents 12.7% of the revenue.
# Display the profit using 2 decimal places.
Revenue = 45_897_153
profit =  Revenue * 0.12
print(f'\nThe company\'s profit is : ', format(profit,'.2f'))
print('\n')
# am looping over a list  and printing it's values
for i in range(len(my_list)):
    print(my_list[i], end=" ")
print('\n')
print('\n')

# Write a Python script that extracts the MAC address (b4:6d:83:77:85:f3) from the string.
my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'
# print(my_str[34:]
modi_str = my_str.split('wlo1 Link encap:Ethernet HWaddr ')

print(f'below is the MAC address accessed using the split method: \n {modi_str[1]}')

print('')
# function to calculate the acceleration
def accele():

    v1, v2, t1, t2 = 0, 10, 0, 20
    acc = (v2 - v1) / (t2 - t1)
    print(acc)
accele()

# function to calculate the volume of liquid in a sphere
def volume(h, r = 10):
    vol = (4 * pi * r**3)/3 - (pi * h**2 *(3*r - h))/3
    return vol

volumee = volume(2)

print(format(volumee,'.5f'))

l1 = [1, 2, 3]
l2 = (4, 5, 6)

for x in range(3):
    sum = l1[x] + l2[x]
    print(sum)