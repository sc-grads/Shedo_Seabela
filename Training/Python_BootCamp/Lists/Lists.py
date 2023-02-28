# create a list named my_list with 4 elements: a float, an integer, a string and another list

my_list = [1.3, 2, 'hello', [1, 'a']]

# x is the 2nd element of my_list
x = my_list[1]

# y is the second element of the list which is the 4th element of my_list
y = my_list[1:][-1][-1]


# list slicing that returns a new list called z with the first 2 elements of my_list
z = my_list[:2]

names_list = ['Alice', 'Bob', 'Eve']
# # Converting list to string
names_str = ','.join(names_list)


url = 'www.python.org'
# # Converting string to list
url_list = url.split(".")

animals = ['Cat', 'Dog']

# ##### YOUR CODE STARTS HERE
animals.append('Donkey')

# # 1. Add an element at the end of the list. The new element will be the string 'Donkey'.

# # animals will be ['Cat', 'Dog', 'Donkey']




# #2. Add an element at position 2. This will be the 2nd element and will store the string 'Horse'
# # animals will be ['Cat', 'Horse', 'Dog', 'Donkey']



animals.insert(1, "Horse")
# #3. Return the index of the element with value 'Cat' in variable called cat_index
cat_index = animals.index("Cat")



# #4. Create a string variable named str_animals from the list by joining the elements of the list using '-' as a delimiter.

# # str_animals will be 'Cat-Horse-Dog-Donkey'
str_animals = '-'.join(animals)

miles = [12, 10, 26, 80]

# 1 mile = 1.609 km

# YOUR CODE STARTS HERE
km = [x * 1.609 for x in miles]
print('distance in km: ', km)

# Challenges

lisst = [1, 2, 1, 1, 2, 3]

# item to remove from the list
n = 1
while n in lisst:
    lisst.remove(n)

print(lisst)

new_list = []
for i in lisst:
    if i not in new_list:
        new_list.append(i)

print(new_list)

nums = '10,20,30,40,50'
nums_list = nums.split(',')
nums1 = [int(n) for n in nums_list]
print(nums1)

new = []
for x in range(1500, 3203):
    if x % 7 == 0 and x % 5 != 3203:
        new.append(x)
print(new)
userwords = input('Enter some words:')
words_list = userwords.split(' ')
words_reversed = ' '.join(reversed(words_list))
print(words_reversed)
